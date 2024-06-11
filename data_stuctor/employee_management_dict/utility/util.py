
from data import employees
from datetime import datetime,timedelta
from table import *
#Function: ====|Menu|====

def menu():
    print("===============| Employee Management System |=====================")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Sort Employee")
    print("7. AL (Annual Leave) Employee")
    
    print("0. Exit")
    print("====================================================")

def add_employee()->None:
    print("===============| Add Employee  |=====================")
    employee_num = len(employees)
    id = f"ep{employee_num+ 1:03d}"
    name = input("Enter employee name: ")
    dob = input("Enter employee date of birth (\"yyyy\"\\\"mm\"\\\"dd\"): ")
    address = input("Enter employee address: ")
    salary = float(input("Enter employee salary: "))
    phone = input("Enter empliyee phone: ")
    position = input("Enter employee position: ")
    department = input("Enter employee department: ")
    in_time = datetime.now()
    #Calculate out time subtract 8 hours from in time
    old_time = timedelta(hours=8)
    duration_morning = in_time - old_time
    morning_time = duration_morning.strftime("%H:%M")
    out_time = datetime.now().strftime("%H:%M")
    io = (morning_time, out_time)
    employee = {
        "id":id,
        "name":name,
        "dob":dob,
        "address":address,
        "salary":salary,
        "phone":phone,
        "position":position,
        "department":department,
        "io":io,
    }

def display_all_employee()->None:
    print_table_header(),
    for employee in employees:
        print_table_row(employee)
display_all_employee()


def update_employee() -> None:
    display_all_employee()
    print("======| Update Employee |=======")
    id = input("Enter employee id: ")
    isFound = False
for employee in employees:
    if employee["id"] == id:
            isFound = True
            print("Enter new information: ")
            position = input("Enter employee position: ")
            salary= float(input("Enter employee salary: "))
            department = input("Enter employee department: ")
            employee.update({
                "position": position,
                "salary": salary,
                "department": department,
                })
            print("Employee updated successfully")
            break        
if not isFound:
            print("Employee not found")

def delete_employee() -> None:
    display_all_employee()
    print("======| Delete Employee |=======")
    id = input("Enter employee id: ")
    isFound = False
    for employee in employees:
        if employee["id"] == id:
            isFound = True
            employee.remove(employee)
            print("Employee deleted successfully")
            break
if not isFound:
        print("Employee not found ")
    

def search_employee() -> None:
    print("======| Search Employee |=======")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Salary")
    print("0. Back")
    print("======================================")
    option = input("Enter option: ")
    if(option == "1"):
        id = input("Enter employee id: ")
        isFound = False
        for employee in employees:
            if employee[id] == id:
                isFound = True
                print_table_header()
                print_employee_row(employee)
                print("======| Employee Detail |=======")
                print_table_header()
                io = employee["io"]
                for index, item in enumerate(io):
                    print_employee_row(item, index)

                break
        else:
            print("Employee not found")
    elif(option == "2"):
        print("========| Search by Name |========")
        name = input("Enter employee name: ")
        for employee in employees:
            if employee["name"].lower() == name.lower() :
                print_table_header()
                print_table_row(employee)
    elif(option == "3"):
        print("========| Search by |========")
        salary = float(input("Enter employee salary: "))
        for employee in employees:
            if salary == employee["salary"] :
                print_table_header()
                print_employee_row(employee)
    elif(option == "0"):
        return
    else:
        print("Invalid option")
        return


def sort_employees() -> None:
    employee_copy = employee.copy()
    print("=======| Sort Employee |========")
    print("1. Sort by Name")
    print("2. Sort by Salary")
    print("3. Sort by Position")
    print("0. Exit")
    print("=====================================")
    option = input("Enter option: ")
    if option == "1":
        employee_copy.sort(key=lambda x: x["name"].lower())
    elif option == "2":
        employee_copy.sort(key=lambda x: x["salary"])
    elif option == "3":
        employee_copy.sort(key=lambda x: x["position"].lower())
    elif option == "0":
        return
    else:
        print("Invalid option")
        return
    print_table_header()
    for employee in employee_copy:
        print_employee_row(employee)
def annual_leave() -> None:
    print("=========| Annual Leave of employee |============")
    print("1. Check In")
    print("2. check out")
    print("3. Display Annual Leave Report by Month")
    print("0. Exit")
    print("====================================")
    option = input("Enter option:")
    today_work = [None, None]
    if (option == 1):
        print("=======| Check In |======")
        id = input("Enter employee id: ")
        isFound = False

   
        for employee in employees:
            if id == employee["id"]:
                isFound = True
                check_in_time = datetime.now()
                today_work[0] = check_in_time.strftime("%H:%M")
                print("Check in succesfully")
                break
            if not isFound:
                print("Employee not found")
    elif (option == 2):
        print("=======| Check Out |=======")
        id = input("Enter employee id: ")
        isFound = False

        
        for employee in employees:
            if id == employee["id"]:
                isFound = True
                check_out_time = datetime.now()
                today_work[1] = check_out_time.strftime("%H:%M")
                print("Check in succesfully")
                break
            if not isFound:
                print("Employee not found")
    elif (option == 3):
        print("=======| Report Detail |=======")
        total_work_per_month = timedelta(hours= 8 * 20)
        total_work_per_month_by_employee = timedelta(hours=0)
        id = input("Enter employee id: ")
        isFound = False
        for employee in employees:
            if id == employee["id"]:
                isFound = True
                print_annual_report_header()
                for index, check_in, check_out in enumerate["io"]:
                    total_work_per_day = timedelta(hours=0)
                    check_in_time = datetime.strftime(check_in, "%H:%M")
                    check_out_time = datetime.strftime(check_out, "%H:%M")
                    total_work_per_day = check_out_time - check_in_time
                    total_work_per_month_by_employee += total_work_per_day

            late_per_day = total_work_per_day - timedelta(hours=8)
            late = ""
            over = ""
          
            if late_per_day.total_seconds() < 0:
              over = datetime.strftime(late_per_day, "%H:%M")
            else:
              late = abs(datetime.strftime(str(late_per_day),"&H:%M:%S").strftime("%H:%M"))
            print_annual_report_row(index + 1, late, over)

    late_time_per_moth = total_work_per_month_by_employee - total_work_per_month
    if late_time_per_moth.total_seconds() <0:
        print(f"Late: {abs(late_time_per_moth)}")
    else:
        print(f"over: {late_time_per_moth}")
       
annual_leave()
print("Annual leave")


