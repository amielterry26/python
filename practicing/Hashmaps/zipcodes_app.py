# Problem:
# Create an area code identifier app.

# Variables
# Logic
# Function

area_codes = {
    "206": {"Seattle, WA"},
    "253": {"Tacoma - Federal Way - Auburn, Washington"},
    "360": {"Seattle Metro Area - Olympia, Bellingham, Vancouver, Washington"},
    "425": {"East Seattle - Everett - Bellevue, Washington"},
    "564": {"Western, Washington"}
}

code = input("What is your area code? ")
if code == "206":
    print(area_codes["206"])
else:
    print("Please enter a valid area code for Washington State.")



