# Problem:
# Create an area code identifier app.

# Variables
which = input("Would you like to look up a city or zip code? ")


# Logic
# Function
def main():

    while True:
        area_codes = {
            "206": {"Seattle, WA"},
            "253": {"Tacoma - Federal Way - Auburn, Washington"},
            "360": {"Seattle Metro Area - Olympia, Bellingham, Vancouver, Washington"},
            "425": {"East Seattle - Everett - Bellevue, Washington"},
            "564": {"Western, Washington"}
        }

        cities = {
            "Seattle, WA": {"206"},
            "Tacoma": {"253"},
            "Federal Way": {"253"},
            "Auburn": {"253"},
            "Seattle Metro Area": {"369"},
            "Olympia": {"369"},
            "Bellingham": {"369"},
            "Vancouver": {"369"},
            "East Seattle": {"425"},
            "Everett": {"425"},
            "Bellevue": {"425"},
            "Western Washington": {"564"},
        }

        code = input("What is your area code? ")
        if code == "206":
            print(area_codes["206"])
        else:
            print("Please enter a valid area code for Washington State.")
        answer = input("Would you like to enter another area code? ")
        if answer != "y":
            break

main()

