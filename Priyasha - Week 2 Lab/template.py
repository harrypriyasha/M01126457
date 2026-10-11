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



label = input("Please enter your label: ")   
count = 0

while label!= 'quit':
    
    value = float(input('Please enter your value: '))     
    limit = float(input("Please enter the limit: "))    



    difference = limit - value        
    percent = (value/limit) * 100       

    status = 'empty' 

    if percent >= 100:
       status ='OVER LIMIT'
    elif percent >= 90 and percent < 100:         
       status ='WARNING'
    else:
        status ='OK'


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print('  Used        : ',f"{value:>10.2f}")
    print('  Total       : ',f"{limit:>10.2f}")
    print('  Free        : ',f"{difference:>10.2f}")
    print('  Percent     : ', f"{percent:>10.2f}", '%')
    print('  Status      : ', f"{status:>10}")


    print("=" * 34)
    
    if status == 'OVER LIMIT':                           #to count how many over limit status there is while the loop runs
            count += 1
            
    label = input("Please enter your label: ")          #to let the user enter their next label
            
print('The count of over limit is:',count) 


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
