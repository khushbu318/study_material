# Python Interview Questions

Importance: ⭐⭐⭐ = Asked 3+ times | ⭐⭐ = Asked 2 times | ⭐ = Asked once

---

## OOP Concepts

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is OOP in Python / Explain OOP | 4x (Q6, Q124, Q139, Q147) | ⭐⭐⭐ |
| What is inheritance and its types | 3x (Q4, Q15, Q91) | ⭐⭐⭐ |
| What is abstract class and interface in Python | 2x (Q14, Q138) | ⭐⭐ |
| What is `__init__` and its use | 2x (Q39, Q107) | ⭐⭐ |
| Top 5 dunder (magic) functions | 2x (Q36, Q96) | ⭐⭐ |
| What is MRO (Method Resolution Order) in inheritance | 1x (Q15) | ⭐ |
| What is overloading and overriding | 1x (Q90) | ⭐ |
| What is `self` in class and why it is needed | 1x (Q97) | ⭐ |
| What is property in Python (`@property`) | 1x (Q37) | ⭐ |
| What is data class and its use | 1x (Q38) | ⭐ |
| What are SOLID principles and where did you use them | 1x (Q125) | ⭐ |

---

## Data Structures & Types

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is list vs tuple — how do they differ | 3x (Q2, Q23, Q94) | ⭐⭐⭐ |
| In context of memory — list vs set vs dict vs tuple (which is best) | 2x (Q40, Q108) | ⭐⭐ |
| What is shallow copy vs deep copy | 2x (Q3, Q16) | ⭐⭐ |
| Can list or tuple be the key of a dictionary | 1x (Q93) | ⭐ |
| How is tuple more memory efficient than list | 1x (Q94) | ⭐ |
| Look-up time in list vs dict — which is memory efficient | 1x (Q41) | ⭐ |
| What is slicing | 1x (Q101) | ⭐ |
| How to get 0th and 3rd item using slicing | 1x (Q102) | ⭐ |
| List, Dict, String built-in functions | 1x (Q89) | ⭐ |
| How to remove a specific key:value pair from a dictionary | 1x (Q100) | ⭐ |
| What is the `zip` function | 1x (Q95) | ⭐ |
| `9/2` vs `9//2` difference | 1x (Q92) | ⭐ |

---

## Functions & Advanced Python

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What are decorators and their use cases | 4x (Q21, Q35, Q98, Q142) | ⭐⭐⭐ |
| What are generators and their use | 4x (Q22, Q99, Q142, Q154) | ⭐⭐⭐ |
| What is `for-else` in Python and how to use it | 1x (Q1) | ⭐ |
| Generators vs iterators | 2x (Q111, Q154) | ⭐⭐ |
| What is serialization | 2x (Q33, Q106) | ⭐⭐ |
| What is `async` IO | 2x (Q111, Q129) | ⭐⭐ |
| What is multithreading vs multiprocessing | 2x (Q26, Q112) | ⭐⭐ |
| When to use async-IO vs multiprocessing vs multithreading | 1x (Q113) | ⭐ |
| What is GIL (Global Interpreter Lock) and its importance | 1x (Q114) | ⭐ |
| Memory management in Python | 1x (Q151) | ⭐ |
| What is exception handling | 1x (Q87) | ⭐ |
| What is `else` block in exception handling and why use it | 1x (Q88) | ⭐ |

---

## Data Structures / DSA

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is a Linked List | 1x (Q9) | ⭐ |
| Create a Stack class with push, pop, display | 1x (Q8) | ⭐ |
| Time complexity of push function of stack | 1x (Q7) | ⭐ |

---

## Coding Problems (Written in Interview)

| Problem | Times Asked | Importance |
|---------|-------------|------------|
| Flatten nested array: `[1,2,[3,4],[5,6]]` → `[1,2,3,4,5,6]` | 2x (Q25, Q109) | ⭐⭐ |
| Merge overlapping intervals: `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]` | 1x (Q86) | ⭐ |
| Count word occurrences in a sentence | 1x (Q134) | ⭐ |
| Remove vowels from string | 1x (Q59) | ⭐ |
| Get characters that appear only once in a string: `"abkkkb"` → `"a"` | 1x (Q155) | ⭐ |
| Matrix transpose | 1x (Q126) | ⭐ |
| Sort list without using set | 1x (Q18) | ⭐ |
| Check if URL is working — given array of URLs return true/false | 1x (Q5) | ⭐ |

---
---
---
# Python Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience working extensively with Python, FastAPI, Flask, Machine Learning, LLMs, REST APIs, asynchronous programming, and cloud deployments.

---

# OOP Concepts

## 1. What is OOP in Python?

Object-Oriented Programming (OOP) is a programming paradigm where code is organized into objects that encapsulate both data (attributes) and behavior (methods). It helps in writing modular, reusable, and maintainable code.

### Four Pillars of OOP
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### Real-world Usage
In AI applications, I use OOP to build reusable components such as:
- Model classes
- Data preprocessing pipelines
- API services
- Database repositories
- Vector store wrappers

Example:

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name
```

---

## 2. What is Inheritance? Explain its Types.

Inheritance allows one class to acquire properties and methods of another class, promoting code reuse.

### Types

### Single Inheritance

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

### Multiple Inheritance

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

### Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

### Hierarchical Inheritance

```python
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

### Hybrid Inheritance

Combination of multiple inheritance types.

### Real-world Usage

I use inheritance while creating:
- Base LLM classes
- Common API clients
- Database repositories
- Authentication modules

---

## 3. What is an Abstract Class and Interface?

### Abstract Class

An abstract class cannot be instantiated directly and contains one or more abstract methods.

```python
from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def predict(self):
        pass
```

### Interface in Python

Python doesn't have interfaces like Java.

We use abstract classes where every subclass must implement required methods.

### Real-world Usage

Used while designing:
- LLM Providers
- Vector Database Connectors
- Storage Services

---

## 4. What is `__init__`?

`__init__` is a constructor that gets executed automatically whenever an object is created.

Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Purpose

- Initialize object attributes
- Dependency Injection
- Default configurations

---

## 5. Top 5 Dunder (Magic) Methods

### `__init__`

Constructor

### `__str__`

Readable string representation

```python
def __str__(self):
    return self.name
```

### `__repr__`

Developer representation

### `__len__`

Called by `len()`

### `__call__`

Makes an object callable

```python
obj()
```

---

## 6. What is MRO (Method Resolution Order)?

MRO defines the order in which Python searches parent classes when multiple inheritance exists.

Python uses the **C3 Linearization Algorithm**.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

---

## 7. What is the Diamond Problem in Python? How does MRO solve it?

The **Diamond Problem** occurs in multiple inheritance when a class inherits from two classes that both inherit from the same parent class. This creates ambiguity about which parent method should be executed.

Python resolves this ambiguity using **Method Resolution Order (MRO)**, which follows the **C3 Linearization Algorithm** to determine a consistent order for searching classes.

### Example

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()

print(D.mro())
```

### Output

```text
B

[<class '__main__.D'>,
 <class '__main__.B'>,
 <class '__main__.C'>,
 <class '__main__.A'>,
 <class 'object'>]
```

### Explanation

When `obj.show()` is called, Python searches for the method in the following order:

1. `D`
2. `B`
3. `C`
4. `A`
5. `object`

Since `B` implements `show()`, Python executes `B.show()` and stops searching.

### Real-world Usage

In large Python applications, such as AI frameworks, FastAPI services, or SDK development, multiple inheritance is sometimes used for combining functionalities like authentication, logging, caching, and validation. Understanding MRO helps avoid unexpected behavior and makes debugging inheritance hierarchies much easier.
---

## 8. Overloading vs Overriding

### Method Overloading

Python does not support traditional method overloading.

We simulate it using:
- Default arguments
- `*args`
- `**kwargs`

### Method Overriding

Child class provides its own implementation.

```python
class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

## 9. What is `self`?

`self` refers to the current object.

It allows access to:

- Instance variables
- Instance methods

Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## 10. What is `@property`?

`@property` converts a method into an attribute.

Example

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
```

Benefits

- Data validation
- Encapsulation
- Read-only properties

---

## 11. What is a Data Class?

Introduced in Python 3.7.

Automatically generates:

- __init__
- __repr__
- __eq__

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Useful for DTOs, API schemas, ML configurations.

---

## 12. SOLID Principles

- S — Single Responsibility
- O — Open/Closed
- L — Liskov Substitution
- I — Interface Segregation
- D — Dependency Inversion

### Where I Used Them

- FastAPI services
- Repository Pattern
- AI model abstraction
- LLM integrations
- Authentication modules

---

# Data Structures & Types

## 13. List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Slower | Faster |
| Higher memory | Lower memory |
| Dynamic | Fixed |

Use List for changing data and Tuple for constant configurations.

---

## 14. List vs Set vs Dict vs Tuple (Memory)

| Type | Ordered | Mutable | Lookup |
|-------|----------|----------|---------|
| List | Yes | Yes | O(n) |
| Tuple | Yes | No | O(n) |
| Set | No | Yes | O(1) |
| Dict | Yes | Yes | O(1) |

Tuple is the most memory efficient.

---

## 15. Shallow Copy vs Deep Copy

>A shallow copy creates a new outer object, but the nested objects inside it are still references to the original objects. So changes to nested mutable objects can affect both copies. A deep copy recursively creates copies of the nested objects as well, so modifications to the copied nested objects do not affect the original. In Python, shallow copying can be done using copy.copy() and deep copying using copy.deepcopy().

### Shallow Copy

Copies only the outer object.

```python
import copy

b = copy.copy(a)
```

```
Original                  Shallow Copy

┌──────────────┐          ┌──────────────┐
│ Outer Box    │          │ Outer Box    │
│              │          │              │
│ ┌──────────┐ │          │ ┌──────────┐ │
│ │Inner Box │←┼──────────┼→│Inner Box │ │
│ └──────────┘ │          │ └──────────┘ │
└──────────────┘          └──────────────┘

```

### Deep Copy

Recursively copies nested objects.

```python
b = copy.deepcopy(a)
```
```
Original                  Deep Copy

┌──────────────┐          ┌──────────────┐
│ Outer Box    │          │ Outer Box    │
│              │          │              │
│ ┌──────────┐ │          │ ┌──────────┐ │
│ │Inner Box │ │          │ │Inner Box │ │
│ └──────────┘ │          │ └──────────┘ │
└──────────────┘          └──────────────┘

     Different inner boxes
```
---

## 16. Can List or Tuple be Dictionary Keys?

List ❌

Because it is mutable.

Tuple ✅

Only if all elements inside are immutable.

---

## 17. Why is Tuple More Memory Efficient?

- Immutable
- Smaller memory footprint
- Faster iteration
- Optimized internally

Useful for coordinates, configurations, cache keys.

---

## 18. Lookup Time

List

O(n)

Dictionary

O(1)

Dictionary uses a hash table.

---

## 19. What is Slicing?

Slicing extracts a portion of a sequence.

```python
arr[1:5]
```

Syntax

```python
[start:end:step]
```

---

## 20. Get 0th and 3rd Item Using Slicing

```python
arr = [1,2,3,4,5]

result = arr[0:4:3]

print(result)
```

Output

```
[1,4]
```

---

## 21. Common Built-in Functions

### List

| Function | Description | Example | Output |
|---|---|---|---|
| `append()` | Adds a single element to the end of a list. | `numbers = [1, 2]`<br>`numbers.append(3)` | `[1, 2, 3]` |
| `extend()` | Adds all elements from another iterable to the end of a list. | `numbers = [1, 2]`<br>`numbers.extend([3, 4])` | `[1, 2, 3, 4]` |
| `remove()` | Removes the first occurrence of a specified value. | `numbers = [1, 2, 3]`<br>`numbers.remove(2)` | `[1, 3]` |
| `sort()` | Sorts the list in ascending order by default. | `numbers = [3, 1, 2]`<br>`numbers.sort()` | `[1, 2, 3]` |
| `pop()` | Removes and returns an element, last element by default. | `numbers = [1, 2, 3]`<br>`numbers.pop()` | `3`<br>List becomes `[1, 2]` |
| `reverse()` | Reverses the order of elements in the list. | `numbers = [1, 2, 3]`<br>`numbers.reverse()` | `[3, 2, 1]` |

### Dict

| Function | Description | Example | Output |
|---|---|---|---|
| `get()` | Returns the value for a specified key without raising an error if the key is missing. | `student = {"name": "John"}`<br>`student.get("name")` | `"John"` |
| `keys()` | Returns all the keys in the dictionary. | `student = {"name": "John", "age": 20}`<br>`student.keys()` | `dict_keys(["name", "age"])` |
| `values()` | Returns all the values in the dictionary. | `student = {"name": "John", "age": 20}`<br>`student.values()` | `dict_values(["John", 20])` |
| `items()` | Returns key-value pairs as tuples. | `student = {"name": "John", "age": 20}`<br>`student.items()` | `dict_items([("name", "John"), ("age", 20)])` |
| `update()` | Adds new key-value pairs or updates existing keys. | `student = {"name": "John"}`<br>`student.update({"age": 20})` | `{"name": "John", "age": 20}` |
| `pop()` | Removes and returns the value associated with a specified key. | `student = {"name": "John", "age": 20}`<br>`student.pop("age")` | `20`<br>Dictionary becomes `{"name": "John"}` |

### String

| Function | Description | Example | Output |
|---|---|---|---|
| `split()` | Splits a string into a list using a separator. | `"hello world".split()` | `["hello", "world"]` |
| `join()` | Joins elements of an iterable into a string using a separator. | `" ".join(["hello", "world"])` | `"hello world"` |
| `replace()` | Replaces occurrences of one substring with another. | `"hello world".replace("world", "Python")` | `"hello Python"` |
| `strip()` | Removes whitespace from the beginning and end of a string. | `"  hello  ".strip()` | `"hello"` |
| `lower()` | Converts all characters in a string to lowercase. | `"HELLO".lower()` | `"hello"` |
| `upper()` | Converts all characters in a string to uppercase. | `"hello".upper()` | `"HELLO"` |

---

## 22. Remove Key-Value Pair

```python
student.pop("age")
```

or

```python
del student["age"]
```

---

## 23. zip()

Combines multiple iterables.

```python
names = ["A","B"]
ages = [20,21]

list(zip(names,ages))
```

Output

```
[('A',20), ('B',21)]
```

---

## 24. Difference Between 9/2 and 9//2

```
9/2  = 4.5

9//2 = 4
```

`/` returns float.

`//` returns floor division.

---

# Functions & Advanced Python

## 25. Decorators

Decorators modify function behavior without changing its code.

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print("Executing")
        return func(*args, **kwargs)

    return wrapper
```

### Real-world Usage

- Authentication
- Logging
- Caching
- Retry logic
- API monitoring
- Exception handling

---

## 26. Generators

Generators produce values lazily using `yield`.

```python
def numbers():

    for i in range(5):
        yield i
```

Benefits

- Memory efficient
- Faster for large datasets
- Lazy evaluation

Used while streaming large datasets and LLM outputs.

---

## 27. for-else

The `else` executes only if the loop completes without a `break`.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Completed")
```

---

## 28. Generator vs Iterator

| Generator | Iterator |
|------------|----------|
| Uses yield | Uses ```__iter__``` and ```__next__``` |
| Easier to write | Manual implementation |
| Memory efficient | Depends |

---

## 29. Serialization

Converting Python objects into a transferable format like JSON or Pickle.

Example

```python
import json

json.dumps(data)
```

Used for:
- REST APIs
- Model persistence
- Caching
- Message queues

---

## 30. Async IO

Async IO allows multiple I/O-bound tasks to run concurrently using a single thread.

```python
async def fetch():
    pass
```

### Where I Use It

- FastAPI
- Async database calls
- OpenAI APIs
- HTTP requests
- File operations

---

## 31. Multithreading vs Multiprocessing

| Multithreading | Multiprocessing |
|---------------|----------------|
| Shared memory | Separate memory |
| Best for I/O | Best for CPU |
| Affected by GIL | Not affected |

---

## 32. When to Use Async vs Threads vs Multiprocessing

- **Async IO:** API calls, DB queries, file operations.
- **Multithreading:** Concurrent I/O tasks such as downloading files or reading multiple files.
- **Multiprocessing:** CPU-intensive tasks like ML preprocessing, image processing, and model training.

---

## 33. What is GIL?

The Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time in CPython.

It limits true parallel execution for CPU-bound threads but does not significantly affect I/O-bound programs.

---

## 34. Memory Management

Python uses:

- Reference counting
- Garbage Collector (GC)

Unused objects are automatically cleaned up.

---

## 35. Exception Handling

```python
try:
    pass
except Exception as e:
    print(e)
finally:
    print("Cleanup")
```

Used to handle runtime errors gracefully.

---

## 36. Why Use `else` in Exception Handling?

The `else` block executes only if no exception occurs.

```python
try:
    print("Success")
except:
    print("Error")
else:
    print("Executed Successfully")
```

Useful for code that should run only when the `try` block succeeds.

---

# Data Structures / DSA

## 37. What is a Linked List?

A Linked List is a linear data structure where each node contains:

- Data
- Pointer to the next node

### Advantages

- Dynamic size
- Efficient insertions/deletions

### Disadvantages

- Sequential access
- Extra memory for pointers

---

## 38. Stack Class

```python
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def display(self):
        return self.items
```

---

## 39. Time Complexity of Stack Push

Using Python List:

```
Push : O(1)
Pop  : O(1)
```

---

# Coding Problems (Interview Solutions)

> **Note:** For interview questions, it's good to know both the **Pythonic solution** (using built-in libraries/functions) and the **Pure Python solution** (without relying on helper libraries). Interviewers often ask for the pure implementation to evaluate problem-solving skills.

---

## 40. Flatten Nested List

### Pythonic Solution (Recursion)

```python
def flatten(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

print(flatten([1, 2, [3, 4], [5, 6]]))
```

### Pure Python Solution (Without `extend()`)

```python
def flatten(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            nested = flatten(item)
            for value in nested:
                result.append(value)
        else:
            result.append(item)

    return result

print(flatten([1, 2, [3, 4], [5, 6]]))
```

---

## 41. Merge Overlapping Intervals

### Pythonic Solution

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)

    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))
```

### Pure Python Solution (Without `max()`)

```python
def merge(intervals):
    intervals.sort()
    result = [intervals[0]]

    for current in intervals[1:]:
        last = result[-1]

        if current[0] <= last[1]:
            if current[1] > last[1]:
                last[1] = current[1]
        else:
            result.append(current)

    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
```

---

## 42. Count Word Occurrences

### Pythonic Solution

```python
from collections import Counter

sentence = "python ai python"

print(Counter(sentence.split()))
```

### Pure Python Solution

```python
sentence = "python ai python"

words = sentence.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
```

---

## 43. Remove Vowels

### Pythonic Solution

```python
text = "Artificial Intelligence"

result = "".join(c for c in text if c.lower() not in "aeiou")

print(result)
```

### Pure Python Solution

```python
text = "Artificial Intelligence"

vowels = "aeiouAEIOU"

result = ""

for char in text:
    if char not in vowels:
        result += char

print(result)
```

---

## 44. Characters Appearing Only Once

### Pythonic Solution

```python
from collections import Counter

s = "abkkkb"

count = Counter(s)

result = "".join(c for c in s if count[c] == 1)

print(result)
```

### Pure Python Solution

```python
s = "abkkkb"

result = ""

for char in s:
    count = 0

    for item in s:
        if char == item:
            count += 1

    if count == 1:
        result += char

print(result)
```

---

## 45. Matrix Transpose

### Pythonic Solution

```python
matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = list(zip(*matrix))

print(transpose)
```

### Pure Python Solution

```python
matrix = [
    [1,2,3],
    [4,5,6]
]

rows = len(matrix)
cols = len(matrix[0])

transpose = []

for j in range(cols):
    row = []

    for i in range(rows):
        row.append(matrix[i][j])

    transpose.append(row)

print(transpose)
```

---

## 46. Sort List Without Using `set`

### Pythonic Solution

```python
nums = [4,2,1,5,3]

nums.sort()

print(nums)
```

### Pure Python Solution (Bubble Sort)

```python
nums = [4,2,1,5,3]

n = len(nums)

for i in range(n):

    for j in range(0, n-i-1):

        if nums[j] > nums[j+1]:

            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)
```

---

## 47. Check if URLs are Working

### Pythonic Solution (`requests`)

```python
import requests

urls = [
    "https://google.com",
    "https://example.com"
]

result = {}

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        result[url] = response.status_code == 200
    except requests.RequestException:
        result[url] = False

print(result)
```

### Pure Python Solution (`urllib`)

```python
from urllib.request import urlopen
from urllib.error import URLError

urls = [
    "https://google.com",
    "https://example.com"
]

result = {}

for url in urls:
    try:
        response = urlopen(url, timeout=5)
        result[url] = response.status == 200
    except URLError:
        result[url] = False

print(result)
```

> **Interview Tip:** If the interviewer says "without using any library", clarify whether standard library modules like `urllib` are allowed. If not, explain that checking a live URL requires network communication, which is typically handled by Python's standard networking libraries.

---

## 48. Check Whether an Integer Is a Palindrome Without Converting to a String

### Pythonic Solution

```python
def is_palindrome(num):
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num


print(is_palindrome(121))
print(is_palindrome(123))
print(is_palindrome(1221))
```
### Output

```
True
False
True
```

### how it works

We reverse the integer mathematically using `%` and `//` without converting it to a string.

For `121`:
```
121 % 10 = 1
12 % 10  = 2
1 % 10   = 1

Reversed number = 121
```

Finally, we compare the reversed number with the original number.

> **Interview Tip**: Mention that the solution uses O(log n) time and O(1) extra space, because we only use a few integer variables and do not create a string or additional data structure.

---
