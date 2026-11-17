'''
4. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply
'''
e=int(input("Soil Moisture = "))
f=int(input("Temperatur = "))
g=input("Crop Type(Wheat) = ").lower()

if e<=30:
	if f>=35:
		if g=="wheat":
			print("Irrigation = High Water Supply")
		else:
			print("Irrigation = Moderate Supply")
	else:
		print("Irrigation = Moderate Supply")
else:
	if e<=60:
		h=input("Rain Prediction(Yes/no)= ").lower()
		if h=="yes":
			print("Irrigation Status = Delay Irrigation")
		else:
			print("Irrigation Status = Light Irrigation")
	else:
		print("Irrigation Status = No Irrigation")			