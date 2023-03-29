import time

currentTime = time.strftime('%H:%M:%S')
print(currentTime)
currentTimeH = int(time.strftime('%H'))
if currentTimeH < 12:
    print("Good Morning")
elif currentTimeH > 12 or currentTimeH < 16:
    print("Good Afternoon")
elif currentTimeH > 16 or currentTimeH < 19:
    print("Good Evening")
else:
    print("Good Night")