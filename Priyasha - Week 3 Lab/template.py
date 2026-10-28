"""
RECORD CHECK  -  my version
===========================

Name  : Priyasha Harry
Lane  :  AI     (delete two)
Date  : 9/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

def status_of(percent):
    """Finds the status of the percentage entered"""
    if percent >= 100:
        status = 'OVER LIMIT'
    elif percent >= 90:
        status = 'WARNING'
    else:
        status = 'OK'
    return status
    
def check(value,limit):
    """Calculates the difference and percentage based of the value and limit"""
    difference = limit - value
    percentage = (value/limit)*100
    return difference, percentage

def print_report(label,value, limit, difference,percent, status):
    """"Prints all the variables"""
    print('Label        : ',f"{label:>10}")
    print('Used         : ',f"{value:>10.2f}")
    print('Total        : ',f"{limit:>10.2f}")
    print('Difference   : ', f"{difference:>10.2f}"),
    print('Percent      : ', f"{percent:>10.2f}", '%')
    print('Status       : ', f"{status:>10}")


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

#asking user to input label 
label = input("Please enter your label: ")  
count = 0                                           #initialise count to 0


#loop to calculate multiple records until quit is entered
while label != 'quit':                                 
    value = float(input('Please enter your value: '))     
    limit = float(input("Please enter the limit: "))   


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.


    difference, percent = check(value,limit)            #assigning the output of the check funtion to variables, difference and percent
    status = status_of(percent)                         #assining the output of the status_of function to variable status

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    #calling the print_report function
    print_report(label,value, limit, difference, percent, status)

    print("=" * 34)
    
    
    if status == 'OVER LIMIT':                           #to count how many over limit status there is while the loop runs
        count += 1
        
    label = input("Please enter your label: ")          #to let the user enter their next label
        
print('The count of over limit is:',count)              #to print the count of OVER LIMIT


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
