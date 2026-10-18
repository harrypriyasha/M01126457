"""
RECORD CHECK  -  my version
===========================

Name  : Priyasha Harry
Lane  :  AI  (delete two)
Date  : 16/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def check_record(value,limit):
    """Calculates the difference and percentage based of the value and limit and returns the status"""
    difference = limit - value
    percentage = (value/limit)*100
    if percentage >= 100:
        status = 'OVER LIMIT'
    elif percentage >= 90:
        status = 'WARNING'
    else:
        status = 'OK'
    
    return difference, percentage, status

def print_report(label,value, limit, difference,percentage, status):
    """"Prints all the variables"""
    print('Label        : ',f"{label:>10}")
    print('Used         : ',f"{value:>10.2f}")
    print('Total        : ',f"{limit:>10.2f}")
    print('Difference   : ', f"{difference:>10.2f}"),
    print('Percent      : ', f"{percentage:>10.2f} %")
    print('Status       : ', f"{status:>10}")


  
with open('new_file.txt', 'w')as f:     # creating and writing into a new file
    f.write('R-01,54,100\n')
    f.write('R-02,86,100\n')
    f.write('R-03,110,100\n')
    f.write('R-04,20,100\n')

def load_records(path):
    """Reads label,value,limit from a file and returns the list""" 
    try:
        with open(path) as f:
            new = []                #empty list to add the dictonary values
            for line in f:
                label, value, limit = line.strip().split(',')   #seperating the line into label, value, limit
                new.append({'label': label,                     #appending the values to the dictionary
                            'value': value,
                            'limit': limit,
                             })
            return new          #stores the data
    except FileNotFoundError:
        print('The file was not found')
        return []     
    
count = 0                               #initialise the count to 0 
records = load_records('new_file.txt')   

with open('temp_results.txt','w')as f:
    for record in records:              #looping through the records in the file
        label = record['label']         
        value =int(record['value'])
        limit = int(record['limit'])
       
        difference,percentage,status = check_record(value,limit)        #calling check records function and storing the data in variables
       
        f.write(f"{label}, {status}\n")         #writing the data to the results file
       
        print_report(label,value, limit, difference,percentage, status)
       
        if status == 'OVER LIMIT':
            count =+ 1
       
        print()
           
    
print(f"The count of OVER LIMIT is: {count}")

with open('temp_results.txt')as x:          
   print(x.read())
    
    



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
