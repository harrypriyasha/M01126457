"""
RECORD CHECK  -  my version
===========================

Name  : Priyasha Harry
Lane  :  AI      
Date  : 02/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""asking the user for inputs, then calculating and presenting the values, difference and percentage"""

label = input('Please enter your name: ')
first = float(input('Enter your first value: '))            #converting the input to float data type
second = float(input('Enter your second value: '))          #converting the input to float data type

#calculating the difference and percent using the variables first and second
difference = second - first
percent = (first/second) * 100



print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

#printing the different variables using f string to format them
print('  The first value : ',f"{first:>10}")
print('  The second value: ',f"{second:>10}")
print('  The difference  : ',f"{difference:>+10.2f}")
print('  The percentage  : ', f"{percent:>10.2f}", '%')

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
