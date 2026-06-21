import pandas as pd

def mask_email(email):
    username, domain = email.split("@")
    return username[0] + "***@" + domain

def salary_band(salary):
    if salary < 50000:
        return "30K-50K"
    elif salary < 80000:
        return "50K-80K"
    else:
        return "80K-120K"

employees = pd.read_csv("employees.csv")

employees["masked_email"] = employees["email"].apply(mask_email)
employees["salary_band"] = employees["salary"].apply(salary_band)

print(
    employees[
        [
            "name",
            "masked_email",
            "department",
            "salary_band"
        ]
    ].head()
)