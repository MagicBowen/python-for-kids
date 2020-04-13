import json

f = open("phone.json", "r+")

phone_numbers = json.load(f)

while True:
    name = input("Who will you search?")

    if name in phone_numbers:
        print(name, "'s phone number is", phone_numbers[name])
    else:
        print("sorry,", name, "'s phone number is not exist")
        is_add = input("Do you want add the phone number for " + name + ", yes / no? ")
        if is_add == "yes":
            number = input("please input the phone number : ")
            phone_numbers[name] = number
        else:
            break

f.seek(0, 0)
f.truncate()        
json.dump(phone_numbers, f)
f.close()