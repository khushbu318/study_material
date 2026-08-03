# Backend & API Interview Questions

Importance: ⭐⭐⭐ = Asked 3+ times | ⭐⭐ = Asked 2 times | ⭐ = Asked once

---

## Framework Comparisons

| Question | Times Asked | Importance |
|----------|-------------|------------|
| Flask vs FastAPI vs Django | 2x (Q17, Q130) | ⭐⭐ |
| What is FastAPI | 1x (Q24) | ⭐ |
| What is the difference between Flask and FastAPI | 1x (Q17) | ⭐ |

---

## FastAPI Specifics

| Question | Times Asked | Importance |
|----------|-------------|------------|
| How do you define routes in FastAPI | 1x (Q145) | ⭐ |
| How to do login authentication in Flask / FastAPI | 1x (Q29) | ⭐ |
| What are tokens in API (Flask / FastAPI) | 1x (Q30) | ⭐ |

---

## Authentication & Security

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is SSO and have you used it | 1x (Q146) | ⭐ |
| What is session and cookies in React JS | 1x (Q140) | ⭐ |
| Can we transfer session data from one session to another | 1x (Q141) | ⭐ |
| What are tokens in API (auth context) | 1x (Q30) | ⭐ |

---

## Database Connectivity

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What technology is used to connect to a database in Python | 1x (Q34) | ⭐ |
| What is the use of `logging.py` and `handler.py` | 1x (Q43) | ⭐ |
| Have you used Alembic or write queries directly in large applications | 1x (Q149) | ⭐ |
| What is Redis and its use cases | 1x (Q157) | ⭐ |

---

## System Design & Architecture

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is system design | 1x (Q152) | ⭐ |
| What is a design pattern | 1x (Q153) | ⭐ |
| Stateful vs stateless servers | 1x (Q63) | ⭐ |
| What is serialization | 2x (Q33, Q106) | ⭐⭐ |

---

## Frontend (React / Angular)

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is React Hooks | 1x (Q11) | ⭐ |
| What is Angular lifecycle | 1x (Q12) | ⭐ |
| Do you know JavaScript | 1x (Q150) | ⭐ |

---
---
---
# Backend & API Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience developing scalable backend systems using Python, FastAPI, Flask, PostgreSQL, SQLAlchemy, Alembic, Redis, Docker, and cloud platforms. I have built REST APIs, authentication systems, RAG applications, AI agents, and production-ready AI services.

---

# Framework Comparisons

## 1. Flask vs FastAPI vs Django

| Flask | FastAPI | Django |
|--------|----------|---------|
| Lightweight microframework | Modern high-performance API framework | Full-stack web framework |
| Minimal features | Built for REST APIs | Comes with ORM, Admin Panel, Authentication |
| WSGI based | ASGI based | Primarily WSGI (ASGI supported) |
| Manual validation | Automatic validation using Pydantic | Django Forms & ORM |
| Good for small APIs | Best for AI APIs and microservices | Best for enterprise web applications |

### When I Use Them

**Flask**

- Small REST APIs
- Quick prototypes
- Internal tools

**FastAPI**

- AI applications
- RAG systems
- LLM APIs
- High-performance microservices
- Async applications

**Django**

- Enterprise applications
- Admin dashboards
- CMS
- E-commerce platforms

### Why I Prefer FastAPI

- Automatic Swagger Documentation
- Async support
- Type hints
- Faster performance
- Pydantic validation
- Easy dependency injection

---

## 2. What is FastAPI?

FastAPI is a modern Python web framework used for building high-performance REST APIs.

It is built on:

- Starlette
- Pydantic
- ASGI

### Features

- Async support
- Automatic API documentation
- Request validation
- Dependency Injection
- High performance
- Type safety

### Real-world Usage

I have used FastAPI for:

- AI Chatbots
- RAG Applications
- Authentication APIs
- LLM Services
- Resume Screening Systems
- PDF Chatbots

---

## 3. Difference Between Flask and FastAPI

| Flask | FastAPI |
|--------|----------|
| WSGI | ASGI |
| Synchronous by default | Supports async and sync |
| Manual validation | Automatic validation |
| Swagger requires extensions | Built-in Swagger UI |
| Slower | Faster |
| No type enforcement | Type hints supported |

---

# FastAPI Specifics

## 4. How Do You Define Routes in FastAPI?

Routes are created using decorators.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}

@app.post("/users")
def create_user():
    return {"status": "Created"}
```

### Common HTTP Methods

- GET
- POST
- PUT
- PATCH
- DELETE

---

## 5. How Do You Implement Login Authentication in FastAPI?

A typical authentication flow is:

1. User submits username and password.
2. Password is verified against the database.
3. Generate a JWT access token.
4. Return the token to the client.
5. Client sends the token in the `Authorization` header.
6. Protected APIs validate the token before processing the request.

### Example Header

```http
Authorization: Bearer <JWT_TOKEN>
```

### Libraries Used

- `python-jose`
- `passlib`
- `bcrypt`
- `OAuth2PasswordBearer`

---

## 6. What are Tokens in APIs?

A token is a secure credential issued after successful authentication.

It allows the client to access protected resources without sending the username and password on every request.

### Common Token Types

- JWT (JSON Web Token)
- OAuth Access Token
- Refresh Token

### JWT Structure

```
Header
.
Payload
.
Signature
```

### Benefits

- Stateless authentication
- Secure
- Scalable
- Suitable for microservices

---

# Authentication & Security

## 7. What is SSO? Have You Used It?

Single Sign-On (SSO) allows users to log in once and access multiple applications without authenticating again.

### Common Providers

- Google
- Microsoft Azure AD
- Okta
- Auth0
- Keycloak

### OAuth/OpenID Connect Flow

```
User
   │
Login
   │
Identity Provider
   │
Access Token
   │
Application
```

### Real-world Usage

I have integrated Google OAuth and Microsoft Azure AD authentication for secure access to AI applications.

---

## 8. What are Sessions and Cookies?

### Cookies

Cookies are small pieces of data stored in the browser and sent with each request.

Used for:

- Authentication
- User preferences
- Remember Me functionality

### Sessions

Sessions store user data on the server.

The browser stores only the Session ID in a cookie.

### Difference

| Cookies | Sessions |
|----------|-----------|
| Stored in browser | Stored on server |
| Limited size | Larger storage |
| Less secure | More secure |
| Sent with every request | Accessed using Session ID |

---

## 9. Can We Transfer Session Data from One Session to Another?

Directly transferring session data between two independent sessions is not recommended because each session has a unique identifier.

Instead, shared authentication is typically achieved using:

- JWT Tokens
- OAuth
- Redis-backed sessions
- Database persistence
- Secure cookies

---

# Database Connectivity

## 10. What Technology is Used to Connect to a Database in Python?

I commonly use:

- SQLAlchemy ORM
- SQLAlchemy Core
- Psycopg2 (PostgreSQL)
- PyMySQL
- SQLite3
- AsyncPG (for async PostgreSQL)

### Typical Stack

```
FastAPI
   │
SQLAlchemy
   │
PostgreSQL
```

---

## 11. What is the Use of `logging.py` and `handler.py`?

### `logging.py`

Responsible for configuring application logging.

Typical responsibilities:

- Log format
- Log level
- File handlers
- Console handlers
- Rotation policies

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

---

### `handler.py`

Typically contains request or business logic handlers.

Examples:

- API request handling
- Exception handling
- Service orchestration
- Background task processing

---

### Real-world Project Structure

```
app/
│
├── routers/
├── services/
├── models/
├── handlers/
├── utils/
├── logging.py
└── main.py
```

---

## 12. Have You Used Alembic or Do You Write Queries Directly?

Yes.

In production applications, I use **SQLAlchemy ORM** with **Alembic** for schema migrations.

### Alembic Advantages

- Version-controlled migrations
- Rollback support
- Team collaboration
- Automated migration generation

Example:

```bash
alembic revision --autogenerate -m "Create user table"

alembic upgrade head
```

### Raw SQL Usage

I use raw SQL for:

- Complex JOINs
- Window functions
- Reporting queries
- Bulk operations
- Performance-critical queries

---

## 13. What is Redis? What are Its Use Cases?

Redis is an in-memory key-value data store.

### Common Use Cases

- API caching
- Session storage
- Rate limiting
- Message queues
- Leaderboards
- Distributed locks

### Real-world Usage

I have used Redis for:

- Caching LLM responses
- Session management
- FastAPI rate limiting
- Temporary chat history
- Celery task queues

---

# System Design & Architecture

## 14. What is System Design?

System Design is the process of designing scalable, reliable, maintainable, and efficient software systems.

It focuses on:

- Scalability
- Performance
- Reliability
- Availability
- Security

### Example AI Architecture

```
Client
   │
FastAPI
   │
Authentication
   │
Business Logic
   │
Vector Database
   │
LLM
   │
Response
```

---

## 15. What is a Design Pattern?

A design pattern is a reusable solution to commonly occurring software design problems.

### Common Design Patterns

- Singleton
- Factory
- Strategy
- Observer
- Repository
- Dependency Injection

### Real-world Usage

I commonly use:

- Repository Pattern for database access
- Factory Pattern for selecting LLM providers
- Dependency Injection in FastAPI
- Strategy Pattern for choosing embedding models

---

## 16. Stateful vs Stateless Servers

| Stateful | Stateless |
|-----------|------------|
| Stores client state | Does not store client state |
| Session dependent | Independent requests |
| Harder to scale | Easier to scale |
| Suitable for long-lived interactions | Preferred for REST APIs |

### Example

**Stateful**

- Traditional web applications with server-side sessions

**Stateless**

- FastAPI REST APIs using JWT authentication

---

## 17. What is Serialization?

Serialization is the process of converting an object into a format that can be stored or transmitted.

Common formats:

- JSON
- XML
- Pickle
- Protocol Buffers

### Python Example

```python
import json

data = {
    "name": "John",
    "age": 30
}

json_string = json.dumps(data)
```

### Why Serialization?

- API communication
- File storage
- Caching
- Message queues
- Database storage

---

# Frontend (Basic Knowledge)

## 18. What are React Hooks?

React Hooks allow functional components to use state and lifecycle features.

Common hooks:

- useState
- useEffect
- useContext
- useRef
- useMemo
- useCallback

I have used them while integrating AI chatbots with FastAPI backends.

---

## 19. What is the Angular Lifecycle?

Angular components follow lifecycle hooks such as:

- ngOnChanges
- ngOnInit
- ngDoCheck
- ngAfterContentInit
- ngAfterViewInit
- ngOnDestroy

These hooks help initialize components, fetch data, detect changes, and clean up resources.

---

## 20. Do You Know JavaScript?

Yes.

Although my primary expertise is backend and AI engineering, I have experience using JavaScript for:

- React applications
- REST API integration
- AI dashboards
- Chatbot UIs
- File uploads
- Authentication flows
- WebSocket communication

Example:

```javascript
async function fetchData() {
    const response = await fetch("/api/chat");
    const data = await response.json();
    console.log(data);
}
```
