import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
        date = dtdt.strptime(date, '%Y-%m-%d')   #ввод дати  
        current_date = dtdt.today()   #поточна дата   
        return(current_date - date).days  #різниця дати
    except Exception:
        print('Введіть коректну дату')

print (get_days_from_today("2021-10-09"))
