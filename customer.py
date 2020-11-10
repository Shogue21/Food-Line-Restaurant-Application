from datetime import date
import random
import sqlite3

time_choices = ["4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00"]

con = sqlite3.connect('restaraunt_1.db')
cur = con.cursor()

def random_date():
    start_dt = date.today().toordinal()
    end_dt = date(2020, 12, 31).toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day

def choose_times():
    random_times = random.choices(time_choices)
    return random_times

print("Welcome to Food Line! Home to all your restaraunt needs!")
choice = input('''Would you like to:
- Make a [reservation]
- Order [carry-out]
- Schedule a [delivery]
''')
if choice == "reservation":
    name = input("What is the name for this order?\n")
    count = input("What is the size of your party?\n")
    print('Here are our available dates and times.')

    dates = {}
    for i in range(10):
        dates["Date %s" %i] = random_date()
    for key in dates:
        print(dates[key])

    chosen_date = input("What date would you like to schedule for?\n")
    split_dates = chosen_date.split("-")
    chosen_date = date(int(split_dates[0]), int(split_dates[1]), int(split_dates[2]))

    print("Here are available times.")
    if chosen_date in dates.values():
        times = {}
        for i in range(6):
            times["Time %s" %i] = choose_times()
        for key in times:
            print(times[key])

    chosen_time = input("What time would you like to schedule for?\n")
    cur.execute('INSERT INTO Reservations VALUES (?, ?, ?, ?, ?)', (name, count, chosen_date, chosen_time, None))
    con.commit()