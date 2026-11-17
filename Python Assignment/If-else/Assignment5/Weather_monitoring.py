'''6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert
'''

temperature=float(input("Enter Temperature:"))
humidity=int(input("Enter humidity:"))
if temperature>=30:
	print("Hot day")
if humidity>=70:
	print("High Humidity Alert")
	