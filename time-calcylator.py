pmam = 0
half = 0
daysofweek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

list = ["3:30 AM", "24:32", "Monday"]

split1 = list[0].split(":")
t1 = split1[1].split()

start_hour = str(split1[0])
start_min = str(t1[0])

split2 = list[1].split(":")
t2 = split2[1].split()

added_hour = str(split2[0])
added_min = str(t2[0])

split3 = list[0].split()
t3 = split3[1]

if t3 == "PM":
    half = half+0

elif t3 == "AM":
    half = half+1

else:
    print("Something is wrong! PMAM")

total_hour = (int((int(start_min)+int(added_min))/60) + int(start_hour) + int(added_hour))

day = int(total_hour)/24

final_hour = (int(total_hour)-(int(day)*24))

pmam = total_hour/12

if final_hour > 12:
    written_hour = final_hour-12
    pmam = pmam+1

else:
    written_hour = final_hour

if int(pmam) % 2 == 0:
    half = half + 0

else:
    half = half+1

if half % 2==0:
    final_pmam = "PM"

else:
    final_pmam = "AM"

total_min = (int((int(start_min)+int(added_min))))

min_hours = int(total_min)/60

final_min = (int(total_min)-(int(min_hours)*60))

t4 = int(int(start_hour)+int(added_hour))

if (int(day)) < 1 and t3 == "PM" and t4 >= 12:
    final_days = "(next day)"

elif day >= 1:
    final_days = f"({int(day)} days later)"

else:
    final_days = ""

if len(list) > 3:
    date = str(list[2]).lower()

    if date in daysofweek:
        if date == daysofweek[0]:
            final_day = ", Monday"

        elif date == daysofweek[1]:
            final_day = ", Tuesday"

        elif date == daysofweek[2]:
            final_day = ", Wednesday"

        elif date == daysofweek[3]:
            final_day = ". Thursday"

        elif date == daysofweek[4]:
            final_day = ", Friday"

        elif date == daysofweek[5]:
            final_day = ", Saturday"

        elif date == daysofweek[6]:
            final_day = ", Sunday"

else:
    final_day = ""

print(f"{written_hour}:{final_min} {final_pmam}{final_day} {final_days}")