seconds = 144229

minutes = 144229 / 60

seconds = seconds%60

print("Minutes:   " + str(int(minutes)) + "     Seconds:   " + str(seconds))

years_in_days = 2000000000 / 365.25
days_left = 2000000000 % 365.25
print(int(years_in_days) , days_left)