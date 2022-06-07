from tabulate import tabulate
import datetime
now = datetime.datetime.now()
print("               -----------WELCOME TO SAGA CAB SERVICES---------           ")
print('')

#avalable vehicle list
car_AC_3 = ["Suzuki Alto  (CVF-6523)","Suzuki Alto  (ASC-3133)"]
car_nAC_3= ["Suzuki Alto  (CAF-4562)","Sunny        (ADD-1234)"]
car_AC_4 = ["Honda Vessel (ASF-2263)","Benz         (FGG-1234)", "Mazda (HHJ-6541)"]
car_nAC_4= ["WagonR       (DAF-1353)","Nissan       (JJK-2566"]

van_AC_6 = ["Toyota KDH   (CAF-4562)"]
van_nAC_6= ["Nissan       (CVF-6523)"]
van_AC_8 = ["Toyota KDH   (DAF-1353)"]
van_nAC_8= ["Mazda        (ASF-2263)"]

wheel_3 = ["Bajaj (FGH-1235)"]

truck_7 = ["Benz (HJH-1235)"]
truck_12= ["DAF (FHG-1237)"]

lory_25 = ["Toyota (DSF-1255)"]
lory_35= ["Nissan (FHG-2513)"]




#welcome message
def welcome():
    print('')
    print("")

    print('Are You Login as a Customer           ---------- please Enter Number 1 \n'
          'Are You Login as a Vehicle Owner      ---------- please Enter Number 2')
    print("")
    login = int(input("Enter Your Number - "))

    if login == 1:
        customerInput1()
    elif login == 2:
        owner()

#perview function
def preview():
    data = [["Car", "Maximum number of passengers - 3 and 4 \n"
                    "AC/ Non AC"],
            ["Van", "Maximum number of passengers - 6 and 8\n"
                    "AC/ Non AC"],
            ["Three Wheel", "Maximum number of passengers - 3"],
            ["Truck", "Size – 7 ft and 12 ft"],
            ["Lorry","Max load and size - 2500kg and 3500kg"]
            ]
    col_names = ["Vehicle Type", "Specifications"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    print('')
    print("Go to Back Page                         ---------- please Enter Number 0 ")
    mainPage = int(input())
    if mainPage == 0:
        customerInput1()
    else :
        print("!!!!! Invalid Input !!!!!")

#vehicle owner function(Add vehicles)
def owner():
    own_type = input("Select Your Vehicle type\n"


       "Car         ----- Enter Number 1 \n"
                   "Van         ----- Enter Number 2 \n"
                   "Three Wheel ----- Enter Number 3 \n"
                   "Truck       ----- Enter Number 4 \n"
                   "Lorry       ----- Enter Number 5 \n\n"
                   "Enter Your Vehicle number -----------> ")
    #car and van
    if own_type == '1' or '2' :
        ac_fact = input("If your vehicle has A/C     , Enter number 1\n"
                        "If your vehicle has not A/C , Enter number 0 ----->")
        ps_fact = input("How many passengers can your vehicle carry ----->")
        own_vh_name = input("Enter Your vehicle name and Number [Eg. Nissan (FDG-6567)]")
        #car
        if ac_fact =='1' and ps_fact == '3':
            car_AC_3.append(own_vh_name)
        elif ac_fact =='1' and ps_fact == '4':
            car_AC_4.append(own_vh_name)
        elif ac_fact =='2' and ps_fact =='3':
            car_nAC_3.append(own_vh_name)
        elif ac_fact =='2' and ps_fact =='4':
            car_nAC_4.append(own_vh_name)

        #van
        elif ac_fact =='1' and ps_fact=='6':
            van_AC_6.append(own_vh_name)
        elif ac_fact =='1' and ps_fact=='8':
            van_AC_8.append(own_vh_name)
        elif ac_fact =='2' and ps_fact=='6':
            van_nAC_6.append(own_vh_name)
        elif ac_fact =='2' and ps_fact=='8':
            van_nAC_8.append(own_vh_name)
        print("*** Your Vehicle Registered ***")
    #three wheel
    elif own_type =="3":
        own_vh_name = input("Enter Your vehicle name and Number [Eg. Bajaj (FDG-6567)]   ----->")
        wheel_3.append(own_vh_name)
        print("*** Your Vehicle Registered ***")

    #truck
    elif own_type =="4":
        long = input("How long is your truck (7ft & 12ft) ----->")
        own_vh_name = input("Enter Your vehicle name and Number [Eg. Suzuki (FDG-6567)]   ----->")
        if long == "7":
            truck_7.append(own_vh_name)
        elif long == "12":
            truck_12.append(own_vh_name)
        print("*** Your Vehicle Registered ***")
    #lorry
    elif own_type=="5":
        weight = input("What is the maximum load your truck can carry (2500kg & 3500kg) ------->")
        own_vh_name = input("Enter Your vehicle name and Number [Eg. Suzuki (FDG-6567)]   ----->")
        if weight =="2500":
            lory_25.append(own_vh_name)
        elif weight == "3500":
            lory_35.append(own_vh_name)
        print("*** Your Vehicle Registered ***")

    print("")
    back = input("Go To Main menu                         ---------- please Enter Number 0")
    if back == '0':
        welcome()
    else:
        exit()

#get user choices for hire vehicle
def cust_Cont():
    print("----------------------------------------------------------------------------------------")
    cust_lst = []
    custName = input("Enter Your Name - ")
    cust_lst.append(custName)
    custID = input("Enter Your NIC Number - ")
    cust_lst.append(custID)
    custAdd = input("Enter Your Address - ")
    cust_lst.append(custAdd)
    vh_type = input(
          "\n"
          "Car         -----    Enter Number 1\n"
          "Van         -----    Enter Number 2\n"
          "Three Wheel -----    Enter Number 3\n"
          "Truck       -----    Enter Number 4\n"
          "Lorry       -----    Enter Number 5\n\n"
          "Which type of vehicle do you want ---> ")

#---------------------------------car functions-----------------

    if vh_type =='1':
        ac_fun = input("Dou you need A/C  (If you need A/C enter 'Y' Or Enter 'N') ----> ")
        pg_fun = input("How many seat do you need ( Please enter 3 Or 4)           ----> ")

        if ac_fun == 'Y' and pg_fun == '3':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(car_AC_3, start=1):
                print("       ",i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans-1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ",car_AC_3[count])
                print("A/C Condition   -- YES \n"
                      "available Seats -- 3 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ",custName,"\n"
                      "Address    --- ",custAdd,"\n"
                      "NIC Number --- ",custID)
                car_AC_3.pop(count)
            elif invoice == '1':
                cust_Cont()


        elif ac_fun == 'Y' and pg_fun == '4':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(car_AC_4, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please enter vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", car_AC_4[count])
                print("A/C Condition   -- YES \n"
                      "available Seats -- 4 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                car_AC_4.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif ac_fun == 'N' and pg_fun == '3':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(car_nAC_3, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", car_nAC_3[count])
                print("A/C Condition   -- NO \n"
                      "available Seats -- 3 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                car_nAC_3.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif ac_fun == 'N' and pg_fun == '4':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(car_nAC_4, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", car_nAC_4[count])
                print("A/C Condition   -- NO \n"
                      "available Seats -- 4 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                car_nAC_4.pop(count)
            elif invoice == '1':
                cust_Cont()
        else:
            print(" ")
            print("!!!!! Invalid Input !!!!!")
            back = input("Go To Back Menu                         ---------- please Enter Number 3")
            if back == '0':
                cust_Cont()
            else:
                exit()


#--------------------VAN Functions --------------------------

    elif vh_type =='2':
        ac_fun = input("Dou you need A/C  (If you need A/C enter 'Y' Or Enter 'N') ----> ")
        pg_fun = input("How many seat do you need ( Please enter 6 Or 8)           ----> ")

        if ac_fun == 'Y' and pg_fun == '6':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(van_AC_6, start=1):
                print("       ",i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans-1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ",van_AC_6[count])
                print("A/C Condition   -- YES \n"
                      "available Seats -- 6 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ",custName,"\n"
                      "Address    --- ",custAdd,"\n"
                      "NIC Number --- ",custID)
                van_AC_6.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif ac_fun == 'Y' and pg_fun == '8':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(van_AC_8, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", van_AC_8[count])
                print("A/C Condition   -- YES \n"
                      "available Seats -- 8 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                van_AC_8.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif ac_fun == 'N' and pg_fun == '6':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(van_nAC_6, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", van_nAC_6[count])
                print("A/C Condition   -- NO \n"
                      "available Seats -- 6 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                van_nAC_6.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif ac_fun == 'N' and pg_fun == '8':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(van_nAC_8, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number - ", van_nAC_8[count])
                print("A/C Condition   -- NO \n"
                      "available Seats -- 8 Seats\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                van_nAC_8.pop(count)
            elif invoice == '1':
                cust_Cont()
        else:
            print(" ")
            print("!!!!! Invalid Input !!!!!")
            back = input("Go To Back Menu                         ---------- please Enter Number 3")
            if back == '0':
                cust_Cont()
            else:
                exit()


    #--------------3Wheel Function-----------------

    elif vh_type =='3':

        print("")
        print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
        for i, item in enumerate(wheel_3, start=1):
            print("       ", i, item)
            print(" ")
        final_ans = int(input("If You Want hire this car ? please type vehicle index number  --->"))
        count = final_ans - 1
        invoice = input("Create invoice  ------> Enter number 0\n"
                        "Go back to menu ------> Enter number 1")
        print("")
        print("---------------------------------------------------------------------")
        print("")
        if invoice == '0':
            print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
            print("")
            print("Vehicle type and number ----> ", wheel_3[count])
            print("available Seats         ---->    3 Seats\n")
            print("~~~ Customer Details ~~~ \n"
                  "Name       --- ", custName, "\n"
                  "Address    --- ", custAdd, "\n"
                  "NIC Number --- ", custID)
            wheel_3.pop(count)
        elif invoice == '1':
            cust_Cont()
        else:
            print(" ")
            print("!!!!! Invalid Input !!!!!")
            back = input("Go To Back Menu                         ---------- please Enter Number 3")
            if back == '0':
                cust_Cont()
            else:
                exit()



#------Truck Functions ----------------------------

    elif vh_type =='4':
        lg_fun = input("Select the Truck Size (If you need 7ft enter '7' and If you 12ft enter '12' ) ----> ")

        if lg_fun == '7':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(truck_7, start=1):
                print("       ",i, item)
                print(" ")
            final_ans = int(input("If You Want hire this Truck ? please type vehicle index number  --->"))
            count = final_ans-1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number ----> ",truck_7[count])
                print("Truck Size              ---->   7 ft\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ",custName,"\n"
                      "Address    --- ",custAdd,"\n"
                      "NIC Number --- ",custID)
                truck_7.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif lg_fun == '12':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(truck_12, start=1):
                print("       ",i, item)
                print(" ")
            final_ans = int(input("If You Want hire this Truck ? please type vehicle index number  --->"))
            count = final_ans-1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number ----> ",truck_12[count])
                print("Truck Size              ---->   12 ft\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ",custName,"\n"
                      "Address    --- ",custAdd,"\n"
                      "NIC Number --- ",custID)
                truck_12.pop(count)
            elif invoice == '1':
                cust_Cont()
            else:
                print(" ")
                print("!!!!! Invalid Input !!!!!")
                back = input("Go To Back Menu                         ---------- please Enter Number 3")
                if back == '0':
                    cust_Cont()
                else:
                    exit()





#------------------Lorry Functioons----------------------

    elif vh_type=='5':
        load_fun= input("Select Max load (If you need 2500kg enter '2500' and If you 3500kg enter '3500')")

        if load_fun == '2500':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(lory_25, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this Truck ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number ----> ", lory_25[count])
                print("Lorry Load              ---->    2500 Kg\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                lory_25.pop(count)
            elif invoice == '1':
                cust_Cont()

        elif load_fun == '35':
            print("")
            print("              ~~~ Existing vehicles according to your requirements ~~~ \n")
            for i, item in enumerate(lory_35, start=1):
                print("       ", i, item)
                print(" ")
            final_ans = int(input("If You Want hire this Truck ? please type vehicle index number  --->"))
            count = final_ans - 1
            invoice = input("Create invoice  ------> Enter number 0\n"
                            "Go back to menu ------> Enter number 1")
            print("")
            print("---------------------------------------------------------------------")
            print("")
            if invoice == '0':
                print("date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("")
                print("Vehicle type and number ----> ", lory_35[count])
                print("Lorry Load              ---->    3500 Kg\n")
                print("~~~ Customer Details ~~~ \n"
                      "Name       --- ", custName, "\n"
                      "Address    --- ", custAdd, "\n"
                      "NIC Number --- ", custID)
                lory_35.pop(count)
            elif invoice == '1':
                cust_Cont()
            else:
                print(" ")
                print("!!!!! Invalid Input !!!!!")
                back = input("Go To Back Menu                         ---------- please Enter Number 3")
                if back == '0':
                    cust_Cont()
                else:
                    exit()






    else:
        print("!!!!! Invalid Input !!!!!")
        back = input("Go To Back Menu                         ---------- please Enter Number 3")
        if back =='0':
            cust_Cont()
        else:
            exit()

#Hire vehicle and view list (step 01)
def customerInput1():
    print("")
    print("View Vehicles Details                   ---------- please Enter Number 1 \n"
          "I Want To Hire Vehicle                  ---------- please Enter Number 2 \n"
          "Go To Back Menu                         ---------- please Enter Number 3 ")
    print("")
    cust1 = (input("Enter Your Number - "))
    if  cust1 =='1':
        preview()
    elif cust1 =='2':
        cust_Cont()
    elif cust1 =='3':
        welcome()
    else:
        print("!!!!! Invalid Input !!!!!")
        print("Go To Back Menu                         ---------- please Enter Number 3")
        elseIN = input()
        if elseIN == '3':
            welcome()
        else:
            print("!!!!! Invalid Input !!!!!")






welcome()

input('Press ENTER to exit')






