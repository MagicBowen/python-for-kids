phone_numbers = {
    "wangbo" : "13759947708",
    "jerry"  : "13588888888",
    "tianyu" : "13772101699"
}

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