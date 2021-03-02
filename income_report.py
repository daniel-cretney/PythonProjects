# this file is to track how much money i'll make after taxes annually


def income_report():
    print("This is your annual take home salary after taxes in the 2020 year based off of state and federal taxes")
    income = float(input("What's your annual salary? (In whole numbers)\n"))
    taxable_income = income - 12400
    if income >= 17001:
        state_rate = 720 + ((income - 17000) * .0575)
    # calculating tax rate in correspondence to annual income
    if income <= 9875:
        tax_rate = .10
        if income <= 3000:
            state_rate = income * .02
        elif income <= 5000:
            state_rate = 60 + ((income - 3000) * .03)
        else:
            state_rate = 120 + ((income - 5000) * .05)
    elif income <= 40125:
        tax_rate = (9875 * .10) + ((income - 9875) * .12)
        if income <= 17000:
            state_rate = state_rate = 120 + ((income - 5000) * .05)
    elif income <= 85525:
        tax_rate = (9875 * .10) + (40125 * .12) + ((income - 40125) * .22)
    elif income <= 163300:
        tax_rate = (9875 * .10) + (40125 * .12) + (85525 * .22) + ((income - 85525) * .24)
    elif income <= 207350:
        tax_rate = (9875 * .10) + (40125 * .12) + (85525 * .22) + (163300 * .24) + ((income - 163300) * .32)
    elif income <= 518400:
        tax_rate = (9875 * .10) + (40125 * .12) + (85525 * .22) + (163300 * .24) + (207350 * .32) + ((income - 207350)
                                                                                                     * .35)
    else:
        tax_rate = (9875 * .10) + (40125 * .12) + (85525 * .22) + (163300 * .24) + (207350 * .32) + (518400 * .35) + \
                   ((income - 518400) * .37)
    social_sec = income * .062
    take_social_s = social_sec * 2

    final_income = income - tax_rate - state_rate - social_sec
    weekly = final_income / 52
    print(f"Your final state taxes amount for this year is ${round(state_rate, 2):,}")
    print(f"Your final federal taxes amount for this year is ${round(tax_rate, 2):,}")
    print(f"You're final social security taxes amount for this year is ${round(social_sec, 2):,}")
    print(f"The amount that is going to your social security for the year is ${round(take_social_s, 2):,}")
    print(f"Your weekly earnings would approximately come out to be ${round(weekly, 2):,}")
    print(f"Your final take home income for the year of 2020 without deductions is ${round(final_income, 2):,}\n")
    count = 0
    while count == 0:
        answer = str(input("Would you like to try a different amount? (Y or N)\n"))
        if answer == "y" or answer == "Y":
            count = 1
            income_report()
        elif answer == "n" or answer == "N":
            print("Session completed, thank you")
            count = 1
        else:
            print("Wrong selection, try again")
            count = 0


if __name__ == "__main__":
    income_report()