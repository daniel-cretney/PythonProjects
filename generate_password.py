# the point of this module is to generate a random password when executing the function

import random
import math


def generate_password():
    list_of_randomized = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "!", "@", "#", "$", "%", "^",
                          "&", "*", "(", ")"]
    list_of_spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    customized_list = []
    length = 0
    query = str(input("Do you require a certain amount of uppercase and special characters? (Y or N)\n"))
    if query == "Y" or query == "y":
        count = 0
        while count == 0:
            length = int(input("How long do you want the password to be?\n"))
            uppercase = int(input("How many uppercase characters do you need?\n"))
            spec_char = int(input("How many special characters do you need?\n"))
            if uppercase + spec_char > length:
                print("Your special characters and uppercase letters are greater than the length of the password.  Try "
                      "again.")
            else:
                count = 1
                for index in range(spec_char):
                    index = math.ceil(random.random() * (len(list_of_spec_char) - 1))
                    variable = list_of_spec_char[index]
                    customized_list.append(variable)
                for index in range(uppercase):
                    index = math.ceil(random.random() * 25)
                    variable = list_of_randomized[index]
                    customized_list.append(variable.upper())
            print(customized_list)
            length = length - uppercase - spec_char
    elif query == "N" or query == "n":
        pass
    else:
        print("Wrong selection, try again.")
    password = ""
    for index in range(length):
        index = math.ceil(random.random() * (len(list_of_randomized) - 1))
        variable = list_of_randomized[index]
        if type(variable) == str:
            odds = math.ceil(random.random() * 5)
            if odds >= 4:
                variable = variable.upper()
        customized_list.append(variable)
    for index in range(len(customized_list)):
        index = math.ceil(random.random() * (len(customized_list) - 1))
        variable = customized_list[index]
        password = password + str(variable)

    print("Here is your randomly generated password: {}".format(password))
    count = 0
    while count == 0:
        again = str(input("Try again? (Y or N)\n"))
        if again == "Y" or again == "y":
            count = 1
            generate_password()
        elif again == "N" or again == "n":
            count = 1
            print("Thank you!")
        else:
            print("Wrong selection, try again")


if __name__ == "__main__":
    generate_password()
