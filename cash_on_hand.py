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

    # T
    everyday_coh= True
    statement= []

    for index in range(1, len(cash_on_hand)):
        previous_coh= int(cash_on_hand[index-1][1])
        current_coh= int(cash_on_hand[index][1])
        diff= current_coh - previous_coh
        if diff < 0:
            everyday_coh= False
            statement.append(f"[CASH DEFICIT]:DAY {(cash_on_hand[index][0])}, AMOUNT: USD {-(diff)}")
        
    if everyday_coh == True:
        statement.append(f"CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    return statement 

summary= coh_function()
print(summary)

# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"
file_path.touch()

# Open the file in file_path using .open to write in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
    for item in summary:
        file.write(f'{item}\n')


        
















