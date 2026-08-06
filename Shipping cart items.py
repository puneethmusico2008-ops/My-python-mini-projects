
"""
Shopping Cart Manager
A simple shopping cart using Python lists.
"""

print("=======> Shopping Cart Manager <=======")

products = []
prices = []

while True:
    print("\n===== MENU =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. View Total Bill")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        product = input("Enter product name: ")

        if product in products:
            print(" Product already exists!")
        else:
            try:
                price = int(input("Enter product price: "))

                products.append(product)
                prices.append(price)

                print("✅ Product added successfully!")

            except ValueError:
                print("Please enter a valid price.")

    elif choice == "2":

        if not products:
            print("Cart is empty.")

        else:
            print("\n====== SHOPPING CART ======")

            for i, product in enumerate(products, start=1):
                print(f"{i}. {product} - ₹{prices[i-1]}")

    elif choice == "3":

        if not products:
            print("Cart is empty.")

        else:
            try:
                product_number = int(input("Enter product number to delete: "))

                if 1 <= product_number <= len(products):

                    deleted_product = products.pop(product_number - 1)
                    deleted_price = prices.pop(product_number - 1)

                    print(f"✅ {deleted_product} removed successfully!")

                else:
                    print("Invalid product number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":

        if not products:
            print("Cart is empty.")

        else:
            print("\n====== BILL ======")

            total = 0

            for i, product in enumerate(products, start=1):
                print(f"{i}. {product} - ₹{prices[i-1]}")
                total += prices[i-1]

            print("-----------------------")
            print(f"Total Bill = ₹{total}")

    elif choice == "5":
        print("Thank you for using Shopping Cart Manager!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")