from datetime import datetime

Fixed_rate = 10
Parking_Spot = int(input("Enter the fixed number of parking spots:\n"))
Start_Date = datetime.date(datetime.now())
Fixed_Parking_spot = Parking_Spot
Data_list = {}
choice = ''
Date = []
num = 0
result = {}


def cost_counter():
    time_taken = (datetime.now() - car_details["Entry_Time"]).seconds
    entry_time = car_details["Entry_Time"].strftime("%d/%m/%y %H:%M:%S")
    standing_time = int(int(time_taken)/60)/60
    cost = Fixed_rate * standing_time
    return entry_time, standing_time, cost


today = datetime.date(datetime.now())

while True:
    print("Select Among the following Choices:\n")
    print("1. Enter Parking\n")
    print("2. Exit Parking\n")
    print("3. To Print Parking Space Directory\n")
    print("4. To Print daily report\n")

    choice = int(input("Enter your  choice:\n"))

    if choice == 1:
        if Parking_Spot > 0:
            car_number = input("Enter the Car Number\t")
            duplication_flag = False
            for num in Data_list:
                if Data_list[num]:
                    if Data_list[num]["Car_Num"] == car_number:
                        duplication_flag = True
                        break

            if not duplication_flag:
                num += 1
                Data_list[num] = {"Car_Num": car_number, "Entry_Time": datetime.now()}
                print("\nWelcome to the Parking!\t\n")
                Parking_Spot -= 1

            elif duplication_flag:
                print("Duplicate entry")
        else:
            print("\n No parking space available. \n")

    elif choice == 2:
        if Parking_Spot == Fixed_Parking_spot:
            print("\nThere's no vehicle in the Parking, Invalid Request\n")
        else:
            rem = input("\nenter your car number\t")
            exit_flag = False
            for num in Data_list:
                if Data_list[num]:
                    if Data_list[num]["Car_Num"] == rem:
                        exit_flag = True
                        car_details = Data_list[num]
                        break

            if not exit_flag:
                print("\nKindly enter valid car Number\n")
            elif exit_flag:
                A, B, C = cost_counter()
                Parking_Spot += 1
                print("\nYour Parking Cost is {}, Thank you for your visit.\n".format(C))
                Data_list[num]["Exit_Time"] = datetime.now()
                Data_list[num]["Amount"] = C
                Date.append(Data_list[num])
                del Data_list[num]

    elif choice == 3:
        print("Sr.No. \t Car No. \t Entry Time \t\t\t Total Time (Hours) \t Total Cost (Rs.)")
        f = 0
        for car_number in Data_list:
            car_details = Data_list[car_number]
            A, B, C = cost_counter()
            f += 1
            print("{} \t\t {} \t\t {} \t\t {} \t\t\t\t\t\t {}".format(f, car_details["Car_Num"], A, B, C))

    elif choice == 4:
        print("Date \t\t\t Car Count \t\t Total Earning (Rs.)")
        count = 0
        Earning = 0
        for num in Date:
            day1 = num["Entry_Time"].strftime('%Y-%m-%d')
            if day1 not in result:
                day = num["Entry_Time"].strftime('%Y-%m-%d')
                count += 1
                Earning += num["Amount"]
                result[day] = {"Amount": Earning, "Count": count}
            elif day1 in result:
                count += 1
                Earning += num["Amount"]
                day = num["Entry_Time"].strftime('%Y-%m-%d')
                result[day] = {"Amount": Earning, "Count": count}
        for day2, Value in result.items():
            print("{} \t\t\t{}\t\t\t {}".format(day2, Value["Count"], Value["Amount"]))