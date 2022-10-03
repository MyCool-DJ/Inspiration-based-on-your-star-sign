#day 8 of 100 days of code
print("Hi, I am your AI Lilly, I want to give you some inspiration!")
name = input("Let's start with your name, type your name here: ")
starSign = input("Ok, what is your star sign? ")
day = input("And what day is it where you are today? ")
print("")
if (starSign == "Aries" or starSign == "aries") and (day == "Monday" or day == "monday"):
		print("Oh no, a Monday!", "Well,", name, "the, main thing is your wicked sense of humur can get your through this am I right? I know I am right!")
elif (starSign == "Aries" or starSign == "aries") and (day == "Tuesday" or day == "tuesday"):
	print("Forever Tuesday, am I right? Keep up your sense of humor,", name ,"and you will be just fine!")
elif (starSign == "Aries" or starSign == "aries") and (day != "Monday" or "monday" or "Tuesday" or "tuesday"):
	print("Oh no, it's a", day)
	
elif starSign == "Taurus" or starSign == "taurus": 
	print("As a Taurus, ", name , "you are brave and you know it!")
elif starSign == "Gemini" or starSign == "gemini": 
	print("As a Gemini, ", name , "you are a boss and you know it!")
elif starSign == "Cancer" or starSign == "cancer": 
	print("As a Cancer, ", name , "you are determined and you know it!")
elif starSign == "Leo" or starSign == "leo": 
	print("As a Leo,", name , "you are strong like a Lion!")
elif starSign == "Virgo" or starSign == "virgo": 
	print("As a Virgo, ", name , "you are clever and you know it!")
elif starSign == "Libra" or starSign == "libra": 
	print(day, "ha I see. As a Libra,", name , "don't forget how strong you are and you know it!")
elif starSign == "Scorpio" or starSign == "scorpio": 
	print(day, "ha I see. As a Scorpio,", name , "don't forget how resourceful you are, and you know it!")
elif starSign == "Sagittarius" or starSign == "sagittarius":
	print(day, "ha, I see. As a Sagittarius,", name , "don't forget how cool you are, and you know it!")
elif starSign == "Capricorn" or starSign == "Capricorn": 
	print(day, "ha I see. As an Aquarius,", name , "don't forget how good-looking you are!")
elif starSign == "Aquarius" or starSign == "aquarius": 
	print(day, "ha I see. As an Aquarius,", name , "don't forget how good-looking you are!")
elif starSign == "Pisces" or starSign == "pisces": 
	print(day, "ha I see. As a Pisces,", name , "you know how to start a party!")
else:
	print("Your entry did not compute, please try again", name)