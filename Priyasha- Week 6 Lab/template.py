"""
RECORD CHECK  -  my version
===========================

Name  : Priyasha Harry
Lane  :  AI
Date  : 02/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

#opening the file
df = pd.read_csv("template_records.csv")

#calculating the percentage
df['percent'] = (df['value'] / df['limit']) * 100

#creating the status column
df['status'] = df['percent'].apply(
    lambda p: 'OVER LIMIT' if p >= 100 else 'WARNING' if p>=90 else 'OK')


#======================================================

#keeping records with status that is not OK
filtered = df[df['status'] != 'OK']

#grouping the data by status and counting the values
print(df.groupby('status').size())

#saving the data frame
df.to_csv('template_report.csv', index = False)


import matplotlib.pyplot as plt

#creating a bar graph using status
df["status"].value_counts().plot(kind="bar")

#setting title of the graph
plt.title('Count of Different Status')

#saving the graph
plt.savefig(('template_status_graph.png'))

plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case

