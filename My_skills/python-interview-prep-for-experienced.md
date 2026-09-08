# Brushing Up Python by Building a Library Catalog & Analytics CLI

## Who this is for
You're an experienced engineer (4 years in AI/ML) who codes daily, but recent interview feedback flagged gaps in core Python fundamentals — the `list`/`set`/`dict`/`tuple` and function idioms interviewers love to probe. This isn't a "learn Python from zero" tutorial. It moves fast, skips basic syntax explanations, and instead drills into the *exact* patterns and scenario questions that show up in interviews, using a small real build as the vehicle so the practice isn't disconnected flashcards.

## What you'll build
A command-line **Library Catalog & Analytics tool** that:
- Stores books with metadata (title, author, year, genres)
- Finds books by author, genre overlap, or year range
- Reports analytics (most common genre, duplicate detection, author frequency)
- Uses immutable records where mutability would be a bug, not a feature

## What you'll learn
- `list` — comprehensions, slicing tricks, sorting with custom keys, when list ops are O(n) and why that matters
- `dict` — comprehensions, `.get()` vs `[]`, `defaultdict`/`Counter`, dict as a routing/lookup table, merging dicts (and the interview trap of shallow vs deep merges)
- `set` — dedup, intersection/union/difference for "overlap" style questions, why sets can't hold unhashable types
- `tuple` — immutability as a design choice, tuples as dict keys, named tuples for readable interview code
- Functions — default args (and the classic mutable-default-argument bug), `*args`/`**kwargs`, closures, and when a generator beats a list
- 10 scenario-style problems mirroring frequently-asked interview questions, solved *in the context of* the catalog app, plus a standalone practice bank at the end

## Prerequisites
- Python 3.10+ installed
- Comfortable with basic syntax (loops, if/else, defining functions) — this skips that

## Project setup

```
library_catalog/
├── catalog.py        # core data + operations
├── analytics.py       # aggregate/report functions
├── cli.py             # entry point
└── tests/
    └── test_catalog.py
```

Production habit worth calling out immediately: separating **data operations** (`catalog.py`), **derived reporting** (`analytics.py`), and the **interface** (`cli.py`) is exactly the kind of structure interviewers expect you to reach for even in a 20-line take-home — it signals you don't dump everything in `main()`.

---

## Step 1: Model a book — tuples vs dicts, and why the choice matters

```python
# catalog.py
from typing import NamedTuple

class Book(NamedTuple):
    isbn: str
    title: str
    author: str
    year: int
    genres: frozenset[str]
```

**Why a `NamedTuple` and not a plain dict?** A book's identity (ISBN, title, year) shouldn't change once created — that's a tuple's whole selling point: immutability. Using a mutable `dict` here would let any function silently rewrite a book's year mid-program, which is exactly the kind of bug interviewers ask about when they say "what's wrong with using a dict here?" `NamedTuple` also gives you `.title` instead of `book['title']` — more readable, and it's hashable, so it can go straight into a `set`.

**Interview checkpoint:** *"Why can't you put a `list` of genres in this tuple?"* — Because lists are unhashable and mutable, and mutable fields silently poison a tuple's hashability. That's why `genres` is a `frozenset`, not a `list` or `set`.

Checkpoint: run `Book("001", "Dune", "Herbert", 1965, frozenset({"scifi"}))` in a REPL and confirm `hash(book)` works, but would fail with a plain `set`.

---

## Step 2: Store and look up books — dict as the workhorse

```python
class Catalog:
    def __init__(self):
        self._books: dict[str, Book] = {}          # isbn -> Book
        self._by_author: dict[str, list[str]] = {}  # author -> [isbn,...]

    def add(self, book: Book) -> None:
        self._books[book.isbn] = book
        self._by_author.setdefault(book.author, []).append(book.isbn)
```

**Why two dicts instead of scanning a list every time?** `_books` gives O(1) lookup by ISBN. `_by_author` is a classic **inverted index** — instead of scanning every book to find an author's works (O(n) every query), you pay a small cost on insert to get O(1) lookups later. This trade-off — precompute an index vs. scan on demand — is one of the most common "how would you speed this up" interview follow-ups.

`setdefault` is doing real work here: it avoids the "check if key exists, then append" two-step, and it's the direct answer to the classic interview question *"what does `dict.setdefault` do and when would you use it over `.get()`?"*

**Interview checkpoint — mutable default argument trap:**
```python
def add_with_bug(self, book, tags=[]):   # DON'T DO THIS
    tags.append("new")
    ...
```
This is the single most common Python "gotcha" interviewers test. Default arguments are evaluated **once**, at function definition time — so every call without an explicit `tags` shares the *same* list, and mutations leak across calls. The fix: `tags=None`, then `tags = tags or []` inside the function.

---

## Step 3: Genre overlap — where `set` earns its keep

```python
def shared_genres(self, isbn_a: str, isbn_b: str) -> frozenset[str]:
    return self._books[isbn_a].genres & self._books[isbn_b].genres
```

**Scenario question this mirrors:** *"Given two collections, find what they have in common."* This shows up constantly (common friends, common tags, common skills between two resumes). The naive approach is nested loops (O(n·m)); converting to sets and using `&` is O(min(n,m)) and, more importantly, it's the *idiomatic* answer interviewers are listening for.

Related set ops worth having cold:
```python
a | b   # union — everything in either
a - b   # difference — in a but not b
a ^ b   # symmetric difference — in exactly one of the two
```

**Interview checkpoint:** *"Find genres unique to book A that book B doesn't have."* → `a.genres - b.genres`.

---

## Step 4: Search and sort — list comprehensions and custom sort keys

```python
def books_between(self, start_year: int, end_year: int) -> list[Book]:
    return sorted(
        (b for b in self._books.values() if start_year <= b.year <= end_year),
        key=lambda b: (b.year, b.title),
    )
```

**Why a generator expression inside `sorted()` instead of a list comprehension?** `sorted()` needs to iterate the whole thing anyway, so building an intermediate list first just wastes memory. This is the practical answer to *"what's the difference between a generator and a list comprehension, and when do you use each?"* — use a generator when something else is going to consume the whole sequence once; use a list when you need to index into it, reuse it, or check its length.

**Interview checkpoint — tuple sort keys:** `key=lambda b: (b.year, b.title)` sorts by year, then alphabetically breaks ties by title — this "sort by multiple fields" pattern via tuple keys is asked constantly and trips people up when they reach for multiple `.sort()` calls instead.

---

## Step 5: Analytics — `Counter`, `defaultdict`, and dict merging

```python
# analytics.py
from collections import Counter

def most_common_genre(books: list[Book]) -> str:
    counts = Counter(g for b in books for g in b.genres)
    return counts.most_common(1)[0][0]

def author_frequency(books: list[Book]) -> dict[str, int]:
    return dict(Counter(b.author for b in books))
```

**Why `Counter` instead of hand-rolling a dict with `+= 1`?** You *can* write the manual version (and you should be able to, on request — it's `d[key] = d.get(key, 0) + 1`), but `Counter` is the standard-library answer, and knowing it exists (plus `.most_common()`) is exactly the kind of "do you know the tools" signal interviewers are checking for.

**Scenario question — merging dicts (the trap):**
```python
def merge_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    merged = a | b          # Python 3.9+: shallow merge, b's values win on collision
    for k, v in b.items():
        merged[k] = merged.get(k, 0) + (v if k in a else 0)
    return merged
```
The trap: `a | b` (or `{**a, **b}`) does a **shallow overwrite**, not a sum — if both dicts have `"scifi": 3`, the naive merge gives you `3`, not `6`. Interviewers ask this specifically to see if you know dict-union syntax *and* know its limits.

---

## Step 6: Deduplication — the classic list-to-set-and-back

```python
def unique_isbns_preserving_order(isbns: list[str]) -> list[str]:
    seen: set[str] = set()
    result = []
    for isbn in isbns:
        if isbn not in seen:
            seen.add(isbn)
            result.append(isbn)
    return result
```

**Scenario question this mirrors almost verbatim:** *"Remove duplicates from a list while preserving order."* `list(set(isbns))` is the wrong answer here — sets don't preserve order (and pre-3.7 dict/set ordering guarantees are a common point of confusion interviewers probe). The `seen` set + manual loop is the correct idiomatic answer, and doubles as a chance to explain *why* `in` on a `set` is O(1) but `in` on a `list` is O(n) — which is the real point of the question.

---

## Testing it

```python
# tests/test_catalog.py
import pytest
from catalog import Catalog, Book

def make_book(isbn="1", author="Herbert", year=1965, genres=("scifi",)):
    return Book(isbn, "Dune", author, year, frozenset(genres))

def test_setdefault_builds_author_index():
    c = Catalog()
    c.add(make_book("1"))
    c.add(make_book("2", author="Herbert"))
    assert c._by_author["Herbert"] == ["1", "2"]

def test_shared_genres_uses_set_intersection():
    c = Catalog()
    c.add(make_book("1", genres=("scifi", "adventure")))
    c.add(make_book("2", genres=("scifi", "drama")))
    assert c.shared_genres("1", "2") == frozenset({"scifi"})
```

Why these two specifically: they test the two patterns interviewers most often ask you to *explain*, not just write — the inverted-index dict and the set-intersection lookup. A test that only checks "does `add()` work" wouldn't tell you anything useful; testing the *reasoning*-heavy parts is what's worth your time here.

## What makes this production-grade (recap)
- `NamedTuple` for immutable records instead of loosely-typed dicts
- An inverted index (`_by_author`) traded a small write cost for fast reads — a deliberate, explainable trade-off, not an accident
- `Counter`/`defaultdict` used instead of hand-rolled counting dicts, because reaching for the standard library where it fits is itself a signal of experience
- Tests target the *reasoning*, not just "does it run"

## Scenario-style practice bank (solve these cold, no app needed)
1. Given two lists, return their intersection without using `set()` explicitly twice (try both the set and two-pointer-on-sorted-lists approaches).
2. Flatten an arbitrarily nested list of lists.
3. Given a list of `(name, score)` tuples, return the name with the highest score — without importing anything.
4. Explain, out loud, why `{1: "a"} == {1: "a", **{}}` but two dicts with the same items in different insertion order still compare equal — and where insertion order *does* matter (iteration, `repr`, Python 3.7+ guarantees).
5. Write a decorator that caches a function's results using a dict — then explain why the dict key has to be hashable, tying back to Step 1.
6. Given a list of words, return the top-3 most frequent using only `dict`, then redo it with `Counter`.
7. Why does `list.append()` amortize to O(1) but inserting at index 0 is O(n)? What data structure would you reach for if you needed fast inserts at both ends?
8. What's the output of this, and why:
   ```python
   def f(x, cache={}):
       cache[x] = cache.get(x, 0) + 1
       return cache
   print(f(1)); print(f(2))
   ```
9. Given two sets of user IDs (this week's active users, last week's active users), compute: churned users, new users, retained users — in one line each.
10. Explain the difference between `is` and `==` for tuples specifically, and why it can surprise people coming from other languages.

## Where to go next
- Redo Steps 2–6 without looking, from memory, timing yourself — the goal is fluency under pressure, not just having seen it once
- Add a `most_prolific_decade()` analytics function using `Counter` and integer division on `year`
- Try the practice bank against a friend or in a mock interview setting and explain your reasoning out loud, not just the code
