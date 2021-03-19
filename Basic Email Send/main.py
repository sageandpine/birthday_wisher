import datetime as dt
import smtplib
import random

MY_EMAIL = "ghost_paste@yahoo.com"
MY_PASSWORD = "aemcdmddeuchdarm"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", "r") as data:
        quote_list = data.readlines()
        todays_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="sage.pina@gmail.com",
                            msg=f"Subject: Inspiration from ghost_paste!!\n\n Get ready for a new day!\n{todays_quote}\nBe well!\n\n\t\t***ghost_paste***")

#make_list from txt file
# check for day of week
# if check matches
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# day_of_week
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)











# import smtplib
#
# my_email = "ghost_paste@yahoo.com"
# password = "aemcdmddeuchdarm"
#
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     # encrypts connection
#     connection.starttls()
#     # log in to provider
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="sage.pina@gmail.com", msg="Subject: Hola from ghosti3!!\n\n"
#                                                                                   "This is a reply to an earlier email!!"
#     )

