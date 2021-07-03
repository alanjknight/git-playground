from datetime import datetime

def alan(x, y="y", z="z"):
    print(x)
    print(y)
    print(z)


#alan("a","b","c")   

#print(bool(1))
#print(bool(0))

date_string = '32/6/21'
print(date_string)
print(type(date_string))

try:
    date_date = datetime.strptime(date_string,'%d/%m/%y')
    print(date_date)
    print(type(date_date))
except:
    print("Error")





