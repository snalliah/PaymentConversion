import datetime


now = datetime.datetime.now()

currentTime = now.hour  

if currentTime < 1 :
        greet = 'Good Morning!'
if currentTime >= 1 :
        greet = 'Good Afternoon!'
if currentTime > 18 :
        greet = 'Good Evening!'
  
print(greet)