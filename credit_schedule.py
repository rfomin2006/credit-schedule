import datetime as dt
from prettytable import PrettyTable

def validate(amount, percent, time, date):
    try:
        float(amount)
        if amount < 0:
            return "Amount must be greater than zero"
    except TypeError:
        return "Amount must be a number"
    try:
        float(percent)
        if percent < 0:
            return "Percent must be greater than zero"
    except TypeError:
        return "Percent must be a number"
    try:
        int(time)
        if time < 0:
            return "Time must be greater then zero"
    except TypeError:
        return "Time must be a number"
    try:
        date = dt.datetime.strptime(date, "%d-%m-%Y")
    except:
        return "Invalid date"
    return True

def credit_schedule(amount, percent, time, date):
    date = dt.datetime.strptime(date, "%d-%m-%Y")
    remainder = amount
    data = []
    for month in range(time+1):
        overpayment = (amount/percent)/12
        payment = amount/time
        fee = payment + overpayment
        remainder -= payment
        date += dt.timedelta(days=30)
        data.append({"date": dt.datetime.strftime(date, "%d-%m-%Y"), "overpayment": overpayment, "payment": payment, "fee": fee, "remainder": remainder})

    return data


