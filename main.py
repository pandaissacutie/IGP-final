# Modularizing the program
# Importing the 3 python file which contains the 3 functions
import overheads, cash_on_hand, profit_loss

# Creating a function called main to combine all the 3 functions
def main():
    '''
    This function will find the highest overhead category and percentage
    This function will compute the difference in the cash on hand on the current day and previous day and identify whether there is a surplus or deficit
    This function will compute the difference in the net profit on the current day and previous day and identify whether there is a surplus or deficit
    The summary will be written into a text file called summary_report.txt
    '''
    overheads.overheads_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()

main()


# Creating a text file for team member's details
from pathlib import Path
team_members= Path.cwd()/"team_members.txt"
team_members.touch()

with team_members.open(mode="w", encoding= "UTF-8") as file:
    file.write("Lin Jiaxin S10244320\nCheng Shao Loong Malcolm S10221126\nNatalie Koh Qian Hui S10242431\nNor Alysha Angullia Mohamed Rashid S10220971\nNur Elrina Ramdan S10247530")






