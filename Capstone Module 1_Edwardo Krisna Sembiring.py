from tabulate import tabulate 

# Initialize data
admin_data = {"admin": "9999"}
user_data = {"edo": "1234"}
active_renters = {}
rent_history = {}
blocked_users = set()

# ======================================= vehicle list =================================================
vehicles_list = [
        {"tipe": "Excavator Mini PC 30", "stock": 10, "harga_unit": 165000, "harga_all_in": 270000},
        {"tipe": "Excavator Mini PC 45", "stock": 10, "harga_unit": 165000, "harga_all_in": 300000},
        {"tipe": "Excavator Mini PC 55", "stock": 5, "harga_unit": 165000, "harga_all_in": 330000},
        {"tipe": "Excavator Mini PC 75", "stock": 5, "harga_unit": 165000, "harga_all_in": 350000},
        {"tipe": "Excavator PC 100", "stock": 15, "harga_unit": 165000, "harga_all_in": 380000},
        {"tipe": "Excavator PC 200", "stock": 15, "harga_unit": 200000, "harga_all_in": 450000},
        {"tipe": "Excavator Long Arm", "stock": 20, "harga_unit": 250000, "harga_all_in": 550000},
        {"tipe": "Excavator Roda Ban", "stock": 20, "harga_unit": 230000, "harga_all_in": 350000},
        {"tipe": "Bulldozer D31 Mini", "stock": 5, "harga_unit": 165000, "harga_all_in": 425000},
        {"tipe": "Bulldozer D31 Mini Swamp", "stock": 5, "harga_unit": 175000, "harga_all_in": 435000},
        {"tipe": "Bulldozer D65 Standar", "stock": 10, "harga_unit": 175000, "harga_all_in": 520000},
        {"tipe": "Bulldozer D65 Swamp", "stock": 10, "harga_unit": 165000, "harga_all_in": 650000}
]
for vehicle in vehicles_list:
    if "Excavator" in vehicle["tipe"]:
        vehicle["category"] = "excavator"
    elif "Bulldozer" in vehicle["tipe"]:
        vehicle["category"] = "bulldozer"

excavators_list = [vehicle for vehicle in vehicles_list if vehicle["category"] == "excavator"]
bulldozers_list = [vehicle for vehicle in vehicles_list if vehicle["category"] == "bulldozer"]

# ========================================= service list ===================================================
service_list = [
    {"jenis_pekerjaan": "Cut and Fill", "harga": 45000, "category": "cut and fill"},
    {"jenis_pekerjaan": "Pemadatan Tanah", "harga": 20000, "category": "pemadatan tanah"}
]

# ======================================================================================================

# Function for admin sign in
def admin_sign_in():
    print("\nAdmin Sign In")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == admin_data["admin"]:
        print("Welcome, Admin!")
        admin_menu()
    else:
        print("Invalid username or password.")

# ======================== 1. display =========================
# Define categories for vehicles and services
def display_vehicle_data(option):
    selected_data = [vehicle for vehicle in vehicles_list if vehicle["category"] == option]
    if not selected_data:
        print("No vehicles found for the selected category.")
        return

    table_rows = []
    for vehicle in selected_data:
        tipe = vehicle["tipe"]
        stock = vehicle["stock"]
        harga_unit = vehicle["harga_unit"]
        harga_all_in = vehicle["harga_all_in"]
        table_rows.append([tipe, stock, harga_unit, harga_all_in])

    headers = ["Tipe", "Stock", "Harga/Unit", "Harga All-In"]
    print(tabulate(table_rows, headers=headers, showindex='always', tablefmt="fancy_grid"))

# Function to display service data
def display_service_data():
    headers = ["Index", "Jenis Pekerjaan", "Harga"]
    rows = []
    for index, service in enumerate(service_list):
        harga = service["harga"]
        jenis_pekerjaan = service["jenis_pekerjaan"]
        unit = 'm^3' if 'Cut' in jenis_pekerjaan else 'm^2'
        harga_formatted = f"Rp {harga}/{unit}"
        rows.append((index, jenis_pekerjaan, harga_formatted)) 
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))


def display_choice():
    while True:
        print("\nDisplay :")
        print("1. Heavy Vehicle")
        print("2. Service")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            print("\n1. Excavator")
            print("2. Bulldozer")
            vehicle_type_choice = input("Enter your choice (1/2): ")
            if vehicle_type_choice == "1":
                display_vehicle_data("excavator")
                break
            elif vehicle_type_choice == "2":
                display_vehicle_data("bulldozer")
                break
            else:
                print("Invalid choice! Please input correct choice (1/2)!")
                continue

        elif choice == "2":
                display_service_data()
                break

        else:
            print("Invalid choice. Please input correct choice (1/2)!")
            continue


# ========================= 2. add/delete =============================
def add_vehicle(category):
    print(f"\nAdd {category.capitalize()}:")
    display_vehicle_data(category)
    tipe = input(f"Enter Tipe {category.capitalize()}: ")
    stock = int(input("Enter Stock: "))
    harga_sewa_unit = int(input("Enter Harga Sewa Unit: "))
    harga_sewa_all_in = int(input("Enter Harga Sewa All In: "))

    vehicles_list.append({
        "tipe": tipe,
        "stock": stock,
        "harga_unit": harga_sewa_unit,
        "harga_all_in": harga_sewa_all_in,
        "category": category
    })

    display_vehicle_data(category)
    print(f"{category.capitalize()} added successfully.")

def delete_vehicle(category):
    print(f"\nDelete {category.capitalize()}:")
    while True:
        display_vehicle_data(category)
        index = int(input(f"Enter the index of the {category} to delete: "))
        if 0 <= index <= len(vehicles_list):
            del vehicles_list[index]
            print(f"{category.capitalize()} deleted successfully.")
            break
        else:
            print("Invalid index.")

def add_delete_vehicle():
    print("\nAdd/Delete Heavy Vehicle:")
    print("1. Add Vehicle")
    print("2. Delete Vehicle")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\n1. Excavator")
        print("2. Bulldozer")
        vehicle_type_choice = input("Enter your choice (1/2): ")

        if vehicle_type_choice == "1":
            add_vehicle("excavator")
        elif vehicle_type_choice == "2":
            add_vehicle("bulldozer")
        else:
            print("Invalid choice.")

    elif choice == "2":
        print("\n1. Excavator")
        print("2. Bulldozer")
        vehicle_type_choice = input("Enter your choice (1/2): ")

        if vehicle_type_choice == "1":
            delete_vehicle("excavator")
        elif vehicle_type_choice == "2":
            delete_vehicle("bulldozer")
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

def add_service():
    print("\nAdd Service:")
    print("1. Cut and Fill")
    print("2. Pemadatan Tanah")
    service_choice = input("Enter your choice (1/2): ")

    if service_choice == "1":
        jenis_pekerjaan = "Cut and Fill"
    elif service_choice == "2":
        jenis_pekerjaan = "Pemadatan Tanah"
    else:
        print("Invalid choice!")
        return

    harga = int(input("Enter the price: "))

    service_list.append({
        "jenis_pekerjaan": jenis_pekerjaan,
        "harga": harga,
        "category": "cut and fill" if service_choice == "1" else "pemadatan tanah"
    })

    display_service_data(jenis_pekerjaan)
    print(f"{jenis_pekerjaan} added successfully.")

def delete_service():
    print("\nDelete Service:")
    display_service_data()  
    index = int(input("Enter the index of the service to delete: "))
    if 0 <= index < len(service_list):  
        del service_list[index]
        display_service_data() 
        print("Service deleted successfully.")
    else:
        print("Invalid index.")

def add_delete_service():
    print("\nAdd/Delete Service:")
    print("1. Add Service")
    print("2. Delete Service")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        add_service()
    elif choice == "2":
        delete_service()
    else:
        print("Invalid choice.")

def add_delete_choice():
    while True:
        print("\nPlease choose:")
        print("1. Heavy Vehicle")
        print("2. Service")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            add_delete_vehicle()
            break
        elif choice == "2":
            add_delete_service()
            break
        else:
            print("Invalid choice. Please input correct choice (1/2)!.")

# ====================== 3. edit ==================== 
# Function to edit sewa alat berat
def edit_heavy_vehicle():
    print("\nEdit Vehicle:")
    print("1. Excavator")
    print("2. Bulldozer")
    vehicle_type_choice = input("Enter your choice (1/2): ")

    if vehicle_type_choice == "1":
        category = "excavator"
    elif vehicle_type_choice == "2":
        category = "bulldozer"
    else:
        print("Invalid choice.")
        return

    display_vehicle_data(category)
    index = int(input(f"Enter the index of the {category} you want to edit: "))
    if 0 <= index < len(vehicles_list):
        selected_vehicle = [vehicle for vehicle in vehicles_list if vehicle["category"] == category][index]
        print("\nChoose what you want to edit:")
        print("1. Tipe")
        print("2. Stock")
        print("3. Harga Sewa Unit")
        print("4. Harga Sewa All In")
        edit_choice = input("Enter your choice (1/2/3/4): ")

        if edit_choice in {"1", "2", "3", "4"}:
            new_value = input(f"Enter new value for {'Tipe' if edit_choice == '1' else 'Stock' if edit_choice == '2' else 'Harga Sewa Unit' if edit_choice == '3' else 'Harga Sewa All In'}: ")
            # Convert stock to integer if editing stock
            if edit_choice == "2":
                new_value = int(new_value)
            selected_vehicle["tipe" if edit_choice == "1" else "stock" if edit_choice == "2" else "harga_unit" if edit_choice == "3" else "harga_all_in"] = new_value
            print("Vehicle details updated successfully.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid index.")

def edit_service():
    print("\nEdit Service:")
    print("1. Cut and Fill")
    print("2. Pemadatan Tanah")
    service_choice = input("Enter your choice (1/2): ")

    if service_choice == "1":
        service_name = "Cut and Fill"
    elif service_choice == "2":
        service_name = "Pemadatan Tanah"
    else:
        print("Invalid choice.")
        return

    service = next((s for s in service_list if s["jenis_pekerjaan"] == service_name), None)
    if service:
        new_price = int(input(f"Enter new price for {service_name}: "))
        service["harga"] = new_price
        print(f"Price for {service_name} updated successfully.")
    else:
        print(f"No service found for {service_name}")

def edit_choice():
    print("\nEdit Choice:")
    print("1. Edit Heavy Vehicle")
    print("2. Edit Service")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        edit_heavy_vehicle()
    elif choice == "2":
        edit_service()
    else:
        print("Invalid choice.")

# =============== 4 ==============================
# Function to show active renters
def show_active_renters():
    print("\nActive Renters:")
    if orders:
        active_renters = set(username for username in orders.keys())
        for user in active_renters:
            print(f"{user}:")
            my_order(user, orders)
    else:
        print("No active renters.")

# ========= 5 ==========================
# Function to block or unblock user
def block_or_unblock_user():
    print("\nBlock/Unblock User:")
    print("1. Block User")
    print("2. Unblock User")
    choice = input("Enter your choice (1/2): ")

    username = input("Enter the username: ")
    if username in user_data:
        if choice == "1":
            block_user(username)
        elif choice == "2":
            unblock_user(username)
        else:
            print("Invalid choice. Please enter either '1' or '2'.")
    else:
        print(f"User '{username}' not found.")

# Function to block user
def block_user(username):
    if username not in blocked_users:
        blocked_users.add(username)
        print(f"{username} has been blocked.")
    else:
        print(f"{username} is already blocked.")

# Function to unblock user
def unblock_user(username):
    if username in blocked_users:
        blocked_users.remove(username)
        print(f"{username} has been unblocked.")
    else:
        print(f"User '{username}' is not blocked.")

# =========================================
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Display Data")
        print("2. Add/Delete")
        print("3. Edit")
        print("4. Show Active Renters")
        print("5. Block/Unblock User")
        print("6. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_choice()
        elif choice == "2":
            add_delete_choice()
        elif choice == "3":
            edit_choice()
        elif choice == "4":
            show_active_renters()
        elif choice == "5":
            block_or_unblock_user()
        elif choice == "6":
            print("Logged out.")
            return
        else:
            print("Invalid choice.")

# ===========================================================
# Function for user sign in
def user_sign_in():
    print("\nUser Sign In")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_data:
        if user_data[username] == password:
            if username not in blocked_users:
                print(f"Welcome, {username.capitalize()}!")
                user_menu(username)
            else:
                print("Your account has been blocked by admin. Please contact admin for more information!")
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")

# ============================================================
# Function for user sign up
def user_sign_up():
    print("\nUser Sign Up")
    username = input("Enter your desired username: ")
    if username in user_data:
        print("Username already exists. Please choose a different one.")
        return
    password = input("Enter your desired password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    user_data[username] = password
    print("User successfully registered!")
    user_sign_in()

# ================== 1 ===================================
# Function for user to rent heavy vehicle
def rent_excavator(username, orders, excavator_orders_unit, excavator_orders_all_in):
    while True:
        try:
            print("\nHarga Sewa Excavator:")
            display_vehicle_data("excavator")
            print("""\nExcavator Rental Price Terms:
            1. Unit rental price does not include operator's food allowance and diesel fuel
            2. All-in rental fee includes operator's food allowance and diesel fuel
            3. The above excavator rental price does not include mess for the operator
            4. The above rental price does not include mobilization/demobilization costs
            """)

            index = int(input("Enter the index of the excavator you want to rent: "))
            if 0 <= index < len(excavators_list):
                selected_excavator = excavators_list[index]
                quantity = int(input("Enter the quantity you want to rent: "))
                rent_type = input("Enter 'unit' for unit price or 'all in' for all-inclusive price: ")
                if rent_type.lower() == 'unit':
                    price = selected_excavator["harga_unit"]
                    excavator_orders_unit.append({
                        "Item": selected_excavator['tipe'],
                        "Quantity": quantity,
                        "Unit Price": f"Rp. {price}"
                    })
                elif rent_type.lower() == 'all in':
                    price = selected_excavator["harga_all_in"]
                    excavator_orders_all_in.append({
                        "Item": selected_excavator['tipe'],
                        "Quantity": quantity,
                        "All Inclusive Price": f"Rp. {price}"
                    })
                else:
                    print("Invalid choice. Please enter 'unit' or 'all in'.")
                    continue
                    
                if quantity <= selected_excavator["stock"]:
                    print(f"You have successfully rented {quantity} {selected_excavator['tipe']}.")
                    
                    # Update stock
                    selected_excavator["stock"] -= quantity
                    
                    # Add or update the rented item in the user order
                    if username in orders:
                        updated = False
                        for item in orders[username]:
                            if item["item"] == selected_excavator['tipe']:
                                item["quantity"] += quantity
                                updated = True
                                break
                        if not updated:
                            orders[username].append({
                                "item": selected_excavator['tipe'],
                                "quantity": quantity,
                                "unit_price": price,
                            })
                    else:
                        orders[username] = [{
                            "item": selected_excavator['tipe'],
                            "quantity": quantity,
                            "unit_price": price,
                        }]
                    
                    # Display updated vehicle data
                    print("\nUpdated Excavator List:")
                    display_vehicle_data("excavator")
                    
                    # Ask user for another order
                    return
                else:
                    print("Insufficient stock. Please enter a valid quantity.")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def rent_bulldozer(username, orders, bulldozer_orders_unit, bulldozer_orders_all_in):
    while True:
        try:
            print("\nHarga Sewa Bulldozer:")
            display_vehicle_data("bulldozer")
            print("""\nKetentuan Harga Rental Bulldozer:")
            1. Rental price and hours can be renegotiated.
            2. Rental price excludes VAT.
            3. Unit rental price excludes operator's food allowance and diesel fuel.
            4. All-in rental fee includes operator's food allowance and diesel fuel.
            5. Rental price excludes mobilization/demobilization costs.
            6. Excavator rental price excludes operator's mess.
            """)

            index = int(input("Enter the index of the bulldozer you want to rent: "))
            if 0 <= index < len(bulldozers_list):
                selected_bulldozer = bulldozers_list[index]
                quantity = int(input("Enter the quantity you want to rent: "))
                rent_type = input("Enter 'unit' for unit price or 'all in' for all-inclusive price: ")
                if rent_type.lower() == 'unit':
                    price = selected_bulldozer["harga_unit"]
                    bulldozer_orders_unit.append({
                        "Item": selected_bulldozer['tipe'],
                        "Quantity": quantity,
                        "Unit Price": f"Rp. {price}"
                    })
                elif rent_type.lower() == 'all in':
                    price = selected_bulldozer["harga_all_in"]
                    bulldozer_orders_all_in.append({
                        "Item": selected_bulldozer['tipe'],
                        "Quantity": quantity,
                        "All Inclusive Price": f"Rp. {price}"
                    })
                else:
                    print("Invalid choice. Please enter 'unit' or 'all in'.")
                    continue
                    
                if quantity <= selected_bulldozer["stock"]:
                    print(f"You have successfully rented {quantity} {selected_bulldozer['tipe']}.")
                    
                    # Update stock
                    selected_bulldozer["stock"] -= quantity
                    
                    # Add or update the rented item in the user's order
                    if username in orders:
                        updated = False
                        for item in orders[username]:
                            if item["item"] == selected_bulldozer['tipe']:
                                item["quantity"] += quantity
                                updated = True
                                break
                        if not updated:
                            orders[username].append({
                                "item": selected_bulldozer['tipe'],
                                "quantity": quantity,
                                "unit_price": price,  
                            })
                    else:
                        orders[username] = [{
                            "item": selected_bulldozer['tipe'],
                            "quantity": quantity,
                            "unit_price": price,  
                        }]
                    
                    # Display updated vehicle data
                    print("\nUpdated Bulldozer List:")
                    display_vehicle_data("bulldozer")
                    
                    # Ask user for another order
                    return
                else:
                    print("Insufficient stock. Please enter a valid quantity.")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def ask_for_another_order():
    while True:
        choice = input("Are there anything else you want to order? (yes/no): ")
        if choice.lower() == "yes":
            return True
        elif choice.lower() == "no":
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def sewa_alat_berat(username, orders):
    excavator_orders_unit = []
    excavator_orders_all_in = []
    bulldozer_orders_unit = []
    bulldozer_orders_all_in = []

    while True:
        print("\nSewa Alat Berat:")
        print("1. Harga Sewa Excavator")
        print("2. Harga Sewa Bulldozer")
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            rent_excavator(username, orders, excavator_orders_unit, excavator_orders_all_in)
        elif choice == "2":
            rent_bulldozer(username, orders, bulldozer_orders_unit, bulldozer_orders_all_in)
        else:
            print("Invalid choice.")
            return None
        
        # Check if the user wants to continue ordering
        if not ask_for_another_order():
            break

    # Display orders for excavators
    if excavator_orders_unit:
        print("\nOrders for Excavators (Unit Price):")
        print(tabulate(excavator_orders_unit, headers="keys", tablefmt="fancy_grid"))
    
    if excavator_orders_all_in:
        print("\nOrders for Excavators (All Inclusive Price):")
        print(tabulate(excavator_orders_all_in, headers="keys", tablefmt="fancy_grid"))
    
    # Display orders for bulldozers
    if bulldozer_orders_unit:
        print("\nOrders for Bulldozers (Unit Price):")
        print(tabulate(bulldozer_orders_unit, headers="keys", tablefmt="fancy_grid"))
    
    if bulldozer_orders_all_in:
        print("\nOrders for Bulldozers (All Inclusive Price):")
        print(tabulate(bulldozer_orders_all_in, headers="keys", tablefmt="fancy_grid"))

    
# =============================== 2 =============================
# Function for user to order services
def validate_order_input(minimum_value, unit):
    while True:
        try:
            order_input = int(input(f"Enter the {unit}: "))
            if order_input >= minimum_value:
                return order_input
            elif order_input == 0:
                print("Order canceled.")
                return None
            else:
                print(f"The minimum order is {minimum_value} {unit}. Please input more than {minimum_value} {unit} or press '0' to cancel the order.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def layanan_jasa(username):
    def display_service_data(service_type):
        headers = ["Jenis Pekerjaan", "Harga"]
        rows = [(service["jenis_pekerjaan"], f"Rp {service['harga']}/{'m^3' if 'Cut' in service['jenis_pekerjaan'] else 'm^2'}") for service in service_list if service_type in service["jenis_pekerjaan"]]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    print("\nLayanan Jasa:")
    print("1. Jasa Cut and Fill Tanah")
    print("2. Jasa Pemadatan Tanah")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nJasa Cut and Fill Tanah:")
        display_service_data("Cut and Fill")
        print("\nKetentuan Harga Rental Cut and Fill Tanah:")
        print("1. Minimum order 2500 m^3")
        print("2. Harga belum termasuk pajak")
        order_volume = validate_order_input(2500, "m^3")
        if order_volume is not None:
            # Find the service dictionary for "Jasa Cut and Fill Tanah" in service_list
            selected_service = next((service for service in service_list if "Cut and Fill" in service["jenis_pekerjaan"]), None)
            if selected_service:
                unit_price = selected_service["harga"]
                print(f"You have successfully ordered {order_volume} m^3 of Cut and Fill Tanah.")
                update_order(username, "Jasa Cut and Fill Tanah", order_volume, unit_price)
            else:
                print("Service data not found.")
            return None

    elif choice == "2":
        print("\nJasa Pemadatan Tanah:")
        display_service_data("Pemadatan Tanah")
        print("\nKetentuan Harga Rental Pemadatan Tanah:")
        print("1. Minimum order 2000 m^2")
        print("2. Harga belum termasuk pajak")
        order_area = validate_order_input(2000, "m^2")
        if order_area is not None:
            # Find the service dictionary for "Jasa Pemadatan Tanah" in service_list
            selected_service = next((service for service in service_list if "Pemadatan Tanah" in service["jenis_pekerjaan"]), None)
            if selected_service:
                unit_price = selected_service["harga"]
                print(f"You have successfully ordered {order_area} m^2 of Pemadatan Tanah.")
                update_order(username, "Jasa Pemadatan Tanah", order_area, unit_price)
            else:
                print("Service data not found.")
            return None

    else:
        print("Invalid choice.")
        return None

def update_order(username, service_name, quantity, unit_price):
    # Add or update the rented service in the user's order
    if username in orders:
        updated = False
        for item in orders[username]:
            if item["item"] == service_name:
                item["quantity"] += quantity
                updated = True
                break
        if not updated:
            orders[username].append({
                "item": service_name,
                "quantity": quantity,
                "unit_price": unit_price,  
            })
    else:
        # Create a new order for the user
        orders[username] = [{
            "item": service_name,
            "quantity": quantity,
            "unit_price": unit_price,  
        }]


# ============================ 3 ===================================
# Function to display user's order details
def my_order(username, orders):
    print("\nMy Order:")
    if isinstance(orders, dict) and username in orders:
        order_items = []
        total_price = 0

        # Prepare data for the table
        for order in orders[username]:
            item = order["item"]
            quantity = order["quantity"]
            unit_price = order["unit_price"]
            total_price += unit_price * quantity
            order_items.append([item, quantity, f"Rp. {unit_price}", f"Rp. {unit_price * quantity}"])

        # Display the table
        headers = ["Item", "Quantity", "Unit Price", "Total Price"]
        print(tabulate(order_items, headers=headers, tablefmt="fancy_grid"))

        # Calculate total price with tax
        total_price_with_tax = total_price * 1.11
        print("\nTotal Price (including 11% tax): Rp.", total_price_with_tax)
    else:
        print("You have no active orders.")

# Initialize orders dictionary
orders = {}

# =======================================================
# Function for user menu
def user_menu(username):
    while True:
        print("\nUser Menu:")
        print("1. Sewa Alat Berat")
        print("2. Layanan Jasa")
        print("3. My Order")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            sewa_alat_berat(username, orders)  
        elif choice == "2":
            layanan_jasa(username)
        elif choice == "3":
            my_order(username, orders)  
        elif choice == "4":
            print("Logged out.")
            return
        else:
            print("Invalid choice.")

# ===================================================
def main():
    while True:
        print("\nWelcome to Heavy Vehicle Rent")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sign_in_choice = input("Are you an admin or user? Enter 'admin' or 'user': ")
            if sign_in_choice == "admin":
                admin_sign_in()
            elif sign_in_choice == "user":
                user_sign_in()
            else:
                print("Invalid choice.")
        elif choice == "2":
            user_sign_up()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
