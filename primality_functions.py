# this file will take a number and report whether it is prime or not

def is_primary():
    number = int(input("Insert a number.\n"))
    if number <= 3:
        return True
    else:
        divisor = 2
        counter = 0
        for i in range(number):
            if number % divisor == 0:
                counter += 1
        if counter > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    print(is_primary())