# Main application logic for seat management system

import app_class as c  # Import seat class module

# Initialize seat data structures
seat_lst = []  # Master list containing all seat objects and markers (X/S)
seat_lst_for_check = []  # List of valid seat numbers for quick validation

# Populate seat layout according to Burak757 specifications
for n in range(0, 4):  # 4 blocks of seats
    for row in ["A", "B", "C", "X", "D", "E", "F"]:  # Seat rows
        if row == "X":
            # Add 20 'X' markers for floor island
            seat_lst.extend(["X"] * 20)
        else:
            # Generate seat numbers for valid rows
            for col in range(n * 20 + 1, (n + 1) * 20 + 1):
                seat_no = str(col) + row
                if seat_no in ["77D", "77E", "77F", "78D", "78E", "78F"]:
                    seat_lst.append("S")  # Storage areas
                else:
                    # Create Seat object and track valid seats
                    seat_lst.append(seat_no)
                    seat_lst[-1] = c.Seat(seat_no)  # Replace string with Seat instance
                    seat_lst_for_check.append(seat_no)


def check_availability(seat_number):
    """Check and display availability status of a specific seat"""
    if seat_number in seat_lst_for_check:
        seat = seat_lst[find_seat_index(seat_number)]
        if seat.status == 0:
            print("The seat you choose is available.\n")
        elif seat.status == 1:
            # Display booking details with blue text (ANSI escape code \033[34m)
            print(f"The seat you choose is already occupied. The person who reserved the seat is \033[34m{seat_lst[find_seat_index(seat_number)].first_name} {seat_lst[find_seat_index(seat_number)].last_name}\033[0m\n")
    else:
        print("The seat you choose does not exist.\n")


def check_seat():
    """Display color-coded seat map using ANSI escape codes"""
    lst_index = 0
    print("All seats shown (Green=Available, Red=Occupied)")
    for i in range(4):  # 4 vertical blocks
        for j in range(7):  # 7 rows
            for k in range(20):  # 20 columns
                if seat_lst[lst_index] not in ["X", "S"]:
                    # Valid seat with color coding
                    if seat_lst[lst_index].status == 0:
                        print(f"\033[92m{seat_lst[lst_index]}\033[0m\t", end="   ")  # Green
                    elif seat_lst[lst_index].status == 1:
                        print(f"\033[91m{seat_lst[lst_index]}\033[0m\t", end="   ")  # Red
                else:
                    # Non-seat area (X/S) with default color
                    print(f"{seat_lst[lst_index]}\t", end="   ")
                lst_index += 1
            print("\n", end="")
        print("\n")


def find_seat_index(seat_number):
    """Calculate index position in seat_lst from seat number"""
    row = seat_number[-1]  # Last character (A-F)
    col = int(seat_number[:-1])  # Numeric part
    # Mapping of rows to vertical positions
    row_map = {"A": 0, "B": 1, "C": 2, "D": 4, "E": 5, "F": 6}
    return row_map[row] * 20 + ((col - 1) % 20)  # Position calculation


def book_seat(seat_number):
    """Handle seat booking process"""
    if str(seat_number) not in seat_lst_for_check:
        print("Invalid seat\n")
    elif seat_lst[find_seat_index(seat_number)].status == 1:
        print("Already occupied\n")
    else:
        # Collect passenger information
        seat_lst[find_seat_index(seat_number)].set_passport_number(input("Please enter your passport number: "))
        seat_lst[find_seat_index(seat_number)].set_first_name(input("First name: "))
        seat_lst[find_seat_index(seat_number)].set_last_name(input("Last name: "))
        seat_lst[find_seat_index(seat_number)].turn_occupied()
        # Display booking reference in yellow (\033[93m)
        print(f"Booked. Reference: \033[93m{seat_lst[find_seat_index(seat_number)].reference_number}\033[0m\n")


def free_seat(seat_number):
    """Handle seat release process"""
    if str(seat_number) not in seat_lst_for_check:
        print("Invalid seat\n")
    elif seat_lst[find_seat_index(seat_number)].status == 0:
        print("Already free\n")
    else:
        seat = seat_lst[find_seat_index(seat_number)]
        seat.turn_available()
        seat.information_clear()
        print("Seat freed\n")


def main():
    """Main menu system using recursive calls"""
    print("Welcome to Apache Booking System")
    print("1. Check availability")
    print("2. Book seat")
    print("3. Free seat")
    print("4. Show seats")
    print("5. Exit")

    choice = input("Choose option: ")
    if choice == "1":
        check_availability(input("Seat number: "))
        main()  # Recursive recall
    elif choice == "2":
        book_seat(input("Seat number: "))
        main()
    elif choice == "3":
        free_seat(input("Seat number: "))
        main()
    elif choice == "4":
        check_seat()
        main()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        main()


# Start application
main()