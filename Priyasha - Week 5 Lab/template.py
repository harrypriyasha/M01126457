"""
RECORD CHECK  -  my version
===========================

Name  :  Priyasha Harry
Lane  :  AI 
Date  :  24/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

"""creating a class and storing all the parameters as attributes"""
class Record:
    over_limit_count = 0
    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit
        
    def status(self):
        """creating a method that calculates the percentage and returns the status"""
        percent = ((self.value/self.limit)*100)         #calculating the percentage from self.value and self.limit
        if percent >= 100:
            return 'OVER LIMIT'
            self.over_limit_count += 1          #incrementing the count 
        elif percent >= 90:
            return 'WARNING'
        else:
            return 'OK'
        
        

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

"""creating Records.txt file to store the records"""
with open('Records.txt', 'w')as f:
    f.write("R-01, 87.0, 100.0\n")
    f.write("R-02, 95.0, 100.0\n")
    f.write("R-03, 121.0, 100.0\n")
    f.write("R-04, 54.0, 100.0\n")
    
def load_records(path):
    """reads records from a file and returns a list of Record objects"""
    new=[]              #new list to store the records
    try: 
        with open(path)as r:
            for line in r:
                label, value, limit = line.strip().split(',')  
                record = Record(label, float(value), float(limit))
                new.append(record)
        return new
    except FileNotFoundError:
        print('File was not found')
        
records = load_records('Records.txt')

"""looping through the records and printing the status of each"""
for record in records:
    print(record.status())
        

    
# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Label:  {record.label:>10}")
    print(f"  Value:  {record.value:>10.2f}")
    print(f"  Limit:  {record.limit:>10.2f}")
    print(f"  Status: {record.status():>10}")

    if record.status() == "OVER LIMIT":
        over_limit_count += 1
        

    print("=" * 34)

print(f"The OVER LIMIT count is: {over_limit_count}")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
