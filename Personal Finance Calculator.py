#!/usr/bin/env python
# coding: utf-8

# In[12]:


def calculate_total_income(net_salary, additional_income):
    return net_salary + additional_income
def calculate_total_expenses(rent, utilities, groceries, transportation, other_expenses):
    return rent + utilities + groceries + transportation + other_expenses
def calculate_savings(total_income, total_expenses):
    return total_income - total_expenses

def main():
    print("Welcome to the Peronal Finance Calculator")
    
    salary = float(input("Enter you monthly net salary: $"))
    additional_income = float(input("Enter any additional monthly income: $"))
    
    rent = float(input("Enter your monthly rent: $"))
    utilities = float(input("Enter your monthly utilities bill: $"))
    groceries = float(input("Enter your monthly groceries expenses: $"))
    transportation = float(input("Enter your monthly transportation expenses: $"))
    other_expenses = float(input("Enter your other expenses: $"))
    
    total_income = calculate_total_income(salary, additional_income)
    total_expenses = calculate_total_expenses(rent, utilities, groceries, transportation, other_expenses)
    savings = calculate_savings(total_income, total_expenses)
    
    print("\nSummary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Savings: ${savings:.2f}")
    
if __name__ == "__main__":
    main()

