# the purpose of this file is to concatenate the daily reports at the end of the week to make a main weekly report using
import os


def weekly_report():
    week_num = str(input("What week is this?\n"))
    container = 0
    iterate = 0
    while container == 0:
        insert_file = str(input("Enter the file you want to add to the weekly report without the extension (Case "
                                "sensitive).\n"))
        full_file = os.path.abspath("{}.txt".format(insert_file))
        day = ""
        count = 0
        while count == 0:
            day = str(input("What day of the week is this document for? (M, T, W, R, F)\n"))
            if day == "M" or day == "m":
                day = "Monday"
                count = 1
            elif day == "T" or day == "t":
                day = "Tuesday"
                count = 1
            elif day == "W" or day == "w":
                day = "Wednesday"
                count = 1
            elif day == "R" or day == "r":
                day = "Thursday"
                count = 1
            elif day == "F" or day == "f":
                day = "Friday"
                count = 1
            else:
                print("Wrong selection, please try again.")
                count = 0
        with open(full_file, 'r') as rf:
            if iterate == 0:
                input_type = "w"
            else:
                input_type = "a"
            with open("Weekly Report {}.txt".format(week_num), "{}".format(input_type)) as wf:
                wf.write("{}\n".format(day))
                wf.writelines(rf)
                wf.write("\n")
                answer = str(input("Do you want to insert any more? (Y or N)\n"))
                if answer == "Y" or answer == "y":
                    iterate += 1
                    container = 0
                else:
                    container = 1
    print('Document is finished')


if __name__ == "__main__":
    weekly_report()
