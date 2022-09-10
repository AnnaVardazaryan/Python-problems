import validators
import datetime


def valid_email(my_email):
    if validators.email(my_email):
        return True
    return False


def valid_url(my_url):
    if validators.url(my_url):
        return True
    return False


def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        return False


def valid_number(num):
    try:
        complex(num)
        return True
    except:
        return False


def valid_card_number(num):
    if len(num) < 8 or len(num) > 19:
        return False
    for i in num:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True


def valid_phone_number(num):
    if num[:4] == '+374' and len(num) == 12 and num[4:].isnumeric() or num[0] == '0' and len(num) == 9 and num[1:].isnumeric() :
        return True
    return False


data = input("Validate:")
data_list = data.split(':')
if data_list[0] == "Email":
    print(valid_email(data_list[1]))
elif data_list[0] == "Website URL":
    print(valid_url(data_list[1]))
elif data_list[0] == "Date":
    print(valid_date(data_list[1]))
elif data_list[0] == "Number":
    print(valid_number(data_list[1]))
elif data_list[0] == "Credit Card Number":
    print(valid_card_number(data_list[1]))
elif data_list[0] == "Mobile Phone Number":
    print(valid_phone_number(data_list[1]))
