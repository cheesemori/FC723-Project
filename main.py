import app_class as c


# 示例输出


seat_lst = []
seat_lst_for_check = []

for n in range(0, 4):
    for row in ["A", "B", "C", "X", "D", "E", "F"]:
        if row == "X":
            for i in range(20):
                seat_lst.append("X")
        else:
            for col in range(n * 20 + 1, (n + 1) * 20 + 1):
                seat_no = str(col) + row
                if seat_no in ["77D", "77E", "77F", "78D", "78E", "78F"]:
                    seat_lst.append("S")
                else:
                    seat_lst.append(seat_no)
                    seat_lst[-1] = c.Seat(seat_no)
                    seat_lst_for_check.append(seat_no)


def check_availability(seat_number):
    if seat_number in seat_lst_for_check:
        if seat_lst[find_seat_index(seat_number)].status == 0:
            print("The seat you choose is available.\n")
        elif seat_lst[find_seat_index(seat_number)].status == 1:
            print(f"The seat you choose is already occupied. The person who reserved the seat is \033[34m{seat_lst[find_seat_index(seat_number)].first_name} {seat_lst[find_seat_index(seat_number)].last_name}\033[0m\n")
    else:
        print("The seat you choose is not exist.\n")


def check_seat():
    lst_index = 0
    print(f"All seats are shown below where Green stands for free and Red stands for occupied.")
    for i in range(4):
        for j in range(7):
            for k in range(20):
                if seat_lst[lst_index] in seat_lst_for_check:
                    if seat_lst[lst_index].status == 0:
                        print(f"\033[32m{seat_lst[lst_index]}\033[0m\t")
                    elif seat_lst[lst_index].status == 1:
                        print(f"\033[31m{seat_lst[lst_index]}\033[0m\t")
                else:
                    print(f"{seat_lst[lst_index]}\t", end="   ")
                lst_index += 1
            print("\n", end="")
        print("\n")


def find_seat_index(seat_number):
    row = str(seat_number)[-1]
    col = int(str(seat_number)[:-1])
    myth_dict = {"A": 0, "B": 1, "C": 2, "D": 4, "E": 5, "F": 6}
    return myth_dict[row] * 20 + ((col - 1) % 20)



def book_seat(seat_number):
    if str(seat_number) not in seat_lst_for_check:
        print("The seat you choose is not exist.\n")
    elif seat_lst[find_seat_index(seat_number)].status == 1:
        print("The seat you choose is already occupied.\n")
    else:
        seat_lst[find_seat_index(seat_number)].passport_number(input("Please enter your passport number: "))
        seat_lst[find_seat_index(seat_number)].first_name(input("Please enter your first name: "))
        seat_lst[find_seat_index(seat_number)].last_name(input("Please enter your last name: "))
        seat_lst[find_seat_index(seat_number)].turn_occupied()
        print(f"The seat you choose is now booked.\nThe reference of your seat is \033[93m{seat_lst[find_seat_index(seat_number)].reference_number}\033[0m\n")


def free_seat(seat_number):
    if str(seat_number) not in seat_lst_for_check:
        print("The seat you choose is not exist.\n")
    elif seat_lst[find_seat_index(seat_number)].status == 0:
        print("The seat you choose is already free.\n")
    else:
        seat_lst[find_seat_index(seat_number)].turn_available()
        print("The seat you choose is now free.\n")
        seat_lst[find_seat_index(seat_number)].information_clear()


def main():
    print("Welcome to Apache flight booking system!")
    print("1. Check availability of seat.")
    print("2. Book a seat.")
    print("3. Free a seat.")
    print("4. Show booking status.")
    print("5. Exit")
    user_option = input("Please choose an option:")
    if user_option == "1":
        check_availability(input("Please enter the seat number you want to check:"))
        main()
    elif user_option == "2":
        book_seat(input("Please enter the seat number you want to book:"))
        main()
    elif user_option == "3":
        free_seat(input("Please enter the seat number you want to free:"))
        main()
    elif user_option == "4":
        check_seat()
        main()
    elif user_option == "5":
        print("Thank you for using Apache flight booking system!")
        exit()
    else:
        print("Invalid option, please try again.")
        main()

main()
