from faker import Faker
import pandas as pd
import random

fake = Faker()

# Employees
employees = []

for i in range(1, 501):
    employees.append({
        "id": i,
        "name": fake.name(),
        "email": fake.email(),
        "department": random.choice(["HR", "Sales", "IT", "Finance"]),
        "salary": random.randint(30000, 120000),
        "performance_score": random.randint(1, 100)
    })

employees_df = pd.DataFrame(employees)
employees_df.to_csv("employees.csv", index=False)

# Sales
sales = []

for i in range(1, 1001):
    sales.append({
        "id": i,
        "employee_id": random.randint(1, 500),
        "sale_amount": random.randint(1000, 50000),
        "sale_date": fake.date_this_year()
    })

sales_df = pd.DataFrame(sales)
sales_df.to_csv("sales.csv", index=False)

print("CSV files created successfully!")