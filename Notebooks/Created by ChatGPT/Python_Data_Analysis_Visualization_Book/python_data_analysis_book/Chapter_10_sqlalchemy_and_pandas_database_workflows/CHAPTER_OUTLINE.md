# Chapter 10 — SQLAlchemy and Pandas Database Workflows

**Purpose:** SQLAlchemy provides database connectivity and SQL expression/ORM layers. Pandas bridges SQL queries and DataFrames. Learn engines, connections, transactions, bind parameters, and table exchange.

**Prerequisites:** Chapter 9 SQL. Install SQLAlchemy; MySQL driver is optional for the SQLite demonstrations.

## Learning goals
- Distinguish Engine, Connection, Session, and ORM concepts.
- Create database URLs and configure connection behavior.
- Execute bound SQL with text().
- Read and write DataFrames to relational databases safely.

## Topic and subtopic plan
### 1. Engine, Connection, dialect, Session
An SQLAlchemy Engine is a long-lived factory and connection pool. A Connection is a checked-out DBAPI connection for statements. A Dialect adapts SQL to the database and driver. A Session is the ORM unit-of-work interface; simple analytical queries often need Core connections, not ORM objects. Reuse an engine rather than creating one for every query.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. URLs and secrets
URL structure: `dialect+driver://username:password@host:port/database`. SQLite examples use `sqlite:///path.db` or `sqlite://` for memory. `URL.create()` avoids manual escaping of special characters. MySQL URLs can use `mysql+mysqlconnector://...` or `mysql+pymysql://...`. Build from environment variables or secret storage; do not hardcode credentials.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. SQL text and parameters
`text("SELECT ... WHERE key=:value")` creates a textual SQL expression with named bind parameters. Execute via `conn.execute(stmt,{"value":v})`. Use `engine.connect()` for queries; `engine.begin()` gives a transaction that commits on successful exit and rolls back on exception. SQLAlchemy 2.x favors explicit Connection execution.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Pandas SQL integration
`pd.read_sql(sql, con, params=None, parse_dates=None, ...)` reads a query/table into a DataFrame. `DataFrame.to_sql(name, con, if_exists="fail", index=True, chunksize=None, dtype=None, method=None)` writes. `if_exists` options: fail, replace, append. `replace` drops/recreates a table and can destroy constraints/indexes. `index=False` prevents an unwanted index column.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Pools and performance
Engine pool arguments include `pool_size`, `max_overflow`, `pool_timeout`, and `pool_recycle`; tune based on workload, not guesses. `chunksize` batches inserts; `method="multi"` can improve inserts where the driver supports it. For very large imports, use database-native bulk loading. Validate row counts and constraints after loads.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Use transactions; Guided 2 — Read with Pandas; Guided 3 — Append a frame; Guided 4 — Configure MySQL |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a local SQLAlchemy/Pandas workflow, query results into a DataFrame, append a frame, then document how to enable the same approach with MySQL.

### Required tasks
- Create a local SQLite engine.
- Create and populate a table with bound parameters.
- Read results into Pandas.
- Append rows with to_sql.
- Explain the risks of replace and the role of transactions.

### Extension challenge
Add a staging table, validation queries, and an explicit transaction. Compare Core connections with ORM sessions for analytical extraction.

### References
- SQLAlchemy 2.0 Tutorial: https://docs.sqlalchemy.org/en/20/tutorial/
- Engine configuration: https://docs.sqlalchemy.org/en/20/core/engines.html
- Pandas SQL IO: https://pandas.pydata.org/docs/user_guide/io.html#sql-queries
