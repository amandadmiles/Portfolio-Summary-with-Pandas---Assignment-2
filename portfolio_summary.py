"""
Program: portfolio_summary.py
Author: Amanda Miles

Purpose: This program demonstrates basic pandas library functions by reading
a sample investment portfolio from a CSV file, cleaning the data, calculating
cost, value, gain or loss, and summarizing the portfolio by sector.

Built-in Python functions used:
1. input() - Used to ask the user for the CSV file name. This function is used
for terminal input and is discussed with basic input and output in Chapter 1.

2. print() - Used to display the portfolio report. This function is used for
terminal output and is discussed with basic input and output in Chapter 1.

3. round() - Used to round money totals to two decimal places. This function is
used to format calculated numeric output and relates to arithmetic expressions
and numeric data in Chapter 2.

Pandas library functions and methods used:
pd.read_csv() - Used to read portfolio data from a CSV file into a DataFrame.
drop_duplicates() - Used to remove repeated portfolio rows.
fillna() - Used to replace missing values with 0.
groupby() - Used to group portfolio results by sector.
sum() - Used to calculate total cost, value, and gain or loss.
sort_values() - Used to sort the sector summary by portfolio value.
to_string() - Used to display DataFrame output clearly in the terminal.
"""

import pandas as pd

# Defines the main function for the program. Section 5.2
def main():
    fileName = input("Enter the portfolio CSV file name: ")

    # Uses the pandas read_csv function to load data from a CSV file.
    data = pd.read_csv(fileName)

    print()
    print("Original Portfolio Data")
    print(data.to_string(index=False))

    # Uses the pandas drop_duplicates method to remove repeated rows.
    data = data.drop_duplicates()

    # Uses the pandas fillna method to replace missing values with 0.
    data = data.fillna(0)

    # Uses arithmetic expressions to calculate total cost. Section 2.4
    data["Cost"] = data["Shares"] * data["Purchase Price"]

    # Uses arithmetic expressions to calculate current value. Section 2.4
    data["Value"] = data["Shares"] * data["Current Price"]

    # Uses arithmetic expressions to calculate gain or loss. Section 2.4
    data["GainLoss"] = data["Value"] - data["Cost"]

    # Uses arithmetic expressions to calculate return percentage. Section 2.4
    data["ReturnPercent"] = data["GainLoss"] / data["Cost"] * 100

    # Uses pandas sum method to calculate total portfolio cost.
    totalCost = data["Cost"].sum()

    # Uses pandas sum method to calculate total portfolio value.
    totalValue = data["Value"].sum()

    # Uses pandas sum method to calculate total portfolio gain or loss.
    totalGainLoss = data["GainLoss"].sum()

    # Uses pandas groupby method to summarize results by sector.
    sectorSummary = data.groupby("Sector")[["Cost", "Value", "GainLoss"]].sum()

    # Uses pandas sort_values method to sort the sector summary.
    sectorSummary = sectorSummary.sort_values("Value", ascending=False)

    print()
    print("Cleaned Portfolio Data")
    print(data.to_string(index=False))

    print()
    print("Portfolio Totals")
    print("Total cost: $", round(totalCost, 2), sep="")
    print("Total value: $", round(totalValue, 2), sep="")
    print("Total gain or loss: $", round(totalGainLoss, 2), sep="")

    # Uses an if-else statement to describe portfolio performance. Section 3.3
    if totalGainLoss >= 0:
        print("Portfolio status: The portfolio has a gain.")
    else:
        print("Portfolio status: The portfolio has a loss.")

    print()
    print("Sector Summary")
    print(sectorSummary.to_string())

# Uses an if statement to run main only when this file is run directly. Section 3.3
if __name__ == "__main__":
    main()