# Areas to Work On

These are topics that came up frequently in interviews or are weak spots based on question patterns.
Priority = frequency × depth expected.

---

## Priority 1 — High Frequency, Must Master

### Decorators & Generators (asked 4x each)
- Know how to write a custom decorator from scratch
- Know how `yield` works, difference between generator and iterator
- Real-world use cases: `@property`, `@staticmethod`, `@lru_cache`, logging decorator, auth decorator

### OOP in Python (asked 4x)
- Be able to explain all 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction
- MRO — explain with diamond problem
- Abstract class vs Interface (ABC module)
- `__init__`, `__str__`, `__repr__`, `__len__`, `__eq__` — top dunder methods

### List vs Tuple vs Set vs Dict (asked 3x in multiple forms)
- Memory layout difference
- Mutability and hashability rules (why tuple can be dict key, list cannot)
- Time complexity: list lookup O(n), dict lookup O(1)
- When to use which

### Joins in SQL / Pandas (asked 3x)
- INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF join — know all with examples
- Write queries confidently: top-N, no-match patterns, GROUP BY + HAVING

---

## Priority 2 — Medium Frequency, Should Know Well

### RAG Architecture
- Full pipeline: PDF → chunking → embedding → vector store → retrieval → LLM
- Types of chunking (fixed, recursive, semantic)
- Hybrid search (dense + sparse)
- How to reduce hallucination

### LangChain / LangGraph
- Difference between the two
- Types of chains in LangChain
- Nodes, edges, state in LangGraph
- HITL (Human-in-the-Loop) implementation

### Multithreading vs Multiprocessing vs Async IO
- Know when to use each
- GIL — what it is, why it matters for threads
- `asyncio`, `await`, event loop basics

### Flask vs FastAPI vs Django
- Performance differences
- When to choose which
- Authentication pattern in FastAPI (JWT, OAuth2)

---

## Priority 3 — Asked Once but Conceptually Important

### Advanced Python
- Shallow vs deep copy (mutable traps)
- `for-else` — rare but asked
- `@property` — getter/setter pattern
- `dataclass` — auto `__init__`, `__repr__`, immutability with `frozen=True`
- SOLID principles — at least S (Single Responsibility) and O (Open/Closed)

### Vector Databases & Embeddings
- How embeddings are created (e.g., `sentence-transformers`, OpenAI embeddings)
- FAISS — flat index, IVF, HNSW
- Cosine similarity vs Euclidean distance — formula and when each applies

### Transformer Architecture
- Self-attention mechanism
- Difference from RNN/LSTM (parallelism, long-range dependencies)
- Why transformers are better for NLP tasks

### System Design & Design Patterns
- Common patterns: Singleton, Factory, Observer
- Know at least 2-3 applied to Python projects

---

## Coding Problems to Practice

| Problem | Frequency |
|---------|-----------|
| Flatten nested list | ⭐⭐ (asked 2x) |
| Merge overlapping intervals | ⭐ |
| Count word frequency in a sentence | ⭐ |
| Remove vowels from string | ⭐ |
| Find unique characters in string | ⭐ |
| Matrix transpose | ⭐ |
| Sort list without set | ⭐ |
| Check if URLs are reachable | ⭐ |

---

## Concepts You Should Be Able to Explain + Code

- Custom decorator (with and without arguments)
- Generator function with `yield`
- Flatten nested array (recursive and iterative)
- Merge intervals algorithm
- Stack using a class
- JWT-based auth in FastAPI
- Simple RAG pipeline (pseudocode is fine)
