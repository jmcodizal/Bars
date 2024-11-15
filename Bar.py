DAYS_IN_MONTH = 30
NUM_ROOMS = 6
NUM_COTTAGES = 6

# Global variables
roomAvailability = [[False] * (DAYS_IN_MONTH + 1) for _ in range(NUM_ROOMS)]
cottageAvailability = [[False] * (DAYS_IN_MONTH + 1) for _ in range(NUM_COTTAGES)]
availability = [True] * (DAYS_IN_MONTH + 1)

accommodation = None
date = None
month = ""
departure = None
name = ""
email = ""
number = ""
Amenity = []  
stay = ""
reservationMade = False
isRoom = False
totalPayment = 0

roomPrices = [3690, 3500, 3279, 3250, 2700, 1580]
cottagePrices = [4999, 1999, 1399, 1299, 999, 1399]
amenityPrices = [3250, 700, 750, 450, 899, 200]  

# Menu items available in the sports bar
menu = {
    'Food': {
        'Burger': 35.00,
        'Pizza': 40.00,
        'Fries': 48.00,
        'Wings': 50.00,
        'Waffle': 65.00,
        'Pasta': 89.00
    },
    'Drinks': {
        'Bloody Blink': 49.00,
        'Green Lily': 49.00,
        'Banana Muggle': 39.00,
        'Fuzzy Polyjuice': 49.00
    },
    'Special Drinks': {
        'Spicy Basilisk': 69.00,
        'Manhattan Beauxbatons': 59.00,
        'Forbidden Quidditch': 59.00,
        'Goblet of Daigure': 59.00
    }
}

# Order status constants
PENDING = 'Pending'
IN_PROGRESS = 'In Progress'
READY = 'Ready'

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = PENDING
        self.total = 0.0

    def add_item(self, item, category):
        category = category.title()  # Capitalize category for uniformity
        print(f"Category selected: {category}")

        if category in menu:
            item = item.lower().title()  # Capitalize item to ensure correct matching
            print(f"Item selected: {item}")

            if item in menu[category]:
                price = menu[category][item]
                self.items.append((item, price))
                self.total += price
                print(f"Added {item} to your order. Price: ${price:.2f}")
            else:
                print(f"Sorry, {item} is not available in the {category} menu.")
        else:
            print(f"Invalid category: {category}. Please choose 'Food', 'Drinks', or 'Special Drinks'.")

    def display_order(self):
        print("\nYour Order Summary:")
        print("--------------------")
        for item, price in self.items:
            print(f"- {item}: ${price:.2f}")
        print(f"Total: ${self.total:.2f}")
        print(f"Status: {self.status}")

    def update_status(self, status):
        self.status = status
        print(f"Order {self.order_id} status updated to {self.status}.")

class SportsBar:
    def __init__(self):
        self.orders = {}
        self.current_order_id = 1

    def display_menu(self):
        print("\n\t\t\t\t\t Welcome to the Sports Bar! \t\t\t\t\t\t")
        print("Here is the menu:")
        for category, items in menu.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"  - {item}: ${price:.2f}")

    def create_order(self):
        order = Order(self.current_order_id)
        self.orders[self.current_order_id] = order
        self.current_order_id += 1
        return order

    def take_order(self):
        self.display_menu()
        order = self.create_order()

        while True:
            category = input("\nSelect category (Food/Drinks/Special Drinks) or type 'done' to finish: ").capitalize()
            if category == 'Done':
                break
            if category not in ['Food', 'Drinks', 'Special Drinks']:
                print("Invalid category. Please choose 'Food', 'Drinks' or 'Special Drinks'.")
                continue

            item = input(f"Enter the name of the {category} item: ").capitalize()
            order.add_item(item, category)

        order.display_order()
        return order

    def prepare_order(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            print(f"\nPreparing Order {order_id}...")
            order.update_status(IN_PROGRESS)
        else:
            print("Order not found.")

    def complete_order(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            print(f"\nCompleting Order {order_id}...")
            order.update_status(READY)
            self.process_payment(order)
        else:
            print("Order not found.")

    def process_payment(self, order):
        print(f"\nYour total is: ${order.total:.2f}")
        payment = float(input("Enter payment amount: $"))
        if payment >= order.total:
            change = payment - order.total
            print(f"Payment successful! Your change is: ${change:.2f}")
        else:
            print("Insufficient payment. Please try again.")

    def display_receipt(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            print("\n--- Receipt ---")
            print(f"Order ID: {order_id}")
            print("----------------")
            for item, price in order.items:
                print(f"{item}: ${price:.2f}")
            print(f"Total: ${order.total:.2f}")
            print(f"Status: {order.status}")
            print("----------------")
        else:
            print("Order not found.")

def sports_bar_system():
    sports_bar = SportsBar()

    while True:
        print("\n                         ----------------------------------------------------------------------      ")
        print("\n\t\t\t\t\t === Sports Bar Ordering System ===\t\t\t\t\t\t")
        print("\t\t\t\t\t  1. Place Order \t\t\t\t\t\t")
        print("\t\t\t\t\t  2. Prepare Order \t\t\t\t\t\t")
        print("\t\t\t\t\t  3. Complete Order \t\t\t\t\t\t")
        print("\t\t\t\t\t  4. View Order Information / Receipt \t\t\t\t\t\t")
        print("\t\t\t\t\t  5. Exit \t\t\t\t\t\t")
        print("                         ----------------------------------------------------------------------      ")

        choice = input("Enter your choice: ")

        if choice == '1':
            sports_bar.take_order()
        elif choice == '2':
            order_id = int(input("Enter Order ID to prepare: "))
            sports_bar.prepare_order(order_id)
        elif choice == '3':
            order_id = int(input("Enter Order ID to complete: "))
            sports_bar.complete_order(order_id)
        elif choice == '4':
            order_id = int(input("Enter Order ID to view receipt: "))
            sports_bar.display_receipt(order_id)
        elif choice == '5':
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
def main():
    print("\n\t\t\t\t\t Welcome to the JMC Reservation and Sports Bar System! \t\t\t\t\t\t")
    print("\t\t\t\t\t 1. Hometel Reservation \t\t\t\t\t\t")
    print("\t\t\t\t\t 2. Sports Bar Ordering System \t\t\t\t\t\t")
    choice = input("\t\t\t\t\t Choose a system (1 or 2): ")

    if choice == '1':
        print("\n\t\t\t\t\t Welcome to the Hometel Reservation System \t\t\t\t\t\t")
        hometel_system()
    elif choice == '2':
        print("\n\t\t\t\t\t Welcome to the Sports Bar Ordering System \t\t\t\t\t\t")
        sports_bar_system()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
