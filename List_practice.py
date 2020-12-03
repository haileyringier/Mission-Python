take_off_checklist = [
    "Put suit on",
    "Seal hatch",
    "Check cabin pressure",
    "Fasten seatbelt"
]

print(take_off_checklist)

# add item to end of list using .append(new item)

take_off_checklist.append("Enjoy Space")

#remove item from the list using .remove(item) or using del

take_off_checklist.remove("Seal hatch")
del take_off_checklist[2]

# insert an item ina  specific index position using .insert(index #, new item)

take_off_checklist.insert(1, "Seal hatch ")

# access an item in list using index

print(take_off_checklist[2]) 

# replace an item in a list by setting the new value 

take_off_checklist[0] = "Put suit on"

print(take_off_checklist)

spacewalk_checklist = [
    "Put suit on",
    "Check oxygen",
    "Seal helmet",
    "Test radio",
    "Open airlock"
]

# list of lists 

flight_manual = [take_off_checklist, spacewalk_checklist]

print(flight_manual)

# to access an individual element in the list of lists need two indexes

print(flight_manual[1][2])

# to combine multiple lists into one use a + or +=

skills_list = take_off_checklist + spacewalk_checklist

print(skills_list)
