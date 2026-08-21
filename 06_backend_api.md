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
# Backend & API Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience developing scalable backend systems using Python, FastAPI, Flask, PostgreSQL, SQLAlchemy, Alembic, Redis, Docker, and cloud platforms. I have built REST APIs, authentication systems, RAG applications, AI agents, and production-ready AI services.

---

# Framework Comparisons

---

## Q1. Flask vs FastAPI vs Django

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

## Q2. What is FastAPI?

FastAPI is a modern Python web framework used for building high-performance REST APIs.

  - A modern Python web framework for building APIs.
  - Built on **Starlette** for web functionality and **Pydantic** for data validation.
  - Supports `async`/`await`, dependency injection, automatic OpenAPI documentation, and type hints.
  - Commonly used for REST APIs, microservices, ML/AI APIs, and high-concurrency applications.


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

## Q3. Difference Between Flask and FastAPI

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

---

## Q4. How Do You Define Routes in FastAPI?

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

## Q5. How Do You Implement Login Authentication in FastAPI?

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

## Q6. What are Tokens in APIs?

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
## Q7. How does FastAPI handle request validation?
  - FastAPI uses Python type hints and Pydantic models.
  - Request data is automatically parsed and validated.
  - Invalid input normally results in a `422 Unprocessable Entity` response.
  - Example:
    ```python
    from pydantic import BaseModel

    class User(BaseModel):
        name: str
        age: int

    @app.post("/users")
    async def create_user(user: User):
        return user
    ```
---
## Q8. What is Pydantic and how is it used in FastAPI?
  - Pydantic is a Python library for data validation and serialization.
  - FastAPI uses Pydantic models for:
    - Request bodies.
    - Response models.
    - Configuration/settings.
    - Nested data validation.
  - It converts validated input into Python objects.

---
## Q9. How do you handle exceptions in FastAPI?
  - Use `HTTPException` for normal API errors.
  - Use custom exception handlers for application-specific errors.
  - Example:
    ```python
    from fastapi import HTTPException

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    ```
  - Global handlers can standardize error responses.

  ---
## Q10. How do you implement middleware in FastAPI?
  - Middleware runs before and/or after request processing.
  - Common uses:
    - Logging.
    - Request IDs.
    - CORS.
    - Authentication-related processing.
    - Metrics.
  - Example:
    ```python
    @app.middleware("http")
    async def log_requests(request, call_next):
        response = await call_next(request)
        return response
    ```
---
## Q11. How do you handle dependency injection in FastAPI?
  - FastAPI provides dependency injection using `Depends`.
  - Dependencies can provide:
    - Database sessions.
    - Current users.
    - Authentication checks.
    - Configuration.
    - Common business services.
  - Example:
    ```python
    @app.get("/users")
    async def users(db = Depends(get_db)):
        return db.query(User).all()
    ```
---
## Q12. How do you structure a production FastAPI project?
  - A common structure:
    ```text
    app/
    ├── main.py
    ├── api/
    │   ├── routes/
    │   └── dependencies.py
    ├── models/
    ├── schemas/
    ├── services/
    ├── repositories/
    ├── core/
    │   ├── config.py
    │   └── security.py
    ├── db/
    └── tests/
    ```
  - Keep HTTP routes thin.
  - Put business logic in services.
  - Put database-specific logic in repositories where appropriate.
  - Keep configuration and security concerns separate.
---
## Q13. How do you handle background tasks?
  - FastAPI provides `BackgroundTasks` for lightweight tasks after returning a response.
  - Suitable for:
    - Sending simple notifications.
    - Logging.
    - Small asynchronous operations.
  - For heavy or long-running jobs, use a task queue such as Celery, RQ, or another distributed worker system.
---

## Q14. How do you implement pagination?
  - Accept parameters such as:
    ```text
    page
    page_size
    ```
    or:
    ```text
    limit
    offset
    ```
  - Apply them to the database query.
  - Return metadata such as:
    ```json
    {
      "items": [],
      "page": 1,
      "page_size": 20,
      "total": 100
    }
    ```
  - For very large datasets, cursor/keyset pagination is often better than large offsets.
---
## Q15. How do you handle file uploads?
  - Use `UploadFile` and `File`.
  - Example:
    ```python
    @app.post("/upload")
    async def upload_file(file: UploadFile):
        content = await file.read()
        return {"filename": file.filename}
    ```
  - Validate:
    - File size.
    - MIME type.
    - Extension.
    - File content where necessary.
  - For large files, prefer streaming/object storage rather than keeping the entire file in memory.

---

## Q16. How do you implement API versioning?
  - Common approach:
    ```text
    /api/v1/users
    /api/v2/users
    ```
  - Alternatively use headers or separate domains, but URL versioning is straightforward.
  - Keep old versions available during a migration period.
  - Clearly document breaking changes.
---
## Q17. How do you write tests for FastAPI APIs?
  - Use `pytest`.
  - FastAPI provides `TestClient` for API testing.
  - Test:
    - Successful requests.
    - Validation failures.
    - Authentication.
    - Authorization.
    - Database interactions.
    - Error handling.
  - Mock external services rather than calling real third-party APIs in unit tests.
---
# Authentication & Security

---

## Q18. What is SSO? Have You Used It?

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

## Q19. What are Sessions and Cookies?

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

## Q20. Can We Transfer Session Data from One Session to Another?

Directly transferring session data between two independent sessions is not recommended because each session has a unique identifier.

Instead, shared authentication is typically achieved using:

- JWT Tokens
- OAuth
- Redis-backed sessions
- Database persistence
- Secure cookies

---
## Q21. How do you implement authentication and authorization?
  - Authentication answers: **Who are you?**
  - Authorization answers: **What are you allowed to do?**
  - Common authentication approaches:
    - OAuth2.
    - JWT access tokens.
    - Session-based authentication.
    - API keys for service-to-service use.
  - FastAPI provides security utilities that integrate with its dependency injection system.
  - Store passwords using a strong password-hashing algorithm such as Argon2 or bcrypt.
  - Never store plaintext passwords.

---

## Q22. How would you implement RBAC in FastAPI?
  - RBAC = Role-Based Access Control.
  - Example roles:
    ```text
    admin
    manager
    user
    ```
  - Store roles/permissions with the user.
  - Authenticate the user first.
  - Add an authorization dependency:
    ```python
    def require_admin(current_user = Depends(get_current_user)):
        if current_user.role != "admin":
            raise HTTPException(status_code=403)
        return current_user
    ```
  - For larger systems, prefer permission-based checks such as:
    ```text
    users:read
    users:create
    users:delete
    ```

---

## Q23. How do you secure FastAPI APIs?
  - Use HTTPS.
  - Validate all input.
  - Use strong authentication.
  - Implement authorization on every protected resource.
  - Hash passwords securely.
  - Protect secrets using environment variables or a secret manager.
  - Implement rate limiting.
  - Configure CORS carefully.
  - Limit file upload sizes and validate uploaded content.
  - Prevent SQL injection through parameterized queries/ORMs.
  - Avoid exposing sensitive information in error messages.
  - Keep dependencies patched.
  - Add logging, monitoring, and security auditing.

---


# Database Connectivity

---

## Q24. What Technology is Used to Connect to a Database in Python?

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

## Q25. What is the Use of `logging.py` and `handler.py`?

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

## Q26. Have You Used Alembic or Do You Write Queries Directly?

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

## Q27. What is Redis? What are Its Use Cases?

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
## Q28. How do you connect FastAPI with a database?
  - Common options include:
    - SQLAlchemy.
    - SQLModel.
    - Async SQLAlchemy.
    - Databases or other database-specific libraries.
  - Create a database engine.
  - Configure connection pooling.
  - Create a session dependency.
  - Inject the session into routes/services.
  - Example concept:
    ```python
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    ```

---

## Q29. How do you handle database connection pooling?
  - Use the connection pool provided by your database driver/ORM.
  - Configure:
    - Pool size.
    - Maximum overflow.
    - Connection timeout.
    - Connection recycling.
  - Avoid creating a brand-new database connection for every query.
  - Ensure connections are returned to the pool after requests.
  - For multiple application instances, remember that each instance can have its own pool, so total database connections can grow quickly.
  - Monitor database connection utilization.

---

# System Design & Architecture

---

## Q30. What is System Design?

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

## Q31. What is a Design Pattern?

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

## Q32. Stateful vs Stateless Servers

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

## Q33. What is Serialization?

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
## Q34. An API is responding slowly. How would you identify the bottleneck?
  - First measure rather than guessing.
  - Check:
    - Request latency.
    - CPU and memory.
    - Database query duration.
    - External API latency.
    - Network latency.
    - Lock contention.
    - Connection pool exhaustion.
  - Add structured logging and distributed tracing.
  - Profile slow endpoints.
  - Inspect database query plans.
  - Look for:
    - N+1 queries.
    - Missing indexes.
    - Large payloads.
    - Synchronous blocking operations inside async endpoints.
    - Slow third-party APIs.
  - Fix the actual bottleneck before scaling blindly.

---

## Q35. An API suddenly receives a large number of requests. How would you scale it?
  - First determine whether the traffic is legitimate or abusive.
  - Add:
    - Load balancing.
    - Multiple application instances.
    - Horizontal autoscaling.
    - Rate limiting.
    - Caching.
    - Database connection pooling.
  - Move expensive work to asynchronous workers.
  - Use a CDN for suitable static/cacheable content.
  - Monitor CPU, memory, latency, error rate, database load, and queue depth.
  - If traffic is extremely high, introduce queues and backpressure rather than allowing every request to hit the database simultaneously.

---

## Q36. How would you implement rate limiting?
  - Define limits such as:
    ```text
    100 requests/minute/user
    20 requests/minute/IP
    ```
  - For multiple API instances, use a shared store such as Redis.
  - Common algorithms:
    - Token bucket.
    - Leaky bucket.
    - Fixed window.
    - Sliding window.
  - Return HTTP `429 Too Many Requests` when the limit is exceeded.
  - Consider separate limits for expensive endpoints.

---

## Q37. How would you implement caching for an API?
  - Identify frequently requested and relatively stable data.
  - Use:
    - Redis.
    - In-memory cache for small single-instance workloads.
    - HTTP caching/CDN where appropriate.
  - Example:
    ```text
    Request
       ↓
    Cache lookup
       ↓
    Cache hit → return data
       ↓
    Cache miss
       ↓
    Database
       ↓
    Store in cache
       ↓
    Return response
    ```
  - Define:
    - TTL.
    - Cache keys.
    - Invalidation strategy.
  - Be careful with stale or user-specific data.

---

## Q38. How would you design an API for a large-scale application?
  - Start with clear resource boundaries and REST/gRPC requirements.
  - Use stateless API servers where possible.
  - Put a load balancer/API gateway in front.
  - Use horizontal scaling.
  - Separate application, database, cache, and background workers.
  - Use database indexes and appropriate read/write strategies.
  - Introduce queues for asynchronous workloads.
  - Add observability:
    - Logs.
    - Metrics.
    - Traces.
    - Alerts.
  - Define:
    - API versioning.
    - Authentication.
    - Authorization.
    - Rate limits.
    - Timeouts.
    - Retry policies.
    - Idempotency.
  - Design for graceful failure rather than assuming every dependency is always available.

---

## Q39. How would you handle long-running tasks in an API?
  - Do not keep the HTTP request open for several minutes if avoidable.
  - Accept the request and create a job:
    ```text
    POST /reports
        ↓
    Create job
        ↓
    Return 202 Accepted
        ↓
    Background worker processes job
        ↓
    Client checks job status
    ```
  - Example response:
    ```json
    {
      "job_id": "123",
      "status": "processing"
    }
    ```
  - Use a task queue and worker system for reliable processing.
  - Store job state so the client can retrieve progress/result.

---

## Q40. How would you design an API that integrates with an LLM?
  - Separate the API layer from the LLM integration layer.
  - Example:
    ```text
    Client
      ↓
    FastAPI
      ↓
    Authentication / validation
      ↓
    LLM service
      ↓
    Provider
    ```
  - Validate prompts and request parameters.
  - Set token/output limits.
  - Add timeouts.
  - Implement retries only where safe.
  - Log metadata rather than sensitive prompts when privacy requires it.
  - Consider:
    - Streaming responses.
    - Conversation state.
    - Prompt/version management.
    - Usage tracking.
    - Cost limits.
    - Content/security filtering.
    - Provider fallbacks.
  - Do not expose provider API keys to clients.

---

## Q41. How would you handle LLM timeouts and retries?
  - Set an explicit request timeout.
  - Retry only transient failures.
  - Use exponential backoff with jitter.
  - Limit the maximum number of retries.
  - Do not blindly retry every error.
  - Use a circuit breaker when an upstream provider is repeatedly failing.
  - Consider a fallback provider/model if the architecture supports it.
  - For long-running generation, consider asynchronous jobs or streaming.
  - Make sure retries do not accidentally create duplicate side effects.

---

## Q42. How would you prevent duplicate API requests?
  - Use **idempotency keys** for operations such as payments or order creation.
  - Client sends:
    ```text
    Idempotency-Key: abc123
    ```
  - Server stores the result associated with that key.
  - If the same request arrives again, return the original result instead of creating another resource.
  - Use database constraints for additional protection.
  - Make critical operations transactional.
  - This is especially important when clients retry because of network timeouts.

---

## Q43. How would you monitor and debug a production API?
  - Use the three main observability pillars:
    - **Logs** — what happened?
    - **Metrics** — how often/how much?
    - **Traces** — where did time go?
  - Track:
    - Request rate.
    - Error rate.
    - P50/P95/P99 latency.
    - CPU/memory.
    - Database latency.
    - Database connections.
    - Cache hit rate.
    - Queue depth.
    - External API latency.
  - Use correlation/request IDs to trace a request across services.
  - Create alerts for abnormal error rates and latency.
  - Avoid logging passwords, tokens, API keys, or other sensitive data.
  - For incidents:
    ```text
    Detect
      ↓
    Identify affected endpoint/service
      ↓
    Check metrics
      ↓
    Check logs/traces
      ↓
    Identify bottleneck
      ↓
    Mitigate
      ↓
    Fix root cause
      ↓
    Add monitoring/tests to prevent recurrence
    ```