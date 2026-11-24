









def select_product(gender, style):
    print("PRODUCT MENU")
    if gender == "Women":
        if style == "Formal":
            print("1. Pants")
            print("2. Dress")
            print("3. High Heels")
        else:
            print("1. Skirt")
            print("2. Pants")
            print("3. T-Shirt")
            print("4. Sneakers")
    else:
        if style == "Formal":
            print("1. Suit")
            print("2. Tie")
            print("3. Shoes")
        else:
            print("1. Pants")
            print("2. T-Shirt")
            print("3. Long-Sleeve Shirt")
            print("4. Sneakers")
    choice = input("Select a product: ")
    match gender:
        case "Women":
            match style:
                case "Formal":
                    match choice:
                        case "1":
                            return "Pants"
                        case "2":
                            return "Dress"
                        case "3":
                            return "High Heels"
                        case _:
                            return None
                case "Casual":
                    match choice:
                        case "1":
                            return "Skirt"
                        case "2":
                            return "Pants"
                        case "3":
                            return "T-Shirt"
                        case "4":
                            return "Sneakers"
                        case _:
                            return None
        case "Men":
            match style:
                case "Formal":
                    match choice:
                        case "1":
                            return "Suit"
                        case "2":
                            return "Tie"
                        case "3":
                            return "Shoes"
                        case _:
                            return None
                case "Casual":
                    match choice:
                        case "1":
                            return "Pants"
                        case "2":
                            return "T-Shirt"
                        case "3":
                            return "Long-Sleeve Shirt"
                        case "4":
                            return "Sneakers"
                        case _:
                            return None

def add_to_cart(cart, gender, style):
    product = select_product(gender, style)
    if product == None:
        print("Invalid product selection!")
        return
    size = input("Enter product size: ").strip()
    if size == "":
        print("Size cannot be empty!")
        return
    while True:
        price = input("Enter product price: ")
        if price.isdigit() and int(price) > 0:
            price = int(price)
            break
        else:
            print("Invalid price! Please enter a positive number.")
    cart.append([gender, style, product, size, price])
    print("Product added to shopping cart!")
    print("Product: " + product)
    print("Size: " + size)
    print("Price: " + str(price) + " Toman")

def show_cart(cart):
    print("SHOPPING CART")
    if len(cart) == 0:
        print("Your shopping cart is empty.")
        return
    for i in range(len(cart)):
        print("Product Number: " + str(i + 1))
        print("Product: " + cart[i][2])
        print("Size: " + cart[i][3])
        print("Price: " + str(cart[i][4]) + " Toman")

def calculate_total(cart):
    total = 0
    for item in cart:
        total += item[4]
    return total

def print_receipt(cart):
    print("FINAL RECEIPT")
    if len(cart) == 0:
        print("No products purchased.")
        return
    for i in range(len(cart)):
        print("Item: " + cart[i][2])
        print("Size: " + cart[i][3])
        print("Price: " + str(cart[i][4]) + " Toman")
    total = calculate_total(cart)
    print("-----------------------------------")
    print("Total Products: " + str(len(cart)))
    print("Total Price: " + str(total) + " Toman")
    print("-----------------------------------")
    print("Thank you for shopping with us!")

cart = []
print("WELCOME TO OUR STORE")
print("Select your department:")
print("1. Women's Section")
print("2. Men's Section")
gender_choice = input("Enter your choice: ")
match gender_choice:
    case "1":
        gender = "Women"
    case "2":
        gender = "Men"
    case _:
        gender = None
        print("Invalid department selection!")
if gender != None:
    print("Select clothing category:")
    print("1. Formal Wear")
    print("2. Casual Wear")
    style_choice = input("Enter your choice: ")
    match style_choice:
        case "1":
            style = "Formal"
        case "2":
            style = "Casual"
        case _:
            style = None
            print("Invalid category selection!")
    if style != None:
        while True:
            print("CLOTHING STORE")
            print("1. Select a Product")
            print("2. Show Shopping Cart")
            print("3. Finish Shopping")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    add_to_cart(cart, gender, style)
                case "2":
                    show_cart(cart)
                case "3":
                    break
                case _:
                    print("Invalid choice!")
        print_receipt(cart)