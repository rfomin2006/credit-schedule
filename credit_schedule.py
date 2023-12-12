import datetime as dt
from prettytable import PrettyTable

def validate(amount, percent, time, date):
    try:
        if type(amount) == bool:
            return "Amount must be a number"
        float(amount)
        if amount < 0:
            return "Amount must be greater than zero"
    except ValueError:
        return "Amount must be a number"
    except TypeError:
        return "Amount must be a number"
    try:
        if type(percent) == bool:
            return "Percent must be a number"
        float(percent)
        if percent < 0:
            return "Percent must be greater than zero"
    except ValueError:
        return "Percent must be a number"
    except TypeError:
        return "Percent must be a number"
    try:
        if type(time) == bool:
            return "Time must be a number"
        int(time)
        if time < 0:
            return "Time must be greater then zero"
    except ValueError:
        return "Time must be a number"
    except TypeError:
        return "Time must be a number"
    try:
        date = dt.datetime.strptime(date, "%d-%m-%Y")
    except:
        return "Invalid date"
    return True

def credit_schedule(amount, percent, time, date):
    validation = validate(amount, percent, time, date)
    if validation == True:
        date = dt.datetime.strptime(date, "%d-%m-%Y")
        remainder = amount
        data = []
        for month in range(time):
            overpayment = round((remainder/percent)/12, 2)
            payment = round(amount/time, 2)
            fee = round(payment + overpayment, 2)
            remainder = round(remainder - payment, 2)
            date += dt.timedelta(days=30)
            if remainder < 0.05:
                remainder = 0
            data.append({"date": dt.datetime.strftime(date, "%d-%m-%Y"), "overpayment": overpayment, "payment": payment, "fee": fee, "remainder": remainder})
    else:
        return validation
    return data

def table_view(data):
    table = PrettyTable()
    table.field_names = list(data[0].keys())
    for element in data:
        table.add_row(element.values())

    return table

print(credit_schedule(10, 10000, "01-01-2000", 10))
# print(table_view(credit_schedule(5000000, 10, 120, '02-01-2000')))
