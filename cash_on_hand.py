# Line 1 to line 15 is correct, please do not edit anything - Jiaxin
from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

   
    cash_on_hand = [] 

    for row in reader:
        cash_on_hand.append([row[0], row[1]])


def coh_function(): 
    '''
    This function does not accepts any parameter 
    This function will calculate the difference in Cash-on-Hand 
    If the cash on hand on the current day is lower than the previous day, this function will print cash deficit on the current day and the difference in cash on hand.
    If the cash on hand on the current day is higher than the previous day, the cash on each day will be higher than the previous day.
    '''

    # Assigning True to a variable called everyday_coh to check if everyday no deficit is true or false
    everyday_nodeficit= True
    # Creating an empty list to store the final statement 
    statement= []
    for index in range(1, len(cash_on_hand)):
    # The previous cash on hand is extracted from the cash_on_hand list using the current loop's index-1 and converted to integer 
        previous_coh= int(cash_on_hand[index-1][1])
    # The current cash on hand is extracted from the cash_on_hand list and converted into an integer 
        current_coh= int(cash_on_hand[index][1])
        diff= current_coh - previous_coh

        if diff < 0:
    # False will be assigned to everyday_nodeficit
            everyday_nodeficit= False
    # A cash deficit statement with the day and amount of cash deficit will be appended into the statement list
            statement.append(f"[CASH DEFICIT]:DAY {(cash_on_hand[index][0])}, AMOUNT: USD {-(diff)}")
        
# If everyday_nodeficit is True which means none of the loop satisfied the condition of diff < 0        
    if everyday_nodeficit == True:
        statement.append(f"CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
# the items in the statement list will be returned after the end of all the for loops 
    return statement 
# The function is assigned to a variable called summary
summary= coh_function()


# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"
file_path.touch()

# Open the file in file_path using .open and "a" to append text in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
# A for loop is created to ensure that each item in the statement list is printed on a different line
    for item in summary:
        file.write(f'{item}\n')


        
















