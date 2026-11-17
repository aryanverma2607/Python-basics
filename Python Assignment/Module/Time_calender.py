import time

x = time.time()        #it returns timestamp represent total seconds from 1 jan 1970 to now
print(x)

print(time.ctime())
#it represent time(in Readable format) with day of week,month,day,time in hour:minute:second then year
print("Hello")
time.sleep(2)    #it pause time for a given second And after waiting for a second it generates the output
print("Aryan")
time.sleep(3)
print("Verma")

x=time.localtime() #it gives time in structured format
print(x)
#to access value from x
print(x.tm_year)
print(x.tm_mon)
print(x.tm_mday)
print(x.tm_hour)
print(x.tm_min)
print(x.tm_sec)

y=time.gmtime()     #gives time according toUTC time
print(y)

a=time.strftime(x,"%d-%-m-%Y")   # date/time ko formatted string mein convert karta hai
print(a)
b=time.strftime(x,"%H:%M:%s")
print(b)

z=time.strptime(x,"%d-%m-%Y")
print(zzz)