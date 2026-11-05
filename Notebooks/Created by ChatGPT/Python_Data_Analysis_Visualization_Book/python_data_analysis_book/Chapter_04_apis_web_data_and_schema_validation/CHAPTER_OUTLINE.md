# Chapter 04 — APIs, Web Data, and Schema Validation

**Purpose:** External systems expose data through HTTP APIs or web pages. Learn HTTP request structure, JSON response handling, defensive parsing, HTML extraction, and schema validation.

**Prerequisites:** Dictionaries, JSON, exceptions, and basic DataFrames; live internet access is optional.

## Learning goals
- Explain URLs, methods, status codes, headers, query parameters, and timeouts.
- Use Requests to retrieve and check API responses.
- Parse HTML locally with BeautifulSoup.
- Validate records with Pydantic and report malformed data.

## Topic and subtopic plan
### 1. HTTP and REST
An HTTP request combines a method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), URL, headers, optional query parameters, and sometimes a body. Responses carry status codes, headers, and content. `2xx` means success; `3xx` redirection; `4xx` client-side issue; `5xx` server-side issue. REST-style APIs model resources, but actual APIs differ: check authentication, pagination, rate limits, and terms.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Requests API and arguments
`requests.get(url, params=None, headers=None, timeout=None, auth=None, verify=True, allow_redirects=True)` sends a GET. `params` encodes query parameters; `headers` sends metadata; `timeout` bounds waits; `verify=True` validates TLS certificates and should normally stay enabled. Inspect `status_code`, `headers`, `text`, `content`; use `.json()` for JSON and `.raise_for_status()` for unsuccessful HTTP responses.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Error handling and retries
Set timeouts. Catch `Timeout`, `ConnectionError`, and `HTTPError` separately when recovery differs. Respect `Retry-After` for rate limits; bound retries and use backoff for transient failures. Do not retry non-idempotent writes blindly. Validate response shape before loading it into an analytical table. Never log tokens or passwords.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. BeautifulSoup
`BeautifulSoup(markup, "html.parser")` parses HTML. `find` returns the first match; `find_all` returns all matches; CSS selectors use `.select` and `.select_one`. `.get_text(separator=" ", strip=True)` extracts clean text; `.get("href")` reads an attribute. Prefer documented APIs; respect site policies and minimize requests.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Pydantic contracts
Pydantic models validate records using type annotations. `BaseModel` declares fields; `Field(gt=0, min_length=1, ...)` adds constraints. Validation errors identify invalid fields and reasons. Choose whether invalid data stops a job, is quarantined, or is corrected under an explicit rule. Pydantic v2 uses `model_validate`; `parse_obj` is a common v1/v2 compatibility path but deprecated in v2.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Inspect the response envelope; Guided 2 — Parse the HTML catalogue; Guided 3 — Validate with Pydantic; Guided 4 — Build a defensive HTTP function |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a local ingestion pipeline that reads an API-shaped JSON fixture, parses an HTML catalogue, validates products, and creates a clean DataFrame.

### Required tasks
- Check the JSON response status and record count.
- Extract products with a CSS selector from the provided HTML.
- Define positive-price and non-empty-name validation.
- Separate valid and invalid records.
- Explain how a live API function should handle timeout and HTTP errors.

### Extension challenge
Add a paginated API workflow using `next_page` tokens. Respect retry-after headers and do not retry schema-validation failures as network errors.

### References
- Requests: https://requests.readthedocs.io/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pydantic: https://docs.pydantic.dev/
