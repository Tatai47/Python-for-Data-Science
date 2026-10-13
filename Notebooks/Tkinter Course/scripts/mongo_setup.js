// Optional MongoDB shell example. Run only against a development database you control.
// This script inserts two synthetic documents; rerunning creates new ObjectIds.
use analytics;

db.orders.insertMany([
  {
    order_id: "ORD-DEMO-0001",
    order_date: ISODate("2026-06-15T10:00:00Z"),
    customer_id: "CUS-DEMO-0001",
    region: "North",
    status: "Paid",
    items: [
      { product: "Monitor", category: "Electronics", quantity: 1, unit_price: NumberDecimal("14000.00"), unit_cost: NumberDecimal("9800.00") },
      { product: "Mouse", category: "Accessories", quantity: 2, unit_price: NumberDecimal("850.00"), unit_cost: NumberDecimal("400.00") }
    ]
  },
  {
    order_id: "ORD-DEMO-0002",
    order_date: ISODate("2026-06-18T09:15:00Z"),
    customer_id: "CUS-DEMO-0002",
    region: "West",
    status: "Pending",
    items: [
      { product: "Chair", category: "Furniture", quantity: 1, unit_price: NumberDecimal("6500.00"), unit_cost: NumberDecimal("4300.00") }
    ]
  }
]);

db.orders.createIndex({ order_date: 1, region: 1, status: 1 });
