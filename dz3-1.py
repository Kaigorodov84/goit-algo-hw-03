import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today():
    try:
        user_input = input('Введіть дату у форматі РРРР-ММ-ДД: ') #ввод дати
        user_date = dtdt.strptime(user_input, '%Y-%m-%d')    
        current_date = dtdt.today()   #поточна дата   
        print((current_date - user_date).days)  #різниця дати
    except Exception:
        print('Введіть коректну дату')

get_days_from_today()
