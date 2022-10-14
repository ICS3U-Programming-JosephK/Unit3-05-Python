#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 13 2022
# This program asks the user for the month as a number
# between 1 and 12. It then displays the month as a
# string to the user.

# This function will return the moment in string format
# for the given month. It is the Switch-Case equivalent
def find_month(month):
    months = {
        1: "{} represents January.".format(month),
        2: "{} represents February.".format(month),
        3: "{} represents March.".format(month),
        4: "{} represents April.".format(month),
        5: "{} represents May.".format(month),
        6: "{} represents June.".format(month),
        7: "{} represents July.".format(month),
        8: "{} represents August.".format(month),
        9: "{} represents September.".format(month),
        10: "{} represents October.".format(month),
        11: "{} represents November.".format(month),
        12: "{} represents December.".format(month),
    }
    # Similar to an else statement, in case all previous cases were false
    return months.get(month, "Error. {} does not represent a month.".format(month))


if __name__ == "__main__":
    # Ask the user for the number from 1-12
    user_month = int(input("Enter the number for a month i.e. 2 for February: "))
    print(find_month(user_month))
