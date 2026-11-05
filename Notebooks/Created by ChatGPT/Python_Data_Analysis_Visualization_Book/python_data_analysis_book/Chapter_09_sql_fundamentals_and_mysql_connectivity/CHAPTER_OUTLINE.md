# Chapter 09 — SQL Fundamentals and MySQL Connectivity

**Purpose:** SQL is the language for relational data. Connect relational design and query logic to Python database drivers, transactions, parameterized SQL, and safe resource handling.

**Prerequisites:** Basic tables and Python functions. MySQL server only needed for live-connection exercises; SQLite is used for local SQL drills.

## Learning goals
- Explain tables, rows, primary keys, and foreign keys.
- Write SELECT, WHERE, GROUP BY, HAVING, JOIN, and subqueries.
- Connect with mysql-connector-python or PyMySQL.
- Use parameterized statements, transactions, cursors, commits, and rollbacks.

## Topic and subtopic plan
### 1. Relational model and keys
A table contains rows at a defined grain. A primary key uniquely identifies a row; a foreign key references a key in another table. A one-to-many relationship stores the parent key on the many-side. Normalization limits update anomalies. Define the grain and key before designing joins.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. SELECT query anatomy
Typical SQL: `SELECT columns FROM table WHERE condition GROUP BY keys HAVING aggregate_condition ORDER BY expression LIMIT n`. Logical processing is conceptually FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. `WHERE` filters rows; `HAVING` filters groups. `COUNT(*)` counts rows; `COUNT(column)` ignores NULL; `COUNT(DISTINCT column)` counts unique non-null values.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Joins and NULLs
`INNER JOIN` keeps matching pairs; `LEFT JOIN` retains all left rows; `RIGHT JOIN` retains the right; `FULL OUTER JOIN` retains both where supported. Duplicate join keys can multiply rows. SQL uses three-valued logic: `column = NULL` is not a null test; use `IS NULL`/`IS NOT NULL`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Python MySQL drivers
`mysql.connector.connect(host, port=3306, user, password, database, connection_timeout=...)` opens Connector/Python connections. `connection.cursor()` yields a cursor; `execute`, `fetchone`, `fetchmany(size)`, and `fetchall` are DB-API patterns. `cursor(dictionary=True)` returns mappings with Connector/Python. PyMySQL is another DB-API driver; its cursor classes include `DictCursor`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Parameters, transactions, and security
Connector/Python and PyMySQL commonly use `%s` value placeholders; SQLite uses `?`. Pass values separately. Placeholders cannot safely stand for table or column identifiers; dynamic identifiers require allow-lists and proper quoting. `commit()` makes changes durable; `rollback()` cancels uncommitted work. Use try/except, close cursors/connections, environment variables, and least-privilege accounts.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Read SQL rows; Guided 2 — Aggregate by group; Guided 3 — Use parameters; Guided 4 — Commit and rollback |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Practice SQL locally, then adapt the same query logic to a MySQL database using a real driver.

### Required tasks
- Create customer and order tables with primary and foreign keys.
- Insert rows using parameterized statements.
- Write a JOIN grouped by city.
- Show how to rollback an update.
- Explain SQLite ? placeholders versus MySQL driver %s placeholders.

### Extension challenge
Implement an idempotent customer import using a unique business key. Compare MySQL `INSERT`, `INSERT IGNORE`, and `INSERT ... ON DUPLICATE KEY UPDATE` and test duplicate handling.

### References
- MySQL Reference: https://dev.mysql.com/doc/refman/8.4/en/
- Connector/Python: https://dev.mysql.com/doc/connector-python/en/
- PyMySQL: https://pymysql.readthedocs.io/
