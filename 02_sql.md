# SQL Interview Questions

Importance: ⭐⭐⭐ = Asked 3+ times | ⭐⭐ = Asked 2 times | ⭐ = Asked once

---

## Joins

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is JOIN and types of joins | 3x (Q13, Q27, Q54) | ⭐⭐⭐ |
| Write a JOIN query | 2x (Q13, Q57) | ⭐⭐ |
| Write query to get departments with no employees (using JOIN) | 1x (Q57) | ⭐ |
| Pandas join query vs SQL join query | 1x (Q27) | ⭐ |

---

## Keys & Constraints

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What are keys in SQL (Primary, Foreign, Unique, etc.) | 1x (Q104) | ⭐ |
| What are SQL relationships | 1x (Q27) | ⭐ |
| What is ACID | 1x (Q128) | ⭐ |

---

## Querying & Clauses

| Question | Times Asked | Importance |
|----------|-------------|------------|
| Write a query to get top 2 spending customers | 1x (Q55) | ⭐ |
| What is the default in `ORDER BY` clause — ASC or DESC | 1x (Q56) | ⭐ |

---

## Database Design

| Question | Times Asked | Importance |
|----------|-------------|------------|
| Do you know database design | 1x (Q122) | ⭐ |
| Benefits of SQLite over PostgreSQL | 1x (Q148) | ⭐ |
| Have you used Alembic or write queries directly in large applications | 1x (Q149) | ⭐ |

---
---
---

# SQL Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience working with PostgreSQL, MySQL, SQLite, SQLAlchemy, Alembic, FastAPI, data pipelines, and analytics. I regularly write SQL queries for AI applications, user management, vector databases, reporting, and backend services.

---

# Joins

## 1. What is a JOIN? Explain the Types of JOINs.

A **JOIN** is used to combine rows from two or more tables based on a related column.

### Types of JOINs

### INNER JOIN

Returns only matching records from both tables.

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
```

---

### LEFT JOIN (LEFT OUTER JOIN)

Returns all records from the left table and matching records from the right table.

If no match exists, NULL values are returned.

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;
```

---

### RIGHT JOIN (RIGHT OUTER JOIN)

Returns all rows from the right table and matching rows from the left table.

```sql
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
```

---

### FULL OUTER JOIN

Returns all records from both tables.

If there is no match, NULL values are returned.

```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;
```

---

### CROSS JOIN

Returns the Cartesian product of both tables.

```sql
SELECT *
FROM employees
CROSS JOIN departments;
```

---

### SELF JOIN

A table joins with itself.

```sql
SELECT
e1.name AS Employee,
e2.name AS Manager
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.employee_id;
```

---

### Real-world Usage

In AI applications, I frequently use JOINs to combine:

- Users and subscriptions
- Models and predictions
- Orders and customers
- Chat sessions and messages
- Employees and departments

---

## 2. Write a JOIN Query

Example tables:

**Employees**

| employee_id | name | department_id |
|-------------|------|---------------|
|1|John|10|
|2|Alice|20|

**Departments**

| department_id | department_name |
|---------------|----------------|
|10|HR|
|20|IT|

Query

```sql
SELECT
e.employee_id,
e.name,
d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
```

---

## 3. Write a Query to Get Departments with No Employees

```sql
SELECT
d.department_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;
```

---

## 4. Pandas JOIN vs SQL JOIN

### SQL

```sql
SELECT *
FROM employee e
JOIN department d
ON e.department_id = d.department_id;
```

### Pandas

```python
import pandas as pd

result = employee.merge(
    department,
    on="department_id",
    how="inner"
)
```

### Mapping

| SQL | Pandas |
|------|---------|
| INNER JOIN | merge(how="inner") |
| LEFT JOIN | merge(how="left") |
| RIGHT JOIN | merge(how="right") |
| FULL JOIN | merge(how="outer") |

---

# Keys & Constraints

## 5. What are Keys in SQL?

Keys are used to uniquely identify records and establish relationships between tables.

### Primary Key

- Unique
- Cannot be NULL
- One per table

```sql
employee_id INT PRIMARY KEY
```

---

### Foreign Key

Maintains relationships between tables.

```sql
department_id INT
REFERENCES departments(department_id)
```

---

### Unique Key

Ensures all values are unique.

```sql
email VARCHAR(100) UNIQUE
```

---

### Candidate Key

Columns that can uniquely identify a row.

Example:

- Employee ID
- Aadhaar Number
- Email

---

### Composite Key

Combination of multiple columns.

```sql
PRIMARY KEY(order_id, product_id)
```

---

### Super Key

A set of one or more columns that uniquely identifies a row.

---

## 6. What are SQL Relationships?

### One-to-One

One record maps to one record.

Example:

- User ↔ Passport

---

### One-to-Many

Most common relationship.

Example:

- Department → Employees

---

### Many-to-Many

Implemented using a junction table.

Example:

- Students ↔ Courses

```
students
courses
student_courses
```

---

## 7. What is ACID?

ACID ensures reliable database transactions.

### A — Atomicity

Transaction executes completely or not at all.

---

### C — Consistency

Database always remains valid.

---

### I — Isolation

Concurrent transactions do not interfere.

---

### D — Durability

Committed data remains even after a crash.

---

### Example

Money Transfer

```
Debit Account A

Credit Account B

Commit
```

If one operation fails, the entire transaction is rolled back.

---

# Querying & Clauses

## 8. Write a Query to Get Top 2 Spending Customers

Suppose table:

```
Orders

customer_id
amount
```

Query

```sql
SELECT
customer_id,
SUM(amount) AS total_spent
FROM Orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 2;
```

---

## 9. What is the Default in ORDER BY?

The default sorting order is:

```
ASC (Ascending)
```

Example

```sql
SELECT *
FROM employees
ORDER BY salary;
```

Equivalent to

```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

Descending

```sql
ORDER BY salary DESC;
```

---

# Database Design

## 10. Do You Know Database Design?

Yes.

While developing AI and backend applications, I follow database normalization principles and design relational schemas based on business requirements.

### Steps I Follow

1. Identify entities.
2. Define attributes.
3. Choose primary keys.
4. Create relationships.
5. Apply normalization (up to 3NF in most cases).
6. Add indexes where needed.
7. Use foreign keys for referential integrity.

### Real-world Example

For an AI chatbot project, I designed tables for:

- Users
- Conversations
- Messages
- LLM Models
- API Usage
- Billing

These tables were connected using primary and foreign keys to maintain data integrity.

---

## 11. Benefits of SQLite over PostgreSQL

| SQLite | PostgreSQL |
|----------|------------|
| File-based database | Client-server database |
| No installation required | Requires server setup |
| Lightweight | Enterprise-grade |
| Easy to embed | Supports large-scale applications |
| Best for local development | Best for production systems |

### When I Use SQLite

- Local development
- Proof of Concepts (POCs)
- Small desktop applications
- Unit testing

### When I Use PostgreSQL

- Production APIs
- AI platforms
- Multi-user applications
- Large datasets
- High concurrency

---

## 12. Have You Used Alembic or Do You Write Queries Directly?

Yes.

In production applications, I primarily use **SQLAlchemy ORM** with **Alembic** for database migrations.

### Why Alembic?

- Version-controlled schema changes
- Easy rollback support
- Team collaboration
- Safe production deployments
- Automated migration generation

### Typical Workflow

```bash
alembic revision --autogenerate -m "Add user table"

alembic upgrade head
```

### Do I Write Raw SQL?

Yes, when needed.

I use raw SQL for:

- Complex JOINs
- Reporting queries
- Performance-critical operations
- Window functions
- Bulk updates

Otherwise, I prefer SQLAlchemy ORM for better maintainability and readability.

---

## 13. Difference Between DELETE, TRUNCATE, and DROP

| DELETE | TRUNCATE | DROP |
|----------|-----------|------|
| Removes selected rows | Removes all rows | Removes entire table |
| WHERE clause supported | WHERE not supported | Deletes table structure |
| Can be rolled back (within a transaction in most DBMS) | Usually minimally logged; rollback behavior depends on DBMS | Removes schema object |
| Table remains | Table remains | Table no longer exists |

### Examples

```sql
DELETE FROM employees
WHERE employee_id = 1;
```

```sql
TRUNCATE TABLE employees;
```

```sql
DROP TABLE employees;
```
