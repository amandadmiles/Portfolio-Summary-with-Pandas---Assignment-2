"""
Program: portfolio_summary.py
Author: Amanda Miles
 
Purpose: This program demonstrates basic pandas library functions by reading
a sample investment portfolio from a CSV file, cleaning the data, calculating
cost, value, gain or loss, and summarizing the portfolio by sector.
 
Built-in Python functions and concepts used:
1. input() - Used to ask the user for the CSV file name. This function is used
for terminal input and is discussed in Section 1.4, composing and running a
simple Python program.
 
2. print() - Used to display the portfolio report in the terminal. This function
is used for terminal output and is discussed in Section 1.4, composing and
running a simple Python program.
 
3. round() - Used to round money totals to two decimal places. This function
relates to arithmetic expressions and numeric output discussed in Section 2.4,
Expressions.
 
4. Arithmetic operators (* - / +) - Used to calculate cost, current value,
gain or loss, and return percentage for each holding. Arithmetic operators
are discussed in Section 2.4, Expressions.
 
5. import statement - Used to import the pandas library as pd so its functions
can be called throughout the program. The import statement is discussed in
Section 2.5, Using Functions and Modules.
 
6. String literals - Used in print statements to display labeled output such as
"Original Portfolio Data" and "Portfolio Totals". String literals are discussed
in Section 2.2, Strings, Assignment, and Comments.
 
7. sep="" - Used as a parameter inside print() to prevent a space from being
inserted between the dollar sign and the numeric value. The sep parameter
relies on string behavior discussed in Section 2.2, Strings, Assignment,
and Comments.
 
8. True and False (Boolean values) - Used in the sort_values() call with
ascending=False to sort the sector summary from highest to lowest value.
Boolean values are discussed in Section 3.3, Selection: if and if-else
Statements.
 
9. String comparison using == - Used in the if __name__ == "__main__" check
to determine whether the file is being run directly. String comparison is
discussed in Section 3.3, Selection: if and if-else Statements.
 
10. Comparison operator >= - Used in the if-else statement to evaluate whether
the total gain or loss is zero or positive. Comparison operators are discussed
in Section 3.3, Selection: if and if-else Statements.
 
Pandas library functions and methods used:
1. pd.read_csv() - Used to read portfolio data from a CSV file into a DataFrame.
Reading data from a file connects to the concept of reading from text files
discussed in Section 4.5, Text Files.
 
2. drop_duplicates() - Used to remove repeated rows from the portfolio data so
that the same holding is not counted more than once in the calculations.
 
3. fillna() - Used to replace any missing values in the data with zero so that
calculations are not affected by empty cells.
 
4. groupby() - Used to group all holdings by their sector so that totals can
be calculated for each industry category.
 
5. sum() - Used to calculate the total cost, total value, and total gain or
loss across all holdings and within each sector group.
 
6. sort_values() - Used to sort the sector summary table from highest to lowest
current value. This is conceptually similar to sorting a list, which is
discussed in Section 5.1, Lists.
 
7. to_string() - Used to display the full DataFrame output in the terminal
without truncating any rows or columns.
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
 