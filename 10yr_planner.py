# Import the necessary libraries
import math

# Define the necessary variables
savings_goal = 1000000
years_to_save = 10

# Calculate the number of months to save
months_to_save = years_to_save * 12

# Initialize the current savings amount to 0
current_savings = 0

# Start a loop that runs for the number of months to save
for month in range(months_to_save):
  # Prompt the user to enter the current savings, monthly salary, monthly expenses, and any additional income
  current_savings = float(input("Enter your current savings: "))
  monthly_salary = float(input("Enter your monthly salary: "))
  monthly_expenses = float(input("Enter your monthly expenses: "))
  additional_income = float(input("Enter any additional income: "))
  
  # Calculate the monthly savings amount
  monthly_savings = monthly_salary + additional_income - monthly_expenses
  
  # Update the current savings amount
  current_savings += monthly_savings
  
  # Calculate the difference between the savings goal and the current savings amount
  difference = savings_goal - current_savings
  
  # If the current savings is less than the savings goal, print a message indicating how much more needs to be saved
  if current_savings < savings_goal:
    print(f"You need to save an additional ${difference:.2f} to reach your goal.")
  
  # If the current savings is equal to the savings goal, print a message indicating the goal has been reached
  elif current_savings == savings_goal:
    print("Congratulations, you have reached your savings goal!")
  
  # If the current savings is greater than the savings goal, print a message indicating the goal has been exceeded
  else:
    print("Congratulations, you have exceeded your savings goal!")
    
  # Prompt the user to update the amounts for the next month
  input("Press enter to update the amounts for the next month.")
