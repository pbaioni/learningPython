#you need datetime in order to manage dates
from datetime import date
from datetime import datetime

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print d1

# Textual month, day and year    
d2 = today.strftime("%B %d, %Y")
print d2

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print d3

# Month abbreviation, day and year    
d4 = today.strftime("%b-%d-%Y")
print d4


# datetime object containing current date and time
now = datetime.now()
print now

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print dt_string