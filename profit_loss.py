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
    everyday_surplus= True
    statement= []
    for index in range(1, len(netprofit)):
        previous_netprofit= int(netprofit[index-1][1])
        current_netprofit= int(netprofit[index][1])
        diff= current_netprofit - previous_netprofit

        if diff < 0:
            everyday_surplus = False
            statement.append(f"[PROFIT DEFICIT]:DAY {int(netprofit[index][0])}, AMOUNT: USD {-(diff)}")

    if everyday_surplus == True:
        statement.append(f"[NET PROFIT SURPLUS] NET PROFIT IN EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return statement

summary = profitloss_function()

# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"

# Open the file in file_path using .open to write in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
    for item in summary:
        file.write(f'{item}\n')




