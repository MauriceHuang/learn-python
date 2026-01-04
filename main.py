import pandas as pd

monthly_expense_pm = 3000
expense_inflation_rate = 0.03
start_age = 30
end_age = 65

ages = list(range(start_age, end_age + 1))
years = [age - start_age for age in ages]
fv_expenses = [monthly_expense_pm * (1 + expense_inflation_rate) ** year for year in years]

df = pd.DataFrame({
    'age': ages,
    'monthly_expense_fv': fv_expenses
})

print(df.to_string(index=False))
