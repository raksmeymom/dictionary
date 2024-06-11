def print_table_header() -> None:
    id = "ID"
    name = "Full Name"
    dob = "Date of Birth"
    address = "Address"
    salary = "Salary"
    phone = "Phone"
    position = "Position"
    department = "Department"
    print("=" * 135)
    print(f"{id:10} {name:<20} {dob:<15} {address:<30} {salary:<10} {phone:<15} {position:<15} {department:<15}")
    print("=" * 135)

def print_table_row(employee) -> None:

    id = employee["id"]
    name = employee["name"]
    dob = employee["dob"]
    address = employee["address"]
    format_address = address[0:25] + "..." if len(address) > 25 else address
    salary = employee["salary"]
    format_salary = f"${salary:,.2f}"
    phone = employee["phone"]
    position = employee["position"]
    department = employee["department"]
    print(f"{id:10} {name:<20} {dob:<15} {format_address:<30} {format_salary:<10} {phone:<15} {position:<15} {department:<15}")
    
def print_employee_header() -> None:
    day = "Day"
    check_in = "Check In"
    check_out = "Check Out"
    print("=" * 25)
    print(f"{day:<10} {check_in:<10} {check_out:<10}")
    print("=" * 25)

def print_employee_row(io, index) -> None:
    day = f"Day {index + 1}"
    check_in, check_out = io
    
    print(f"{day:<10} {check_in:<10} {check_out:<10}")

def print_annual_report_header() -> None:
    day = "Day"
    late = "Late Per Day"
    over = "Over Time Per Day"
    print("=" * 45)
    print(f"{day:<10} {late:<10} {over:<15}")
    print("=" * 45)

def print_annual_report_row(day, late, over) -> None:
    print(f"{day:<10} {str(late):<10} {str(over):<15}")
    
