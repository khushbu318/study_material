# What is an API?

**API (Application Programming Interface)** is a mechanism that enables two software components—such as the **frontend** and **backend** of an application—to communicate with each other using a defined set of:

- Rules
- Protocols
- Data formats

![API Diagram](images_md\api_diagram.png)

---

# Need for APIs

## Problems with Monolithic Architecture

In a **monolithic architecture**, the frontend and backend are tightly coupled together.

This can create problems when an application needs to support multiple platforms, such as:

- Website
- Android application
- iOS application

Each platform may have a different frontend, but the **backend logic and data** can remain the same.

APIs solve this problem by providing a common interface through which different clients can communicate with the same backend.

### Example

```text
                 ┌──────────────┐
                 │   Website    │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │              │
                 │     API      │
                 │              │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │   Backend    │
                 └──────────────┘
                        ▲
                        │
          ┌─────────────┼─────────────┐
          │             │             │
     Android App     iOS App      Other Clients
```

## Decoupling of Frontend and Backend

One of the major advantages of API architecture is the **decoupling of the frontend and backend**.

This means:

- Frontend developers can work independently of backend developers.
- Multiple frontend applications can use the same backend.
- The backend can serve different types of clients.
- Changes to the frontend do not necessarily require changes to the backend.

---

# Data Format Used by APIs

A common data format used for API **requests and responses** is **JSON (JavaScript Object Notation)**.

For example:

```json
{
  "name": "John",
  "age": 25
}
```

JSON is useful because the **client can be written in any programming language**.

As long as the client understands the API contract and JSON format, it can communicate with the backend.

---

# API Communication Protocols

APIs can use different communication protocols and standards.

A very common approach for web APIs is:

- **HTTP / HTTPS**
- REST
- GraphQL
- gRPC

For example, a REST API commonly uses HTTP methods such as:

| Method | Purpose |
|---|---|
| `GET` | Retrieve data |
| `POST` | Create/send data |
| `PUT` | Update data |
| `PATCH` | Partially update data |
| `DELETE` | Delete data |

---

# API — Machine Learning Perspective

The concept of APIs becomes especially useful in **Machine Learning (ML)** applications.

Instead of the backend primarily interacting with a **database**, we can have an **ML model** as an important component of the backend.

```text
Client
   │
   │ Request
   ▼
 ┌─────────┐
 │   API   │
 └────┬────┘
      │
      ▼
 ┌─────────┐
 │ ML Model│
 └────┬────┘
      │
      ▼
   Response
```

> Example: ChatGPT
---
FastAPI

It is a modern, high-performance web framework from building APIs with python 

starlette
It managets how your API receives requests and sends back responses.

Pydantic
It is used to check if the data coming into your api is correct and in the right format

---

# Philosophy of FastAPI

FastAPI focuses on being **fast in two different ways**:

1. **Fast to run** — High performance when handling API requests.
2. **Fast to code** — Making APIs is quick and easy with less boilerplate code.

---

## 1. Fast to Run

FastAPI is designed to provide **high performance** when running APIs.

### Why is FastAPI Fast to Run?

To understand why FastAPI is fast, we first need to understand how **API code communicates with the web server**.

This communication happens through an interface between the **web server** and the **application code**.

---

## 2. How API Code and Web Server Communicate

The communication between the API application and the web server happens through a **Server Gateway Interface (SGI)**.

> **SGI (Server Gateway Interface)** acts as a bridge between the web server and the API/application code.

The basic flow can be understood as:

```text
Client
   ↓
Web Server
   ↓
SGI
   ↓
API / Application Code
   ↓
SGI
   ↓
Web Server
   ↓
Client
```

![web_sgi_api_communication](images_md/web_sgi_api_communication.png)


---
# Flask vs FastAPI — Comparison
> This will explain why FastApi is fast to RUN

| Feature | Flask | FastAPI |
|---|---|---|
| Framework | Flask | FastAPI |
| Common Server | Gunicorn | Uvicorn |
| Interface | **WSGI** — Web Server Gateway Interface | **ASGI** — Asynchronous Server Gateway Interface |
| Programming Model | Mainly synchronous | Supports synchronous and asynchronous |
| `async/await` | Limited/traditional synchronous model | First-class support |
| WebSockets | Requires additional setup | Supported through ASGI |
| Automatic API Docs | Not built-in | Built-in |
| Data Validation | Usually requires additional libraries | Pydantic-based |
| Performance | Good | Very high |
| Best Known For | Simplicity and flexibility | Modern, high-performance APIs |

---

## Full Forms

| Short Form | Full Form | Used With | Purpose |
|---|---|---|---|
| **WSGI** | **Web Server Gateway Interface** | Flask | Interface between a web server and a Python web application |
| **ASGI** | **Asynchronous Server Gateway Interface** | FastAPI | Interface between a web server and an asynchronous Python web application |
| **API** | **Application Programming Interface** | Flask / FastAPI | Allows applications to communicate with each other |
| **HTTP** | **Hypertext Transfer Protocol** | Web / APIs | Protocol used for communication between clients and servers |
| **REST** | **Representational State Transfer** | APIs | Architectural style commonly used for web APIs |
| **JSON** | **JavaScript Object Notation** | APIs | Lightweight format commonly used to exchange data |
| **URL** | **Uniform Resource Locator** | Web / APIs | Address used to locate a resource on the internet |
| **CRUD** | **Create, Read, Update, Delete** | APIs / Databases | Four basic operations performed on data |
| **I/O** | **Input/Output** | Python / APIs | Operations involving external resources such as databases, files, or networks |
| **OTP** | **One-Time Password** | Authentication | Temporary password used for authentication |
| **DB** | **Database** | APIs / Applications | System used to store and manage data |
| **SQL** | **Structured Query Language** | Databases | Language used to interact with relational databases |

---

## Important Servers

| Server | Full Name | Commonly Used With | Purpose |
|---|---|---|---|
| **Gunicorn** | **Green Unicorn** | Flask | Production WSGI HTTP server |
| **Uvicorn** | **Uvicorn** | FastAPI | High-performance ASGI server |

---

## Quick Memory Trick

```text
Flask
  ↓
Gunicorn
  ↓
WSGI
  ↓
Synchronous


FastAPI
  ↓
Uvicorn
  ↓
ASGI
  ↓
Asynchronous
```
![flask_vs_fastapi](images_md/flask_vs_fastapi.png)

---
# Why FastAPI is Fast to Code?

FastAPI is called **fast to code** because it makes creating APIs simple and requires less boilerplate code.

---

## HTTP Methods

To understand how FastAPI makes API development easy, we first need to understand **HTTP methods**.

HTTP methods define the type of operation we want to perform on a resource.

The commonly used HTTP methods are:

| HTTP Method | Purpose | CRUD Operation |
|---|---|---|
| **POST** | Create a new resource | **Create** |
| **GET** | Retrieve/read a resource | **Retrieve** |
| **PUT** | Update/replace a resource | **Update** |
| **PATCH** | Partially update a resource | **Update** |
| **DELETE** | Delete a resource | **Delete** |

---

## Static vs Dynamic Software

Software can broadly be understood as either **static** or **dynamic**.

### Static Software

Static software mainly displays information that does not change frequently based on user interaction.

Example:

```text
Website
   ↓
Displays
   ↓
Text + Images + Information
```

### Dynamic Software

Dynamic software **interacts with data** and can create, retrieve, update, or delete information.

For example, a **patient management system** may allow us to:

- Add a patient
- View patient details
- Update patient information
- Delete a patient

This is commonly handled using **CRUD operations**.

---

# CRUD Operations

**CRUD** stands for:

| CRUD Operation | Meaning | HTTP Method |
|---|---|---|
| **C — Create** | Create new data | `POST` |
| **R — Retrieve** | Retrieve/read existing data | `GET` |
| **U — Update** | Update existing data | `PUT` / `PATCH` |
| **D — Delete** | Delete existing data | `DELETE` |

# Path Parameters

**Path parameters** are dynamic segments of a URL path used to identify a specific resource.

## `Path()` Function in FastAPI

The `Path()` function in **FastAPI** is used to provide:

- Metadata
- Validation
- Rules/constraints
- Documentation hints

for **path parameters** in API endpoints.

| Parameter | Purpose | Example |
|---|---|---|
| `...` | Indicates that the parameter is **required** | `Path(...)` |
| `title` | Provides a short title for the parameter | `title="User ID"` |
| `description` | Provides additional information about the parameter | `description="Unique user ID"` |
| `ge` | **Greater than or equal to** | `ge=1` |
| `gt` | **Greater than** | `gt=0` |
| `le` | **Less than or equal to** | `le=100` |
| `lt` | **Less than** | `lt=100` |
| `min_length` | Sets the minimum length of a string | `min_length=3` |
| `max_length` | Sets the maximum length of a string | `max_length=20` |
| `regex` | Validates the value against a regular expression | `regex="^[a-zA-Z]+$"` |

For example:

```text
/users/101
```
> Here, `101` is a path parameter that identifies a specific user.



```python
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(
        ...,
        title="User ID",
        description="The unique ID of the user",
        ge=1,
        le=1000
    )
):
    return {"user_id": user_id}
```


---
# HTTP Status Codes

**HTTP status codes** are **3-digit numbers** returned by a web server (such as FastAPI) to indicate the result of a client's request.

The client can be:

- Browser
- Frontend application
- Mobile application
- API consumer

They help the client understand:

1. Whether the request was successful
2. Whether something went wrong
3. What kind of issue occurred, if any

---

## HTTP Status Code Categories

| Code | Meaning | Description |
|---|---|---|
| **2xx** | ✅ **Success** | The request was successfully received and processed. |
| **3xx** | 🔄 **Redirection** | The client needs to take additional action to complete the request. |
| **4xx** | ❌ **Client Error** | Something is wrong with the request sent by the client. |
| **5xx** | 💥 **Server Error** | The server encountered an error while processing a valid request. |

---

## 2xx — Success

**2xx status codes** indicate that the request was successfully received and processed.

| Code | Meaning | Description |
|---|---|---|
| **200** | ✅ **OK** | The request was successful. |
| **201** | ✅ **Created** | A new resource was successfully created. |
| **204** | ✅ **No Content** | The request was successful, but there is no response body to return. |

## 3xx — Redirection

**3xx status codes** indicate that the client needs to take additional action, usually by following a different URL.

| Code | Meaning | Description |
|---|---|---|
| **301** | 🔄 **Moved Permanently** | The requested resource has been permanently moved to a new URL. |
| **302** | 🔄 **Found** | The requested resource is temporarily available at a different URL. |
| **304** | 🔄 **Not Modified** | The resource has not changed since the client's last request, so the cached version can be used. |

---

## 4xx — Client Error

**4xx status codes** indicate that there is a problem with the request sent by the client.

| Code | Meaning | Description |
|---|---|---|
| **400** | ❌ **Bad Request** | The server cannot process the request because the request is invalid or malformed. |
| **401** | 🔐 **Unauthorized** | Authentication is required or the provided authentication credentials are invalid. |
| **403** | 🚫 **Forbidden** | The server understood the request but refuses to allow access to the resource. |
| **404** | 🔍 **Not Found** | The requested resource or endpoint could not be found. |
| **405** | 🚷 **Method Not Allowed** | The HTTP method used is not allowed for the requested resource. |
| **422** | ⚠️ **Unprocessable Content** | The request format is valid, but the provided data fails validation or cannot be processed. |
| **429** | 🛑 **Too Many Requests** | The client has sent too many requests within a given period, usually because of rate limiting. |

---

## 5xx — Server Error

**5xx status codes** indicate that the server encountered an error while processing the request.

| Code | Meaning | Description |
|---|---|---|
| **500** | 💥 **Internal Server Error** | The server encountered an unexpected error while processing the request. |
| **501** | 🚧 **Not Implemented** | The server does not support the functionality required to fulfill the request. |
| **502** | 🔌 **Bad Gateway** | A server acting as a gateway or proxy received an invalid response from an upstream server. |
| **503** | 🛠️ **Service Unavailable** | The server is temporarily unable to handle the request, often because of overload or maintenance. |
| **504** | ⏱️ **Gateway Timeout** | A gateway or proxy server did not receive a timely response from an upstream server. |

---

# HTTPException in Python and FastAPI

## What is `HTTPException`?

`HTTPException` is a **FastAPI exception** used to stop the normal execution of an API endpoint and return an appropriate **HTTP error response** to the client.

It is mainly used when something goes wrong while processing a request.

For example:

- User is not found
- User is not authorized
- Invalid request
- Resource does not exist
- User does not have permission

---

## Why Do We Use `HTTPException`?

When an error occurs in an API, we should return a meaningful **HTTP status code** and an explanation of what went wrong.

`HTTPException` allows us to specify:

1. **Status code** → What type of error occurred
2. **Detail** → A message explaining the error

### Basic Syntax

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```
| Status Code | Meaning | Example Use |
|---|---|---|
| `400` | **Bad Request** | Invalid request data |
| `401` | **Unauthorized** | User is not authenticated |
| `403` | **Forbidden** | User does not have permission |
| `404` | **Not Found** | Requested resource does not exist |
| `409` | **Conflict** | Resource already exists |
| `422` | **Unprocessable Content** | Validation-related error |
| `500` | **Internal Server Error** | Unexpected server-side error |

# `raise` vs `return`

A common mistake is to **return** an `HTTPException`.

❌ **Incorrect:**

```python
return HTTPException(
    status_code=404,
    detail="User not found"
)
```

✅ **Correct:**

```python
raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

## Why `raise`?

`raise` tells Python:

> "Stop executing this function because an error has occurred."

FastAPI catches the exception and converts it into the appropriate HTTP response.

### In One Line

> HTTPException is used in FastAPI to raise an HTTP error with a specific status code and a meaningful error message.

---
# Query Parameter

Query parameters are **optional key-value pairs** appended to the end of a URL. They are used to pass additional data to the server in an HTTP request.

They are typically used for operations such as:

- Filtering
- Sorting
- Searching
- Pagination

Query parameters allow us to pass additional information **without changing the endpoint path itself**.

### Example

```text
/patients?city=Delhi&sort_by=age
```
### How It Works

- `?` marks the **start of query parameters**.
- Each parameter is a **key-value pair** in the format:
  ```text
  key=value
  ```
- Multiple parameters are separated using `&`.

In the above example:

- `city=Delhi` → Query parameter used for **filtering**.
- `sort_by=age` → Query parameter used for **sorting**.

### FastAPI `Query()`

`Query()` is a utility function provided by **FastAPI** to declare, validate, and document query parameters in your API endpoints.

It allows you to:

- Set default values
- Enforce validation rules
- Add metadata like description, title, and examples

| Parameter | Purpose | Example |
|---|---|---|
| `None` | Makes the query parameter **optional** by providing `None` as the default value | `Query(None)` |
| `...` | Indicates that the query parameter is **required** | `Query(...)` |
| `default` | Specifies the default value when the query parameter is not provided | `Query("all")` |
| `title` | Provides a short title for the query parameter | `Query(..., title="Search Term")` |
| `description` | Provides additional information about the query parameter | `Query(..., description="Search by patient name")` |
| `gt` | **Greater than** | `Query(..., gt=0)` |
| `ge` | **Greater than or equal to** | `Query(..., ge=1)` |
| `lt` | **Less than** | `Query(..., lt=100)` |
| `le` | **Less than or equal to** | `Query(..., le=100)` |
| `min_length` | Sets the **minimum length** of a string query parameter | `Query(..., min_length=3)` |
| `max_length` | Sets the **maximum length** of a string query parameter | `Query(..., max_length=20)` |
| `pattern` | Validates a string query parameter against a **regular expression pattern** | `Query(..., pattern="^[a-zA-Z]+$")` |
| `alias` | Allows the query parameter to have a different name in the API than in the Python code | `Query(..., alias="search-term")` |
| `deprecated` | Marks the query parameter as **deprecated** in the generated API documentation | `Query(..., deprecated=True)` |
| `include_in_schema` | Controls whether the query parameter is included in the generated OpenAPI schema and API documentation | `Query(..., include_in_schema=False)` |
| `examples` | Provides example values for the query parameter in the generated API documentation | `Query(..., examples=["Delhi", "Mumbai"])` |
| `example` | Provides a single example value; **deprecated in newer FastAPI versions** in favor of `examples` | `Query(..., example="Delhi")` |

---

# Pydantic

Pydantic is a Python library used for **data validation and data parsing** using Python type hints.

It is widely used with **FastAPI** to validate request data and define the structure of data.

## Why Pydantic Is Needed

When an API receives data from a client, we need to make sure the data:

- Has the correct **data types**
- Contains the required fields
- Follows validation rules
- Has the expected structure
- Can be safely converted into the required Python types

Pydantic helps us do this automatically.

### Example Without Pydantic

```python
@app.post("/patient")
def create_patient(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
```

As the application becomes larger, manually validating every field can become difficult.

### Example With Pydantic

```python
from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    city: str


@app.post("/patient")
def create_patient(patient: Patient):
    return patient
```

Now Pydantic validates the incoming request body according to the `Patient` model.

> If the incoming data does not satisfy the model's validation requirements, FastAPI can return a validation error automatically.

---

# Advantages of Pydantic

| Advantage | Explanation |
|---|---|
| **Data Validation** | Automatically validates data according to the model definition and validation rules. |
| **Type Safety** | Uses Python type hints to define the expected data types. |
| **Less Boilerplate** | Reduces the need to write manual validation code. |
| **Data Parsing** | Can parse and convert compatible input data into the declared Python types. |
| **Nested Models** | Supports complex and nested data structures easily. |
| **FastAPI Integration** | FastAPI uses Pydantic extensively for request validation, response serialization, and API schema generation. |
| **Clear Data Models** | Makes the expected structure of data easy to understand from the model itself. |
| **Automatic Documentation** | Pydantic models used by FastAPI contribute to the generated OpenAPI/Swagger documentation. |
| **Custom Validation** | Supports custom validation logic when built-in validation rules are not enough. |

---

# Disadvantages of Pydantic

| Disadvantage | Explanation |
|---|---|
| **Additional Dependency** | Your project needs Pydantic as an external library. |
| **Validation Overhead** | Validation and parsing introduce some runtime overhead compared with using plain Python objects or dictionaries. |
| **Learning Curve** | Advanced features such as validators, nested models, aliases, serialization, and model configuration require additional learning. |
| **More Models to Maintain** | Large applications may require many Pydantic models, which can increase the amount of code that needs to be maintained. |
| **Type Conversion Can Be Unexpected** | Pydantic may convert compatible input values to the declared type, so developers need to understand its parsing/coercion behavior. |
| **Version Differences** | Code and APIs can differ between major versions, particularly between Pydantic v1 and v2. |

---

# Pydantic in FastAPI

A common FastAPI flow is:

```text
Client
  ↓
JSON Request
  ↓
FastAPI
  ↓
Pydantic Model
  ↓
Validation + Parsing
  ↓
API Function
  ↓
Response
```

### Interview One-Liner

> Pydantic is a Python library that uses type hints and validation rules to **validate**, **parse, and serialize structured data**. In **FastAPI**, it is commonly used to define and validate request and response data.

--- 
# Pydantic

## Definition

**Pydantic** is a Python library used for **data validation, parsing, and serialization** based on Python type hints.

In **FastAPI**, Pydantic is commonly used to:

- Define the structure of request and response data.
- Validate incoming data.
- Convert compatible input data into the declared Python types.
- Apply business-specific validation rules.
- Add metadata that can be used in API documentation.

---

# Pydantic Type Validation

Pydantic uses Python's **type hints** to understand what type of data is expected.

| Type | Used For | Example |
|---|---|---|
| `str` | Text/string values | `name: str` |
| `int` | Integer/whole numbers | `age: int` |
| `float` | Decimal numbers | `salary: float` |
| `bool` | Boolean values | `is_active: bool` |
| `list` | List of values | `skills: list` |
| `List` | List with a specific item type | `skills: List[str]` |
| `dict` | Dictionary/object | `address: dict` |
| `Dict` | Dictionary with specific key/value types | `scores: Dict[str, int]` |
| `tuple` | Fixed or ordered collection | `coordinates: tuple` |
| `Set` | Collection of unique values | `tags: set[str]` |
| `Optional` | Value can be a specific type or `None` | `phone: Optional[str]` |
| `Union` | Value can be one of multiple types | `value: Union[int, str]` |
| `Any` | Allows any type of value | `data: Any` |
| `Literal` | Restricts value to specific choices | `status: Literal["active", "inactive"]` |
| `Enum` | Defines a fixed set of named choices | `status: Status` |
| `datetime` | Date and time values | `created_at: datetime` |
| `date` | Date values | `dob: date` |

> **Note:** In modern Python, built-in generic types such as `list[str]` and `dict[str, int]` are generally preferred over `List[str]` and `Dict[str, int]`.

### Example

```python
from typing import Optional, List, Dict, Any

class Patient(BaseModel):
    name: str
    age: int
    skills: List[str]
    scores: Dict[str, int]
    phone: Optional[str] = None
    extra_data: Any
```
# Pydantic Data Validation

Type hints validate the **basic data type**, but sometimes the business requirement needs more specific validation.

For example:

| Requirement | Type Hint | Additional Validation |
|---|---|---|
| Patient name must be text | `str` | `min_length`, `max_length` |
| Patient age must be a number | `int` | `ge`, `le` |
| Email must be a valid email | `EmailStr` | Email format validation |
| Website must be a valid URL | `AnyUrl` | URL format validation |
| Age must be greater than 18 | `int` | `gt=18` |
| Username must have 3–20 characters | `str` | `min_length=3`, `max_length=20` |

# Pydantic Built-in Data Validation Types

Pydantic provides specialized types when normal Python types are not enough.

| Pydantic Type | Purpose | Example |
|---|---|---|
| `EmailStr` | Validates that a string contains a valid email address | `email: EmailStr` |
| `AnyUrl` | Validates that a value is a valid URL | `website: AnyUrl` |
| `AnyHttpUrl` | Validates HTTP/HTTPS URLs | `website: AnyHttpUrl` |
| `HttpUrl` | Validates HTTP/HTTPS URLs with additional URL constraints | `website: HttpUrl` |
| `IPvAnyAddress` | Validates an IPv4 or IPv6 address | `ip: IPvAnyAddress` |
| `IPvAnyInterface` | Validates an IPv4 or IPv6 interface | `interface: IPvAnyInterface` |
| `IPvAnyNetwork` | Validates an IPv4 or IPv6 network | `network: IPvAnyNetwork` |
| `PositiveInt` | Integer must be greater than `0` | `age: PositiveInt` |
| `NegativeInt` | Integer must be less than `0` | `value: NegativeInt` |
| `NonNegativeInt` | Integer must be greater than or equal to `0` | `count: NonNegativeInt` |
| `PositiveFloat` | Float must be greater than `0` | `price: PositiveFloat` |
| `NegativeFloat` | Float must be less than `0` | `temperature: NegativeFloat` |
| `StrictStr` | Requires an actual string instead of allowing certain conversions | `code: StrictStr` |
| `StrictInt` | Requires an actual integer instead of allowing certain conversions | `age: StrictInt` |
| `StrictFloat` | Requires an actual float | `price: StrictFloat` |
| `StrictBool` | Requires an actual boolean | `is_active: StrictBool` |

> **Note:** Some specialized types require additional dependencies. For example, `EmailStr` requires the `email-validator` package.

---

# `Field()` in Pydantic

`Field()` is used when **type hints alone are not enough** and we need additional validation rules or metadata.

It can be used to:

- Set default values.
- Apply validation constraints.
- Add descriptions.
- Add titles.
- Add examples.
- Provide metadata for API documentation.

### Basic Example
```python
from pydantic import BaseModel, Field


class Patient(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Patient's full name"
    )

    age: int = Field(
        ...,
        ge=0,
        le=120,
        description="Patient's age"
    )
```

# Common `Field()` Parameters

| Parameter | Purpose | Example |
|---|---|---|
| `default` | Specifies the default value | `Field("Unknown")` |
| `default_factory` | Generates the default value dynamically | `Field(default_factory=list)` |
| `title` | Provides a short title for the field | `Field(..., title="Patient Name")` |
| `description` | Provides additional information about the field | `Field(..., description="Full name of patient")` |
| `examples` | Provides example values for documentation | `Field(..., examples=["John Doe"])` |
| `gt` | Value must be **greater than** the specified value | `Field(..., gt=0)` |
| `ge` | Value must be **greater than or equal to** the specified value | `Field(..., ge=0)` |
| `lt` | Value must be **less than** the specified value | `Field(..., lt=100)` |
| `le` | Value must be **less than or equal to** the specified value | `Field(..., le=100)` |
| `multiple_of` | Value must be a multiple of the specified number | `Field(..., multiple_of=5)` |
| `min_length` | Sets the minimum length of a string or collection | `Field(..., min_length=3)` |
| `max_length` | Sets the maximum length of a string or collection | `Field(..., max_length=50)` |
| `pattern` | Validates a string against a regular expression pattern | `Field(..., pattern=r"^[A-Za-z]+$")` |
| `strict` | Enables strict validation for the field | `Field(..., strict=True)` |
| `frozen` | Prevents the field from being changed after model creation | `Field(..., frozen=True)` |
| `exclude` | Controls whether the field is excluded during serialization | `Field(..., exclude=True)` |
| `deprecated` | Marks the field as deprecated in generated schema/documentation | `Field(..., deprecated=True)` |
| `repr` | Controls whether the field is included in the model's representation | `Field(..., repr=False)` |
| `alias` | Specifies an alternative name for the field | `Field(..., alias="patientName")` |

### `...` in `Field()`

> `...` represents a required field when used as the default value.

```python
class Patient(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
```
This means:
```
name → required
age  → required
```
> A request without these fields will fail validation.

### `Annotated` + `Field()`

`Annotated` allows us to attach metadata and validation information to a type annotation.

```python
from typing import Annotated
from pydantic import BaseModel, Field


class Patient(BaseModel):
    age: Annotated[
        int,
        Field(
            ge=18,
            le=100,
            description="Patient age must be between 18 and 100"
        )
    ]
```

# `Field()` vs `Annotated`

| Approach | Example | Purpose |
|---|---|---|
| Direct `Field()` | `age: int = Field(..., ge=18)` | Defines the field and its constraints together |
| `Annotated` + `Field()` | `age: Annotated[int, Field(ge=18)]` | Attaches constraints/metadata to the type annotation |
| Plain type | `age: int` | Only specifies the expected type |

### When to Use

| Requirement | Recommended |
|---|---|
| Only need the data type | `age: int` |
| Need a default value | `age: int = 18` |
| Need validation constraints | `age: int = Field(..., ge=18)` |
| Need reusable/annotated type metadata | `Annotated[int, Field(...)]` |
| Need descriptions and documentation metadata | `Field(..., description="...")` or `Annotated[..., Field(...)]` |

---

# Pydantic Validation Levels

It is useful to think about Pydantic validation in layers:

| Level | Example | What It Checks |
|---|---|---|
| **1. Basic Type Validation** | `age: int` | Is the value compatible with the expected type? |
| **2. Specialized Type Validation** | `email: EmailStr` | Does the value satisfy a specific format/type requirement? |
| **3. Field Constraints** | `age: int = Field(..., ge=18)` | Does the value satisfy business constraints? |
| **4. Custom Validation** | `@field_validator` | Does the value satisfy custom business logic? |

---

# Custom Business Validation

Sometimes built-in types and `Field()` constraints are not enough.

For example:

> A patient's age must be at least 18, and the email domain must be from a specific company.

For such requirements, Pydantic provides validators.

```python
from pydantic import BaseModel, EmailStr, field_validator


class Employee(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if not value.endswith("@company.com"):
            raise ValueError("Email must belong to company.com")

        return value
```

### When to Use What?

| Requirement | Use |
|---|---|
| Expected type is `int`, `str`, `bool`, etc. | Python type hints |
| Valid email address | `EmailStr` |
| Valid URL | `AnyUrl`, `HttpUrl`, etc. |
| Minimum/maximum value | `Field(ge=..., le=...)` |
| Minimum/maximum string length | `Field(min_length=..., max_length=...)` |
| Regex/pattern validation | `Field(pattern=...)` |
| Custom business rule | `@field_validator` |
| API documentation metadata | `Field()` + `Annotated` |

---

# Interview Summary

> **Pydantic is used to validate, parse, and serialize structured data using Python type hints. Basic types such as `str`, `int`, `List`, `Dict`, and `Optional` define the expected data type. Specialized Pydantic types such as `EmailStr` and `AnyUrl` provide additional format validation. When business-specific constraints are required, we can use `Field()` for constraints such as `gt`, `ge`, `lt`, `le`, `min_length`, and `max_length`. `Field()` and `Annotated` can also be used to attach metadata such as descriptions, titles, and examples for API documentation. For complex business rules, Pydantic validators such as `@field_validator` can be used.**


---
# Pydantic `field_validator`

`field_validator` is used to create **custom field-level validation logic** in Pydantic.

It is useful when the built-in Pydantic types and `Field()` constraints are not enough to implement a specific **business rule**.

### Import

```python
from pydantic import BaseModel, field_validator
```

### Why Use `field_validator`?

We use `@field_validator` when we need to define custom validation logic according to our business requirements.

For example:

- Check whether a username follows a specific rule.
- Validate that an email belongs to a particular domain.
- Ensure a value follows a custom format.
- Apply business-specific validation that cannot be expressed using Field().

### `@field_validator` Decorator

We use the `@field_validator` decorator above the validation method.

```python
from pydantic import BaseModel, field_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("Username must contain at least 3 characters")

        return value
```
Here:

| Part | Purpose |
|---|---|
| `@field_validator("username")` | Tells Pydantic to validate the `username` field using this method |
| `@classmethod` | Makes the validator a class method |
| `cls` | Refers to the Pydantic model class |
| `value` | Contains the value of the field being validated |
| `raise ValueError(...)` | Indicates that validation has failed |
| `return value` | Returns the validated value |

> **Note:** In Pydantic v2, `@field_validator` methods are commonly written with `@classmethod`. Pydantic can also recognize the method as a class method based on the decorator usage, but explicitly using `@classmethod` is clear and recommended in examples.

---

# Modes of `field_validator`

`field_validator` supports two commonly used modes:

| Mode | When It Runs | Use When |
|---|---|---|
| `after` | **After** Pydantic has validated/coerced the value into the declared type | You want to work with the already validated/converted value |
| `before` | **Before** Pydantic performs type validation/coercion | You need to inspect, clean, normalize, or transform the raw input first |

---

# `before` vs `after`

| Feature | `before` | `after` |
|---|---|---|
| Runs | Before Pydantic type validation/coercion | After Pydantic type validation/coercion |
| Receives | Raw input | Validated/parsed value |
| Default Mode | No | **Yes — `after` is the default mode** |
| Best for | Cleaning, normalization, preprocessing | Business rules and final validation |
| Type of value | May be any input type | Usually the declared/validated type |
| Example | Convert `"  John  "` → `"John"` | Check `age >= 18` |

---

### Interview Answer

> **`field_validator` in Pydantic is used to implement custom field-level validation according to business requirements. It supports `before` and `after` modes. `before` runs before Pydantic's normal type validation and coercion, so it is useful for preprocessing or transforming raw input. `after` runs after type validation/coercion, so it is useful for validating the already parsed value and applying business rules. The default mode is `after`.**

---
# Pydantic `model_validator`

`model_validator` is used when we need to validate or process **multiple fields together** at the model level.

While `field_validator` is used to validate a **specific field**, `model_validator` is useful when the validation depends on **two or more fields**.

### Why Use `model_validator`?

We can use `@model_validator` when:

- Validation depends on multiple fields.
- We need to compare two or more fields.
- We need to enforce a business rule involving multiple fields.
- We need to validate the complete model together.

### Example

Suppose we have:

- `password`
- `confirm_password`

We want to make sure both values are the same.

```python
from pydantic import BaseModel, model_validator


class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self
```
Here:

| Part | Purpose |
|---|---|
| `@model_validator` | Tells Pydantic that this is a model-level validator |
| `mode="after"` | Runs the validator after the model's fields have been validated |
| `self` | Represents the complete model instance |
| `self.password` | Accesses the `password` field |
| `self.confirm_password` | Accesses the `confirm_password` field |
| `raise ValueError(...)` | Indicates that model validation has failed |
| `return self` | Returns the validated model instance |

---

# `field_validator` vs `model_validator`

| Validator | Used For | Example |
|---|---|---|
| `@field_validator` | Validation of a **specific field** | Check whether `age >= 18` |
| `@model_validator` | Validation involving **multiple fields or the entire model** | Check whether `password == confirm_password` |

---

# Interview Answer

> **`model_validator` in Pydantic is used for model-level validation when a validation rule depends on multiple fields or the complete model. It is defined using the `@model_validator` decorator and can be used to compare or validate multiple fields together according to business requirements.**


---
# Pydantic `computed_field`

A **computed field** is a field whose value is **calculated dynamically from other fields** in the Pydantic model instead of being provided directly as input.

### `@computed_field` + `@property`

- `@computed_field` is used to include the calculated value in the Pydantic model's serialization/schema.
- `@property` is used to define the logic for calculating the value.
- The **function name becomes the computed field name**.

### Example

```python
from pydantic import BaseModel, computed_field


class Rectangle(BaseModel):
    length: float
    width: float

    @computed_field
    @property
    def area(self) -> float:
        return self.length * self.width
```

Here:

| Part | Purpose |
|---|---|
| `@computed_field` | Marks the property as a Pydantic computed field |
| `@property` | Allows the method to be accessed like an attribute |
| `area` | Becomes the **computed field name** |
| `self.length` | Gets the `length` value from the model |
| `self.width` | Gets the `width` value from the model |
| `return self.length * self.width` | Calculates the computed value |

---
### Usage
```python
rectangle = Rectangle(length=10, width=5)

print(rectangle.area)
```

Output:
```
50.0
```
The `area` value does not need to be provided when creating the model:
```python
Rectangle(
    length=10,
    width=5
)
```
Pydantic calculates it when `area` is accessed.

# Interview Answer

> **`computed_field` in Pydantic is used to include a calculated property as a field in the model's serialization and schema. It is commonly used together with `@property`, where the function contains the calculation logic and the function name becomes the computed field name.**
---
# Nested Models in Pydantic

**Nested models** are Pydantic models used inside other Pydantic models to represent **related or hierarchical data structures**.

They are useful for:

- **Better Organization** — Keep related data grouped into separate models.
- **Reusability** — The same Pydantic model can be reused in multiple models.
- **Readability** — Makes complex data structures easier to understand and maintain.
- **Validation** — Pydantic validates the fields inside nested models as well.

### Example

```python
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pincode: int


class Patient(BaseModel):
    name: str
    age: int
    address: Address

```
Here, `Address` is a nested model inside the `Patient` model.

Input Example:
```python
{
    "name": "Rahul",
    "age": 25,
    "address": {
        "city": "Delhi",
        "state": "Delhi",
        "pincode": 110001
    }
}
```
### Benefits of Nested Models

| Benefit | Explanation |
|---|---|
| **Better Organization** | Groups related fields into their own model. |
| **Reusability** | The same model can be used in multiple Pydantic models. |
| **Readability** | Makes complex request/response structures easier to understand. |
| **Validation** | Validates nested fields according to the nested model's rules. |

---

# Interview Answer

> **Nested models in Pydantic allow us to use one Pydantic model inside another model. They help organize related data, improve reusability and readability, and provide validation for nested data structures.**

---
# Serialization Using Pydantic

**Serialization** means converting a Pydantic model into a format that can be easily stored, transmitted, or returned by an API.

Pydantic provides methods such as:

| Method | Purpose | Output |
|---|---|---|
| `model_dump()` | Converts a Pydantic model into a Python dictionary | `dict` |
| `model_dump_json()` | Converts a Pydantic model into a JSON string | `str` |

> **Note:** `model_dump()` and `model_dump_json()` are the recommended Pydantic v2 methods. In Pydantic v1, the equivalent methods were `dict()` and `json()`.

---

# `model_dump()`

`model_dump()` converts a Pydantic model into a **Python dictionary**.

### Example

```python
from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    city: str


patient = Patient(
    name="Rahul",
    age=25,
    city="Delhi"
)

data = patient.model_dump()

print(data)
```
Output:
```
{
    'name': 'Rahul',
    'age': 25,
    'city': 'Delhi'
}
```
# Common `model_dump()` Parameters

| Parameter | Purpose | Example |
|---|---|---|
| `include` | Specifies which fields should be included in the output | `model_dump(include={"name", "age"})` |
| `exclude` | Specifies which fields should be excluded from the output | `model_dump(exclude={"city"})` |
| `exclude_unset` | Excludes fields that were not explicitly provided when the model was created. `Include fields provided during model creation` | `model_dump(exclude_unset=True)` |
| `exclude_defaults` | Excludes fields whose value is equal to their default value | `model_dump

### `model_dump_json()`

`model_dump_json()` serializes a Pydantic model into a JSON string.

Example
```python
patient = Patient(
    name="Rahul",
    age=25,
    city="Delhi"
)

data = patient.model_dump_json()

print(data)
```

Output:
```json
{"name":"Rahul","age":25,"city":"Delhi"}
```
### `model_dump()` vs `model_dump_json()`

| Method | Returns | Example Output |
|---|---|---|
| `model_dump()` | Python `dict` | `{'name': 'Rahul', 'age': 25}` |
| `model_dump_json()` | JSON `str` | `'{"name":"Rahul","age":25}'` |

---

# `model_dump_json()` with Parameters

Many serialization options available in `model_dump()` can also be used with `model_dump_json()`.

---

# Interview Summary

| Method / Parameter | Key Point |
|---|---|
| `model_dump()` | Converts a Pydantic model into a Python dictionary |
| `model_dump_json()` | Converts a Pydantic model into a JSON string |
| `include` | Selects which fields to include |
| `exclude` | Selects which fields to exclude |
| `exclude_unset=True` | Excludes fields that were not explicitly provided |
| `exclude_defaults=True` | Excludes fields that have their default values |
| `exclude_none=True` | Excludes fields whose value is `None` |
| `by_alias=True` | Uses field aliases in the serialized output |

> **Interview Answer:**
>
> **Pydantic provides `model_dump()` to serialize a model into a Python dictionary and `model_dump_json()` to serialize it into a JSON string. `model_dump()` supports options such as `include` to select fields, `exclude` to remove fields, and `exclude_unset=True` to exclude fields that were not explicitly provided when creating the model.**

---
# FastAPI + Pydantic — Patient API Notes

## 1. Pydantic Models

- `BaseModel` is used to define data models and validate incoming data.
- `Field()` provides metadata, descriptions, examples, and validation constraints.
- `Annotated` combines a type with `Field()` metadata.
- Pydantic supports nested models, allowing structured objects such as `Patient` containing `Address`.

## 2. Important Pydantic Field Types

- `str` → text values.
- `int` → integer values.
- `bool` → true/false values.
- `date` → validates and converts date values.
- `EmailStr` → validates email format.
- `List[T]` → list containing values of type `T`.
- `Optional[T]` → allows the value to be `None`.
- `Literal[...]` → restricts a field to predefined values.

## 3. Field Validation

`Field()` can enforce constraints such as:

- `gt` → greater than
- `ge` → greater than or equal to
- `lt` → less than
- `le` → less than or equal to
- `min_length` → minimum string length
- `max_length` → maximum string length

Pydantic automatically validates incoming request data against these rules.

## 4. Computed Fields

`@computed_field` is used when a value should be calculated from other model fields rather than provided by the client.

Example use case:

- Height + weight → BMI
- The client sends height and weight.
- The application calculates BMI automatically.

### BMI Formula

```text
BMI = weight (kg) / height (m)²
```
## 5. Request Body in POST Endpoints

Pydantic models are commonly used as the **request body model** in POST endpoints.

| Benefit | Description |
|---|---|
| Automatic validation | Validates incoming data against the model |
| Type conversion | Converts compatible input into the expected Python types |
| Clear API schema | Defines the expected request structure |
| Swagger/OpenAPI documentation | Automatically generates request schema in API docs |
| Data protection | Prevents invalid data from reaching business logic |

If the request body does not match the Pydantic model, FastAPI returns a validation error, commonly with HTTP `422`.

## 6. JSONResponse

`JSONResponse` is used when you need explicit control over the HTTP response.

| Can control | Description |
|---|---|
| Response content | JSON data returned to the client |
| HTTP status code | e.g. `200`, `201`, `400`, `404` |
| Response headers | Custom HTTP response headers |

For example, after successfully creating a patient, returning HTTP `201 Created` indicates that a new resource was successfully created.

## 7. Pydantic Serialization

| Method | Purpose |
|---|---|
| `model_dump()` | Converts a Pydantic model into a Python dictionary |
| `model_dump(mode="json")` | Converts the model into a JSON-compatible dictionary |

`model_dump(mode="json")` is especially useful when the model contains Python-specific types such as `date`.

## 8. Common Errors

| Error | Meaning | Solution |
|---|---|---|
| `json_invalid → Extra data` | Request JSON is malformed, e.g. multiple JSON objects | Send one valid JSON object |
| `422 Validation Error` | JSON is valid but doesn't match the Pydantic model | Check field types and validation rules |
| `Object of type date is not JSON serializable` | Python `date` object passed directly to `json.dump()` | Use JSON-compatible serialization |
| `data.keys` Error | `keys` is used as a method without calling it | Use `data.keys()` or simply `key in data` |

## 9. Interview Takeaways

| Concept | Key Point |
|---|---|
| `BaseModel` | Defines and validates data |
| `Field` | Adds metadata and validation constraints |
| `Annotated` | Combines type and metadata |
| `Literal` | Restricts values to predefined options |
| `Optional` | Allows `None` |
| Nested models | Represent structured/related data |
| `computed_field` | Calculates derived values |
| Request body | Carries client data, especially for POST/create operations |
| `model_dump()` | Converts Pydantic model to Python dictionary |
| `model_dump(mode="json")` | Creates JSON-compatible data |
| `JSONResponse` | Provides explicit control over response content and status code |
| FastAPI + Pydantic | Provides automatic request validation and API documentation |

---

serving ml models via fastapi

model_api.py will help to undersand

---
FastAPI + sql integration

