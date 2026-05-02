"""
Program: portfolio_summary.py
Author: Amanda Miles
 
Purpose: This program demonstrates pandas library functions by reading
a sample investment portfolio from a CSV file, cleaning the data, calculating
cost, value, gain or loss, and summarizing the portfolio by sector.
 
Built-in Python functions and concepts used:
1. input() - Asks the user to type the CSV file name so the program knows
which file to open. (Section 1.4 Compose and run a simple Python program)
 
2. print() - Displays text and results in the terminal for the user to read.
(Section 1.4 Compose and run a simple Python program)
 
3. round() - Rounds dollar totals to two decimal places for clean output.
(Section 2.4 Expressions)
 
4. Arithmetic operators (* - / +) - Used to calculate cost, current value,
gain or loss, and return percentage for each holding.
(Section 2.4 Expressions)
 
5. import statement - Brings the pandas library into the program so its
tools are ready to use. The shortcut pd is assigned as a nickname so that
pd can be written instead of pandas throughout the code.
(Section 2.5 Using Functions and Modules)
 
6. String literals - Text in quotes used to label each section of output,
such as "Original Portfolio Data" and "Portfolio Totals".
(Section 2.2 Strings, Assignment, and Comments)
 
7. sep="" - Removes the automatic space that print() adds between items,
keeping the dollar sign and number together with no gap.
(Section 2.2 Strings, Assignment, and Comments)
 
8. True and False (Boolean values) - Used to control the sort direction,
where ascending=False tells the program to sort from highest to lowest.
(Section 3.3 Selection: if and if-else Statements)
 
9. String comparison using == - Checks whether the program is being run
directly, which determines whether the main function should be called.
(Section 3.3 Selection: if and if-else Statements)
 
10. Comparison operator >= - Checks whether the total gain or loss is zero
or greater to decide which status message to print.
(Section 3.3 Selection: if and if-else Statements)
 
Pandas library functions and methods used:
1. pd.read_csv() - Reads the CSV file and loads all the data into a table
the program can work with. (Section 4.5 Text Files)
 
2. drop_duplicates() - Scans the data and removes any rows that appear more
than once so no holding is counted twice.
 
3. fillna() - Finds any empty cells in the data and fills them with zero
so calculations are not affected.
 
4. groupby() - Groups all holdings together by sector so totals can be
calculated for each industry category.
 
5. sum() - Adds up the numbers in a column to produce a total, used for
cost, value, and gain or loss across the whole portfolio.
 
6. sort_values() - Sorts the sector summary from highest to lowest value,
similar to sorting a list. (Section 5.1 Lists)
 
7. to_string() - Displays the full table in the terminal without cutting
off any rows or columns.
"""
 
# Imports the pandas library so its functions can be used in the program (Section 2.5 Using Functions and Modules)
import pandas as pd
 
# Defines the main function for the program (Section 5.2 Defining Simple Functions)
def main():
    # Uses an assignment statement and input function to store the CSV file name (Sections 2.2 and 1.4)
    fileName = input("Enter the portfolio CSV file name: ")
 
    # Uses the pandas read_csv function to load portfolio data from a CSV file (Section 4.5 Text Files)
    data = pd.read_csv(fileName)
 
    # Uses print statements to display the original data (Section 1.4)
    print()
    print("Original Portfolio Data")
    print(data.to_string(index=False))
 
    # Uses the pandas drop_duplicates method to remove repeated rows
    data = data.drop_duplicates()
 
    # Uses the pandas fillna method to replace missing values with 0
    data = data.fillna(0)
 
    # Uses pandas DataFrame column access and an arithmetic expression to calculate cost (Section 2.4 Expressions)
    data["Cost"] = data["Shares"] * data["Purchase Price"]
 
    # Uses pandas DataFrame column access and an arithmetic expression to calculate current value (Section 2.4 Expressions)
    data["Value"] = data["Shares"] * data["Current Price"]
 
    # Uses pandas DataFrame column access and an arithmetic expression to calculate gain or loss (Section 2.4 Expressions)
    data["GainLoss"] = data["Value"] - data["Cost"]
 
    # Uses pandas DataFrame column access and an arithmetic expression to calculate return percentage (Section 2.4 Expressions)
    data["ReturnPercent"] = data["GainLoss"] / data["Cost"] * 100
 
    # Uses an assignment statement and pandas sum method to calculate total portfolio cost (Section 2.2)
    totalCost = data["Cost"].sum()
 
    # Uses an assignment statement and pandas sum method to calculate total portfolio value (Section 2.2)
    totalValue = data["Value"].sum()
 
    # Uses an assignment statement and pandas sum method to calculate total portfolio gain or loss (Section 2.2)
    totalGainLoss = data["GainLoss"].sum()
 
    # Uses the pandas groupby method and a list of column names to summarize results by sector (Section 5.1 Lists)
    sectorSummary = data.groupby("Sector")[["Cost", "Value", "GainLoss"]].sum()
 
    # Uses the pandas sort_values method to sort the sector summary by value
    sectorSummary = sectorSummary.sort_values("Value", ascending=False)
 
    # Uses print statements to display the cleaned data (Section 1.4)
    print()
    print("Cleaned Portfolio Data")
    print(data.to_string(index=False))
 
    # Uses print statements and round to display portfolio totals (Sections 1.4 and 2.4)
    print()
    print("Portfolio Totals")
    print("Total cost: $", round(totalCost, 2), sep="")
    print("Total value: $", round(totalValue, 2), sep="")
    print("Total gain or loss: $", round(totalGainLoss, 2), sep="")
 
    # Uses an if-else statement and >= comparison operator to describe overall portfolio performance (Section 3.3 Selection: if and if-else Statements)
    if totalGainLoss >= 0:
        print("Portfolio status: The portfolio has a gain.")
    else:
        print("Portfolio status: The portfolio has a loss.")
 
    # Uses print statements to display the sector summary (Section 1.4)
    print()
    print("Sector Summary")
    print(sectorSummary.to_string())
 
# Uses an equality check and calls the main function when this file is run directly (Sections 3.3 and 5.2)
if __name__ == "__main__":
    main()
 