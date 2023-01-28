from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

   
    netprofit = [] 

    for row in reader:
        netprofit.append([row[0], row[4]])

def profitloss_function():
    '''
    This function does not accepts any parameter 
    This function will calculate the difference in Net profit 
    If the current Net profit is lower than the previous day, this function will print profit deficit on the current day and the difference in net profit.
    If the Net profit on the current day is higher than the previous day, the net profit on each day will be higher than the previous day.
    '''
    # Assigning True to a variable called everyday_surplus to check if everyday surplus is true or false
    everyday_surplus= True
    # Creating an empty list to store the final statement 
    statement= []
     # A for loop is created to loop index of the net profits in the list stored by a variable called netprofit from the second profit in the list to the last profit in the list
    for index in range(1, len(netprofit)):
    # The previous net profit is extracted from the netprofit list using the current loop's index-1 and converted to integer 
        previous_netprofit= int(netprofit[index-1][1])
    # The current net profit is extracted from the netprofit list and converted into an integer 
        current_netprofit= int(netprofit[index][1])
       # Difference between the current and previous net profit is calculated by substracting previous_netprofit from current_netprofit and stored in a variable called diff
        diff= current_netprofit - previous_netprofit
        
    # If at any loop, diff is less than zero
        if diff < 0:
    # False will be assigned to everyday_surplus
            everyday_surplus = False
    # A profit deficit statement with the day and amount of profit deficit will be appended into the statement list
            statement.append(f"[PROFIT DEFICIT]:DAY {int(netprofit[index][0])}, AMOUNT: USD {-(diff)}")
    # If everyday_surplus is True which means none of the loop satisfied the condition of diff < 0 
    if everyday_surplus == True:
    # A net profit surplus statement will be appended into the statement list
        statement.append(f"[NET PROFIT SURPLUS] NET PROFIT IN EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    # the items in the statement list will be returned after the end of all the for loops 
    return statement

# The function is assigned to a variable called summary
summary = profitloss_function()

# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"

# Open the file in file_path using .open and "a" to append text in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
# A for loop is created to ensure that each item in the statement list is printed on a different line
    for item in summary:
        file.write(f'{item}\n')




