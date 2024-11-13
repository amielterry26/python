# Problem:
# Create an area code identifier app.
# Variables
# Logic
# Function

def main():

    while True:
        which = input("Would you like to look up a area code or city? ")
        if which == "area code":
            area_code()
        elif which == "city":
            cities()
        else:
            break


def area_code():
    while True:
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
        elif code == "253":
            print(area_codes["253"])
        elif code == "360":
            print(area_codes["360"])
        elif code == "425":
            print(area_codes["425"])
        elif code == "564":
            print(area_codes["564"])
        else:
            print("Please enter a valid area code for Washington State.")
        answer = input("Would you like to enter another area code? ")
        if answer.lower() != "y":
            break


def cities():
    while True:
        cities = {
            "Seattle, WA": {"206"},
            "Tacoma": {"253"},
            "Federal Way": {"253"},
            "Auburn": {"253"},
            "Seattle Metro Area": {"360"},
            "Olympia": {"360"},
            "Bellingham": {"360"},
            "Vancouver": {"360"},
            "East Seattle": {"425"},
            "Everett": {"425"},
            "Bellevue": {"425"},
            "Western Washington": {"564"},
        }

        city = input("What is the city? ")
        if city == "Seattle":
            print(cities["Seattle, WA"])
        elif city == "Tacoma":
            print(cities["Tacoma"])
        elif city == "Federal Way":
            print(cities["Federal Way"])
        elif city == "Auburn":
            print(cities["Auburn"])
        elif city == "Seattle Metro Area":
            print(cities["Seattle Metro Area"])
        elif city == "Olympia":
            print(cities["Olympia"])
        elif city == "Bellingham":
            print(cities["Bellingham"])
        elif city == "Vancouver":
            print(cities["Vancouver"])
        elif city == "East Seattle":
            print(cities["East Seattle"])
        elif city == "Everett":
            print(cities["Everett"])
        elif city == "Bellevue":
            print(cities["Bellevue"])
        elif city == "Western Washington":
            print(cities["Western Washington"])
        else:
            print("Please enter a valid city for Washington State.")
        answer = input("Would you like to enter another city? (y/n): ")
        if answer.lower() != "y":
            break



main()