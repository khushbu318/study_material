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

# SQL Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience working with PostgreSQL, MySQL, SQLite, SQLAlchemy, Alembic, FastAPI, data pipelines, and analytics. I regularly write SQL queries for AI applications, user management, vector databases, reporting, and backend services.

---

# Joins

---

## Q1. What is a JOIN? Explain the Types of JOINs.

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

## Q2. Write a JOIN Query

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

## Q3. Write a Query to Get Departments with No Employees

```sql
SELECT
d.department_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;
```

---

## Q4. Pandas JOIN vs SQL JOIN

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

---

## Q5. What are Keys in SQL?

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

## Q6. What are SQL Relationships?

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

## Q7. What is ACID?

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

---

## Q8. Write a Query to Get Top 2 Spending Customers

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

## Q9. What is the Default in ORDER BY?

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

## Q10. What are Subqueries and CTEs in SQL?

### Subquery

A **subquery** is a query written inside another SQL query. The inner query executes first, and its result is used by the outer query.

A subquery can be used inside:

- `WHERE`
- `FROM`
- `SELECT`
- `HAVING`

### Example of a Subquery

Find employees whose salary is greater than the **average salary**:

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```
Here, the inner query:
```sql
SELECT AVG(salary)
FROM employees;
```

> calculates the average salary, and the outer query returns employees whose salary is greater than that average.

### CTE (Common Table Expression)

A CTE is a temporary named result set that we define using the `WITH` clause. It makes complex queries easier to **read, understand, and maintain**.

### Example of a CTE

The same problem can be written using a CTE:

```sql
WITH avg_salary AS (
    SELECT AVG(salary) AS average_salary
    FROM employees
)
SELECT employee_name, salary
FROM employees
CROSS JOIN avg_salary
WHERE salary > average_salary;
```

### Subquery vs CTE

| Feature | Subquery | CTE |
|---|---|---|
| **Definition** | Query inside another query | Named temporary result using `WITH` |
| **Readability** | Can become difficult with complex queries | Usually easier to read |
| **Reusability** | Usually used in one location | Can be referenced multiple times within the query |
| **Complex Queries** | Can become nested and difficult to maintain | Better for breaking complex logic into steps |
| **Recursive Queries** | Not ideal | Supports recursive CTEs in databases that support them |

> **Interview Tip:** Use a **subquery** for simple one-time nested logic. Use a **CTE** when the query has multiple logical steps or when you want to make complex SQL more readable and maintainable.
---

## Common SQL Scenario-Based Interview Questions

---

### Q11. Find the Second Highest Salary

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);
```
---
### 2. Find the Nth Highest Salary
```sql 
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
```
> OFFSET `2` returns the **3rd highest salary**. For the `Nth` highest salary, use `OFFSET N-1`.
---
### 3. Find Employees Who Earn More Than Their Department Average
```sql
SELECT employee_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
```
---
### 4. Find Duplicate Records
```sql
SELECT email, COUNT(*) AS count
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;
```
---
### 5. Find Employees Who Do Not Have a Department
```sql
SELECT e.employee_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```
---
### 6. Find the Highest-Paid Employee in Each Department
```sql
SELECT employee_name, department, salary
FROM (
    SELECT
        employee_name,
        department,
        salary,
        RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
) ranked
WHERE salary_rank = 1;
```
---
### 7. Find Employees With the Same Salary
```sql
SELECT salary, COUNT(*) AS employee_count
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1;
```
---
### 8. Find Employees Who Joined in the Last 30 Days
```sql 
SELECT *
FROM employees
WHERE joining_date >= CURRENT_DATE - INTERVAL '30 days';
```
> The exact date syntax can vary between databases such as PostgreSQL, MySQL, and SQL Server.
---
### 9. Find the Top 3 Salaries in Each Department
```sql
SELECT employee_name, department, salary
FROM (
    SELECT
        employee_name,
        department,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
) ranked
WHERE salary_rank <= 3;
```
---
### 10. Find Customers Who Have Never Placed an Order
```sql
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;
```
---
### 11. Find the Total Sales for Each Customer
```sql
SELECT
    customer_id,
    SUM(amount) AS total_sales
FROM orders
GROUP BY customer_id;
```
---
### 12. Find Departments Having More Than 5 Employees
```sql
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```
---
### 13. Find the Running Total of Sales
```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;
```
---
### 14. Find Employees Whose Salary Is Higher Than the Previous Employee
```sql
SELECT
    employee_name,
    salary,
    LAG(salary) OVER (
        ORDER BY employee_id
    ) AS previous_salary
FROM employees;
```
---
### 15. Find the Difference Between Current and Previous Salary
```sql
SELECT
    employee_name,
    salary,
    salary - LAG(salary) OVER (
        ORDER BY employee_id
    ) AS salary_difference
FROM employees;
```
> Interview Tip: Most SQL scenario-based questions test your understanding of `JOIN`, `GROUP BY`, `HAVING`, **subqueries, CTEs, window functions, aggregate functions,** and **filtering**. Focus on understanding why each clause is used rather than memorizing queries.

---

## Q12. What are Window Functions in SQL?

A **window function** performs a calculation across a set of related rows without combining those rows into a single row.

Unlike `GROUP BY`, a window function **keeps the original rows** while adding the calculated result.

Common window functions include:

- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `SUM()`
- `AVG()`
- `COUNT()`
- `LAG()`
- `LEAD()`

### Basic Syntax

```sql
function_name() OVER (
    PARTITION BY column
    ORDER BY column
)
```
`PARTITION BY` → Divides the rows into groups.
`ORDER BY` → Defines the order in which the window function operates.

We want to assign a salary rank within each department:
```sql
SELECT
    employee_name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;
```
Here:

- `PARTITION BY department` creates a separate window for each department.
- `ORDER BY salary DESC` ranks employees from highest to lowest salary.
- `RANK()` assigns the rank.
- The original employee rows are **not collapsed**, unlike with `GROUP BY`.

### Window Function vs GROUP BY

| Window Function | `GROUP BY` |
|---|---|
| Keeps individual rows | Combines rows into groups |
| Adds calculated values to each row | Returns one row per group |
| Useful for ranking, running totals, comparisons | Useful for aggregations |
| Uses `OVER()` | Uses `GROUP BY` |

> **Interview Tip:** The key difference to remember is: **`GROUP BY` reduces rows, while window functions perform calculations across related rows without reducing the number of rows.**

---




# Database Design

---

## Q13. Do You Know Database Design?

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

## Q14. Benefits of SQLite over PostgreSQL

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

## Q15. Have You Used Alembic or Do You Write Queries Directly?

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

## Q16. Difference Between DELETE, TRUNCATE, and DROP

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
---
## Q17. What is Database Normalization and Denormalization?

### Normalization

**Normalization** is the process of organizing data into multiple related tables to **reduce data duplication and improve data consistency**.

For example, instead of storing customer information repeatedly in an `orders` table, we can separate customers and orders:

```text
Customers
---------
customer_id
customer_name
email

Orders
------
order_id
customer_id
order_date
amount
```
Here, `customer_id` acts as a *foreign key* in the `Orders` table.

### Main Goals of Normalization

1. Reduce duplicate data.
2. Improve data consistency.
3. Avoid update, insert, and delete anomalies.
4. Maintain clear relationships between tables.
5. Improve data integrity.

### Common Normal Forms

| Normal Form | Main Idea |
|---|---|
| **1NF** | Each column contains atomic/single values and there are no repeating groups. |
| **2NF** | Must be in 1NF and every non-key column depends on the entire primary key. |
| **3NF** | Must be in 2NF and non-key columns should not depend on other non-key columns. |
| **BCNF** | A stronger version of 3NF where every determinant is a candidate key. |

---

### Denormalization

**Denormalization** is the process of intentionally combining or duplicating data across tables to **improve read/query performance**.

For example, instead of joining `Customers` and `Orders` every time, we may store customer information directly in the `Orders` table:

```text
Orders
------
order_id
customer_id
customer_name
email
order_date
amount
```
Here, `customer_name` and `email` may be duplicated across multiple orders.

### Normalization vs Denormalization

| Feature | Normalization | Denormalization |
|---|---|---|
| **Main Goal** | Reduce duplication | Improve read performance |
| **Data Duplication** | Minimized | Intentionally increased |
| **Number of Tables** | Usually more | Usually fewer |
| **JOINs** | More likely | Reduced |
| **Storage** | Generally less | Generally more |
| **Data Consistency** | Easier to maintain | More difficult to maintain |
| **Read Performance** | Can require more joins | Often faster for read-heavy queries |
| **Write Performance** | Usually better for maintaining consistency | Can require updates in multiple places |

### When to Use?

**Normalization:**

- Transactional systems
- Frequently updated data
- Systems where data consistency is important
- OLTP applications

**Denormalization:**

- Read-heavy applications
- Reporting and analytics
- Data warehouses
- When reducing expensive joins improves performance

> **Interview Tip:** A simple way to remember it is: **Normalization focuses on reducing redundancy and maintaining consistency, while denormalization intentionally introduces some redundancy to improve read performance.**
---
# Indexing & Query Optimization

---

## Q18. What is Indexing and Query Optimization in SQL?

### Indexing

An **index** is a data structure created on one or more columns of a table to make data retrieval **faster**.

Instead of scanning every row in the table, the database can use the index to quickly find the required rows.

For example:

```sql
CREATE INDEX idx_employee_email
ON employees(email);
```

Now, a query such as:
```sql
SELECT *
FROM employees
WHERE email = 'john@example.com';
```

can use the index on `email` to find the matching record more efficiently.

### How an Index Works

`Without` an index:
```
Query → Scan every row → Find matching row
```
`With` an index:
```
Query → Search Index → Locate matching row → Return data
```

### Common Types of Indexes

| Index Type | Purpose |
|---|---|
| **Single-Column Index** | Index created on one column |
| **Composite Index** | Index created on multiple columns |
| **Unique Index** | Ensures indexed values are unique |
| **Primary Key Index** | Index associated with the primary key |
| **Clustered Index** | Determines the physical/logical ordering of table data in databases that support clustered indexes |
| **Non-Clustered Index** | Separate index structure that points to the underlying table data |

### Advantages of Indexing

1. Faster `SELECT` queries.
2. Faster filtering using `WHERE`.
3. Faster `JOIN` operations.
4. Faster sorting and grouping in some cases.
5. Can improve lookup performance on frequently searched columns.

### Disadvantages of Indexing

1. Requires additional storage.
2. `INSERT`, `UPDATE`, and `DELETE` operations can become slower because indexes also need to be updated.
3. Too many indexes can negatively affect database performance.
4. Indexes need to be designed based on actual query patterns.

---

### Query Optimization

**Query optimization** is the process of improving a SQL query so that the database can execute it **faster and with fewer resources**.

The database optimizer analyzes a query and chooses an efficient **execution plan**.

For example, it may decide whether to:

- Use an index or perform a table scan.
- Use a particular join strategy.
- Apply filters early.
- Choose the order in which tables should be joined.

### Example

Instead of:

```sql
SELECT *
FROM employees
WHERE department = 'IT';
```
we can avoid fetching unnecessary columns:
```sql
SELECT employee_name, salary
FROM employees
WHERE department = 'IT';
```
This can reduce the amount of data that needs to be read and returned.

### Common Query Optimization Techniques

| Technique | Explanation |
|---|---|
| **Use Appropriate Indexes** | Create indexes on columns frequently used in `WHERE`, `JOIN`, `ORDER BY`, and sometimes `GROUP BY`. |
| **Avoid `SELECT *`** | Select only the columns that are required. |
| **Filter Early** | Apply filters as early as practical to reduce the amount of data processed. |
| **Optimize JOINs** | Ensure appropriate columns are indexed and avoid unnecessary joins. |
| **Use EXPLAIN** | Analyze the query execution plan to identify expensive operations. |
| **Avoid Unnecessary Subqueries** | Use joins or CTEs where they make the query more efficient or readable. |
| **Use Pagination** | Avoid returning extremely large result sets at once. |
| **Avoid Functions on Indexed Columns When Possible** | Applying functions to indexed columns can prevent efficient index usage in some databases. |

### EXPLAIN Example

We can use `EXPLAIN` to inspect how the database plans to execute a query:

```sql
EXPLAIN
SELECT *
FROM employees
WHERE email = 'john@example.com';
```

The execution plan can help identify:

- Whether an index is being used.
- Whether a full table scan is happening.
- Which join strategy is being used.
- Which operations are expensive.

> **Interview Tip**: Remember: **Indexing improves data lookup performance, while query optimization focuses on improving the overall execution of SQL queries.** Indexes can make reads faster, but excessive indexing can slow down write operations.


# Transactions & Concurrency

---

## Q19. What are Transactions and ACID Properties in SQL?

### Transaction

A **transaction** is a sequence of one or more SQL operations that are treated as a **single unit of work**.

A transaction should either **complete successfully as a whole** or **have all its changes rolled back** if something fails.

### Example

Suppose we transfer ₹5,000 from Account A to Account B:

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 101;

UPDATE accounts
SET balance = balance + 5000
WHERE account_id = 102;

COMMIT;
```
If any operation fails, we can roll back the transaction:

```sql
ROLLBACK;
```
The main goal is to ensure that money is not deducted from one account without being added to the other.
---

### ACID Properties

ACID stands for:

**Atomicity, Consistency, Isolation, and Durability.**

| Property | Meaning | Example |
|---|---|---|
| **Atomicity** | All operations in a transaction succeed, or none of them are applied. | Money is either transferred completely or not transferred at all. |
| **Consistency** | A transaction takes the database from one valid state to another valid state while maintaining constraints and rules. | Account balances and database constraints remain valid after the transaction. |
| **Isolation** | Concurrent transactions should not incorrectly interfere with each other. | Two transactions updating the same account should not produce an incorrect balance. |
| **Durability** | Once a transaction is committed, its changes are permanently stored even if the system crashes. | After `COMMIT`, the money transfer remains recorded after a database restart. |

### Common Transaction Commands

| Command | Purpose |
|---|---|
| `BEGIN` / `START TRANSACTION` | Starts a transaction |
| `COMMIT` | Permanently saves the transaction changes |
| `ROLLBACK` | Undoes changes made during the transaction |
| `SAVEPOINT` | Creates a point within a transaction that we can roll back to |

### Transaction Example with Rollback

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 101;

-- If something goes wrong
ROLLBACK;
```
The changes made after `BEGIN` are undone.

### Why Are Transactions Important?

Transactions are especially important when multiple database operations must be treated as `one logical operation`, such as:

- Money transfers
- Order creation and payment processing
- Inventory updates
- Banking operations
- Booking and reservation systems

> Interview Tip: Remember ACID as: Atomicity = all or nothing, Consistency = valid state, Isolation = transactions don't incorrectly interfere, Durability = committed data is permanent.