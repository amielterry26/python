# This will be a directory hotel dictionary using a hashmap
directory = {
    "Room 101": {"name": "Jo", "age": 38, "gender": "male", "location": "Puyallup, Washington"},
    "Room 102": {"name": "Amiel", "age": 30, "gender": "male", "location": "Bellvue, Washington"},
    "Room 103": {"name": "Bernard", "age": 44, "gender": "male", "location": "Las Vegas, NV"}
}

print(directory["Room 101"])

# Storing the key-pair in a variable and outputting the variable.
# MAKE SURE TO RESEARCH MORE
room_101_info = directory["Room 101"]
for key, value in room_101_info.items():
    print(f"{key}: {value}")
