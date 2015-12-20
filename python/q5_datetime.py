# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

# convert dates into datetime format
date_start = datetime.strptime(date_start, '%m-%d-%Y')
date_stop = datetime.strptime(date_stop, '%m-%d-%Y')

print ("Date difference in days = ", (date_stop-date_start).days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime.strptime(date_start, '%m%d%Y')
date_stop = datetime.strptime(date_stop, '%m%d%Y')

print ("Date difference in days = ", (date_stop-date_start).days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start = datetime.strptime(date_start, '%d-%b-%Y')
date_stop = datetime.strptime(date_stop, '%d-%b-%Y')

print ("Date difference in days = ", (date_stop-date_start).days)
