#%%
import pandas as pd

officeEmployees = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "age": 28,
        "salary": 45000,
        "email": "aarav.sharma@example.com"
    },
    {
        "id": 2,
        "name": "Priya Singh",
        "age": 31,
        "salary": 58000,
        "email": "priya.singh@example.com"
    },
    {
        "id": 3,
        "name": "Rohan Verma",
        "age": 26,
        "salary": 42000,
        "email": "rohan.verma@example.com"
    },
    {
        "id": 4,
        "name": "Neha Gupta",
        "age": 35,
        "salary": 72000,
        "email": "neha.gupta@example.com"
    },
    {
        "id": 5,
        "name": "Vikram Patel",
        "age": 40,
        "salary": 90000,
        "email": "vikram.patel@example.com"
    },
    {
        "id": 6,
        "name": "Ananya Das",
        "age": 29,
        "salary": 51000,
        "email": "ananya.das@example.com"
    },
    {
        "id": 7,
        "name": "Karan Mehta",
        "age": 33,
        "salary": 65000,
        "email": "karan.mehta@example.com"
    },
    {
        "id": 8,
        "name": "Sneha Joshi",
        "age": 27,
        "salary": None,
        "email": "Sneha.Joshi@example.com"
    },
    {
        "id": 9,
        "name": "Rahul Kapoor",
        "age": None,
        "salary": None,
        "email": "rahul.kapoor@example.com"
    },
    {
        "id": 10,
        "name": "Meera Nair",
        "age": 30,
        "salary": 60000,
        "email": "meera.nair@example.com"
    },

]

df = pd.DataFrame(officeEmployees)

print(df)

# Save to CSV
df.to_csv("officeEmployees.csv", index=False)