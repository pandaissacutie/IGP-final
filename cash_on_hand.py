# Importing path from path library 
from pathlib import Path
# Importing csv file 
import csv

# Creating the file to a csv file
fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

# Read the csv file to append day and cash on hand and from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skip header
    next(reader) 

# Creating an empty list to store day and cash on hand
    cash_on_hand = [] 
    
# Append day and cash on hand as a list back to each empty list
    for row in reader:
        cash_on_hand.append([row[0], row[1]])

# Creating a function called coh_function
def coh_function(): 
    '''
    This function does not accepts any parameter 
    This function will calculate the difference in Cash-on-Hand and check whether everyday no deficit is true or false
    If the cash on hand on the current day is lower than the previous day (everyday no deficit is False), this function will return cash deficit on the current day and the difference in cash on hand.
    If all the cash on hand on the current day is higher than the previous day (everyday deficit is True), the cash on each day will be higher than the previous day.
    '''

    # Assigning True to a variable called everyday_nodeficit to check whether it is true or false
    everyday_nodeficit= True
    
    # Creating an empty list to store the final statement 
    statement= []
    
    # A for loop is created to loop the position of each nested list of the cash on hand list from a range of 1 to len(Cash_on_hand)
    for index in range(1, len(cash_on_hand)):
    # The previous cash on hand is extracted from the cash_on_hand list using the current loop's index-1 and converted to an integer 
        previous_coh= int(cash_on_hand[index-1][1])
    # The current cash on hand is extracted from the cash_on_hand list and converted into an integer 
        current_coh= int(cash_on_hand[index][1]) 
    # To calculate the variable called diff, previous cash on hand is deducted from current cash on hand  
        diff= current_coh - previous_coh
        
    # If diff is less than zero, there is deficit a on that day
        if diff < 0:
    # False will be assigned to everyday_nodeficit if diff < 0
            everyday_nodeficit= False
        
    # A cash deficit statement with the day and amount of cash deficit will be appended into the statement list
            statement.append(f"[CASH DEFICIT] DAY: {(cash_on_hand[index][0])}, AMOUNT: USD {-(diff)}")
        
# If everyday_nodeficit is True, it would mean that none of the loop satisfied the condition of diff < 0        
    if everyday_nodeficit == True:      
# The statement will be appended into the statement list
        statement.append(f"CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    
# The items in the statement list will be returned after the end of all the for loops 
    return statement 

# The function is assigned to a variable called summary
summary= coh_function()


# Import Path method from Path Library
from pathlib import Path

# Assigning the summary report text file path to a variable called file path
file_path = Path.cwd()/"summary_report.txt"

# Open the file in file_path using .open and "a" to append text in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
    
# A for loop is created to ensure that each item in the statement list is printed on a different line
    for item in summary:
        file.write(f'{item}\n')


        
















