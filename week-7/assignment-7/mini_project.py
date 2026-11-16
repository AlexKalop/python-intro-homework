import csv
import os
import sys
from datetime import datetime


if not os.path.exists("../data/expense.csv"):
    print("expenses.csv not found.")
    sys.exit()
with open('../data/expenses.csv', 'r') as file:
    records = list(csv.DictReader(file))
for item in records: item['amount'] = float(item['amount'])
    
        
food_expenses = [row for row in records if row['category'] == 'Food'] 
total_cost = sum(expense['amount'] for expense in food_expenses) 

now = datetime.now()    
date = now.strftime("%B %d, %Y")
with open('food_report.txt', 'w') as file:
    file.write(f"Food Expense Report — generated {date}\n")
    for item in food_expenses:
        file.write(f"{item['date']}: ${item['amount']:.2f}\n")
    file.write(f"Total: ${total_cost:.2f}")

