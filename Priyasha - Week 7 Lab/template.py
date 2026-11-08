"""
RECORD CHECK  -  my version
===========================

Name  : Priyasha Harry
Lane  :  AI 
Date  : 07/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """Cleans a line and returns a dictionary"""

    #removing spaces from the whole string
    raw_line = raw_line.strip()

    #splitting the survey name from the remaining string
    survey_part, rest = raw_line.split(',', 1)

    #cleaning the survey name
    survey_part = survey_part.strip().lower()

    #creating an empty dictionary
    fields = {}

    #extracting the key and value
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = float(value.strip())

    #creating the final dictionary
    fields = {
        "survey": survey_part,
        "rating": fields["rating"],
        "age": fields["age"]
    }

    return fields


def status_of(rating, age):
    """Returns a status based on the survey rating"""

    #checking the rating
    if rating <= 2:
        return "FLAGGED"
    else:
        return "OK"
    


raw_records = []   

try:
    #opening the file and reading it line by line
    with open('records.txt', 'r')as f:
        for line in f:
            raw_records.append(line)        #appending the list 
except FileNotFoundError:
    print('File not found')


#initialising the count to 0
count = 0

for raw_record in raw_records:
    try:   
        #calling the parse_line funvtion for each record
        result = parse_line(raw_record)
        
        #calling the status_of function using the rating and age from result
        status = status_of(result['rating'], result['age'])

        print(result,status)
        
        if status == 'FLAGGED':     #checking if the status is equal Flagged
            count += 1              #incrementing the count
    except ValueError:
        #alternative text incase line could not be parsed
        ('Could not parse', raw_record)

#printing one line summary of the number of records and the number of them flagged       
print('Number of records: ', len(raw_records), '&', 'Count of flagged: ', count)  
    


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
