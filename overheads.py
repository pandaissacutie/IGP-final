from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

   
    overheads = [] 

    for row in reader:
        overheads.append([row[0], row[1]])

def overheads_function():
    '''
    This function does not accepts any parameter 
    This function will identify the highest overhead
    '''

    percentage_of_overheads= []
    statement= []
    for data in overheads:
        percentage_of_overheads.append(float(data[1]))
        highest_overheads_percentage = max(percentage_of_overheads)
        if float(data[1]) == highest_overheads_percentage:
           statement.append(f'[HIGHEST OVERHEADS] {data[0]}: {highest_overheads_percentage}%')
    return statement 

summary = overheads_function()

# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"


# Open the file in file_path using .open to write in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
    for item in summary:
        file.write(f'{item}\n')






    

