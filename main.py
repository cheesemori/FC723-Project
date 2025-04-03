import app_class as c

seat_lst = []

for n in range(0,4):
    for row in ["A","B","C","X","D","E","F"]:
        if row == "X":
            for i in range(20):
                seat_lst.append("X")
        else:
            for col in range(n*20+1,(n+1)*20+1):
                seat_no = str(col)+row
                if seat_no in ["77D","77E","77F","78D","78E","78F"]:
                    seat_lst.append("S")
                else:
                    seat_lst.append(seat_no)
                    seat_lst[-1] = c.Seat(seat_no)




def check_seat():
    lst_index = 0
    for i in range(4):
        for j in range(7):
            for k in range(20):
                if seat_lst[lst_index] not in ["X","S"]:
                    if seat_lst[lst_index].status == 0:
                        print(f"\033[92m{seat_lst[lst_index]}\033[0m\t", end="   ")
                    elif seat_lst[lst_index].status == 1:
                        print(f"\032[92m{seat_lst[lst_index]}\033[0m\t", end="   ")
                else:
                    print(f"{seat_lst[lst_index]}\t", end="   ")
                lst_index += 1
            print("\n", end="")
        print("\n")

def find_seat_index(seat_number):
    lst_index = 0

check_seat()

print(seat_lst)