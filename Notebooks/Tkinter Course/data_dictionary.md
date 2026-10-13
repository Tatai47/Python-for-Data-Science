# Data dictionary — sample sales files

The main file models **one row per order line**. An `order_id` can repeat because one order can include several products. Revenue/cost/profit are derived in the analytics pipeline, not stored in the base CSV.

| Column | Intended type | Meaning | Key cautions |
|---|---|---|---|
| `order_id` | string | Synthetic order identifier | May repeat across line items; count unique IDs for orders |
| `order_date` | date | Synthetic order date in 2026 | Stored in ISO `YYYY-MM-DD` form in CSV |
| `customer_id` | string | Synthetic customer identifier | Not a numeric measure |
| `region` | category/string | North, South, East, West, Central | Filters should define an All option explicitly |
| `product` | category/string | Synthetic product name | Values map to a product category |
| `category` | category/string | Electronics, Accessories, Furniture, Stationery | Validate unexpected values |
| `quantity` | integer | Unit count on one line | Negative or malformed values need a return/data-quality policy |
| `unit_price` | numeric | Selling price per unit | Currency units are illustrative; formatting does not define currency |
| `unit_cost` | numeric | Cost per unit | Missing cost is not the same as zero cost |
| `status` | category/string | Paid, Pending, Cancelled, Returned | Decide status inclusion for every metric |
| `revenue` | derived numeric | `quantity * unit_price` | Define return sign semantics before use |
| `cost` | derived numeric | `quantity * unit_cost` | Depends on valid unit cost and quantity |
| `profit` | derived numeric | `revenue - cost` | Negative values may be valid in refund/return cases |
| `profit_margin` | derived ratio | `profit / revenue` for nonzero revenue | Undefined when revenue is zero; preserve as missing/None |

`sample_sales.csv` is clean enough for introductory examples. `sales_with_issues.csv` intentionally contains invalid dates/numbers, missing customer IDs, inconsistent region casing/spacing, unexpected status values, negative quantities, and duplicate rows for validation exercises. All sample records are synthetic.
