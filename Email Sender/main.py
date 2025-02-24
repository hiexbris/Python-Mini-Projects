import smtplib
import datetime as dt
import random

my_email = 'hiexbris@gmail.com'
password = 'nhhclhppxxtofibw'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    with open('quotes.txt', 'r') as quotes:
        all_quotes = quotes.readlines()
        quotes_1 = random.choice(all_quotes)
        connection.sendmail(from_addr=my_email, to_addrs='hellojiaditya@gmail.com',
                            msg=f"Subject:Quote of the Day \n\n{quotes_1}")
    connection.close()

