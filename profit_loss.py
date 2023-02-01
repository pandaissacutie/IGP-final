# Importing path from path library 
from pathlib import Path
# Importing csv file 
import csv

# Creating the file to a csv file
fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

# Read the csv file to append day and net profit from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skip header
    next(reader) 

# Creating an empty list to store day and net profit 
    netprofit = [] 
# Append day and net profit as a list back to each empty list
    for row in reader:
        netprofit.append([row[0], row[4]])

# Creating a function called profitloss_function()
def profitloss_function():
    '''
    This function does not accepts any parameter 
    This function will calculate the difference in Net profit and check whether everyday surplus is true or false
    If the current Net profit is lower than the previous day (everyday surplus is false), this function will return profit deficit on the current day and the difference in net profit.
    If  all the Net profit on the current day is higher than the previous day (everyday surplus is true), the net profit on each day will be higher than the previous day.
    '''
    # Assigning True to a variable called everyday_surplus to check if everyday surplus is true or false
    everyday_surplus= True
    
    # Creating an empty list to store the final statement 
    statement= []
    
     # A for loop is created to loop the position of each nested list in the net profit list from a range of 1 to len(Cash_on_hand)
    for index in range(1, len(netprofit)):
    # The previous net profit is extracted from the netprofit list using the current loop's index-1 and converted to integer 
        previous_netprofit= int(netprofit[index-1][1])
    # The current net profit is extracted from the netprofit list and converted into an integer 
        current_netprofit= int(netprofit[index][1])
    # To calculate the variable called diff, previous net profit is deducted from current net profit
        diff= current_netprofit - previous_netprofit
        
    # If diff is less than zero, there is a deficit on that day
        if diff < 0:
    # False will be assigned to everyday_surplus if diff < 0
            everyday_surplus = False
    # A profit deficit statement with the day and amount of profit deficit will be appended into the statement list
            statement.append(f"[PROFIT DEFICIT] DAY: {int(netprofit[index][0])}, AMOUNT: USD {-(diff)}")
        
    # If everyday_surplus is True, it would mean that none of the loops satisfied the condition of diff < 0 
    if everyday_surplus == True:
    # A net profit surplus statement will be appended into the statement list
        statement.append(f"[NET PROFIT SURPLUS] NET PROFIT IN EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        
    # The items in the statement list will be returned after the end of all the for loops 
    return statement

# The function is assigned to a variable called summary
summary = profitloss_function()


# Import Path method from Path Library
from pathlib import Path

# Assigning the summary report text file path to a variable called file path
file_path = Path.cwd()/"summary_report.txt"

# Open the file in file_path using .open and "a" to append text in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
# A for loop is created to ensure that each item in the statement list is printed on a different line
    for item in summary:
        file.write(f'{item}\n')




