









import random
genders = ["Men", "Women", "Kids"]
seasons = [
    "Spring & Summer",
    "Autumn & Winter"
]
categories = [
    "Formal Wear",
    "Casual Wear",
    "Shoes",
    "Accessories"
]
products = [
    ["Men", "Formal Wear", "Suit Jacket", 4500000, False],
    ["Men", "Formal Wear", "Formal Pants", 1800000, False],
    ["Men", "Formal Wear", "Waistcoat", 1500000, False],
    ["Men", "Formal Wear", "Dress Shirt", 1200000, False],
    ["Men", "Formal Wear", "Overcoat", 5800000, True],
    ["Men", "Casual Wear", "Jeans", 1600000, False],
    ["Men", "Casual Wear", "Fabric Pants", 1400000, False],
    ["Men", "Casual Wear", "T-Shirt", 750000, False],
    ["Men", "Casual Wear", "Long Sleeve Shirt", 950000, False],
    ["Men", "Casual Wear", "Hoodie", 1800000, True],
    ["Men", "Shoes", "Sneakers", 3200000, False],
    ["Men", "Shoes", "Crocs", 1500000, False],
    ["Men", "Shoes", "Loafers", 2800000, False],
    ["Men", "Shoes", "Leather Shoes", 3900000, False],
    ["Men", "Shoes", "Ankle Boots", 4200000, True],
    ["Men", "Accessories", "Tie", 450000, False],
    ["Men", "Accessories", "Sunglasses", 1200000, False],
    ["Men", "Accessories", "Perfume", 2500000, False],
    ["Men", "Accessories", "Bow Tie", 350000, False],
    ["Men", "Accessories", "Socks", 180000, False],
    ["Men", "Accessories", "Belt", 650000, False],
    ["Men", "Accessories", "Cufflinks", 850000, False],
    ["Men", "Accessories", "Scarf", 700000, False],
    ["Women", "Formal Wear", "Blazer", 3800000, False],
    ["Women", "Formal Wear", "Dress", 3500000, False],
    ["Women", "Formal Wear", "Skirt", 1400000, False],
    ["Women", "Formal Wear", "Formal Pants", 1700000, False],
    ["Women", "Formal Wear", "Formal Blouse", 1300000, False],
    ["Women", "Formal Wear", "Overcoat", 5500000, True],
    ["Women", "Casual Wear", "Jeans", 1600000, False],
    ["Women", "Casual Wear", "Fabric Pants", 1400000, False],
    ["Women", "Casual Wear", "Long Sleeve Shirt", 950000, False],
    ["Women", "Casual Wear", "Manteau", 2300000, False],
    ["Women", "Casual Wear", "Casual Blouse", 1100000, False],
    ["Women", "Casual Wear", "Hoodie", 1750000, True],
    ["Women", "Shoes", "Sneakers", 3000000, False],
    ["Women", "Shoes", "Crocs", 1400000, False],
    ["Women", "Shoes", "Loafers", 2600000, False],
    ["Women", "Shoes", "Leather Shoes", 3500000, False],
    ["Women", "Shoes", "High Heels", 2900000, False],
    ["Women", "Shoes", "Ankle Boots", 3900000, True],
    ["Women", "Shoes", "Tall Boots", 4800000, True],
    ["Women", "Accessories", "Sunglasses", 1200000, False],
    ["Women", "Accessories", "Perfume", 2800000, False],
    ["Women", "Accessories", "Earrings", 750000, False],
    ["Women", "Accessories", "Bracelet", 850000, False],
    ["Women", "Accessories", "Socks", 180000, False],
    ["Women", "Accessories", "Scarf", 650000, False],
    ["Kids", "Formal Wear", "Girls Dress", 1800000, False],
    ["Kids", "Formal Wear", "Boys Suit", 2600000, False],
    ["Kids", "Casual Wear", "T-Shirt and Pants Set", 1100000, False],
    ["Kids", "Casual Wear", "T-Shirt and Shorts Set", 950000, False],
    ["Kids", "Casual Wear", "Long Sleeve and Pants Set", 1300000, False],
    ["Kids", "Casual Wear", "Hoodie", 1050000, True],
    ["Kids", "Casual Wear", "Winter Jacket", 2200000, True],
    ["Kids", "Shoes", "Sneakers", 1700000, False],
    ["Kids", "Shoes", "Crocs", 950000, False],
    ["Kids", "Shoes", "Leather Shoes", 1900000, False],
    ["Kids", "Shoes", "Ankle Boots", 2400000, True],
    ["Kids", "Accessories", "Socks", 120000, False],
    ["Kids", "Accessories", "Sunglasses", 550000, False],
    ["Kids", "Accessories", "Scarf", 350000, False],
    ["Kids", "Accessories", "Hat", 450000, False],
    ["Kids", "Accessories", "Girls Hair Clip", 150000, False]
]
for i in range(len(products)):
    products[i].append(random.randint(5, 30))
colors = [
    "Black",
    "White",
    "Gray",
    "Navy Blue",
    "Dark Green",
    "Brown",
    "Beige",
    "Cream",
    "Red",
    "Pink",
    "Light Blue",
    "Purple"
]
adult_sizes = [
    "XS", "S", "M", "L", "XL", "XXL", "XXXL"
]
kids_sizes = [
    "1-2 Years",
    "3-4 Years",
    "5-6 Years",
    "7-8 Years",
    "9-10 Years",
    "11-12 Years"
]
men_shoe_sizes = [
    "39", "40", "41", "42", "43", "44", "45", "46"
]
women_shoe_sizes = [
    "35", "36", "37", "38", "39", "40", "41", "42"
]
kids_shoe_sizes = [
    "22", "23", "24", "25", "26", "27", "28",
    "29", "30", "31", "32", "33", "34", "35"
]
perfume_sizes = [
    "30 ml", "50 ml", "100 ml"
]
models = [
    "Original",
    "Classic",
    "Formal",
    "Sport",
    "Casual",
    "Evening",
    "Luxury"
]
cart = []
discount_codes = [
    ["WELCOME10", 10],
    ["VIP20", 20]
]
def line():
    print("=" * 65)

def money(amount):
    return f"{amount:,} Toman"

def get_number(message, minimum, maximum):
    while True:
        value = input(message).strip()
        if value.isdigit():
            number = int(value)
            if minimum <= number <= maximum:
                return number
        print("Invalid input. Please try again.")

def select_option(title, options):
    line()
    print(title)
    line()
    for i in range(len(options)):
        print(i + 1, "-", options[i])
    print("0 - Back")
    choice = get_number(
        "Enter your choice: ",
        0,
        len(options)
    )
    if choice == 0:
        return None
    return options[choice - 1]

def get_sizes(product):
    gender = product[0]
    category = product[1]
    name = product[2]
    if category == "Shoes":
        if gender == "Men":
            return men_shoe_sizes
        elif gender == "Women":
            return women_shoe_sizes
        else:
            return kids_shoe_sizes
    elif category == "Accessories":
        if name == "Perfume":
            return perfume_sizes
        elif name == "Belt":
            return ["85 cm", "95 cm", "105 cm", "115 cm"]
        elif name == "Socks":
            if gender == "Kids":
                return ["Small", "Medium", "Large"]
            else:
                return ["36-39", "40-43", "44-46"]
        elif name == "Hat":
            return ["Small", "Medium", "Large"]
        else:
            return ["One Size"]
    else:
        if gender == "Kids":
            return kids_sizes
        else:
            return adult_sizes

def filter_products(gender, season, category):
    result = []
    for i in range(len(products)):
        product = products[i]
        if product[0] == gender:
            if product[1] == category:
                if product[4] == False:
                    result.append(i)
                elif season == "Autumn & Winter":
                    result.append(i)
    return result

def show_products(product_indexes):
    line()
    print("AVAILABLE PRODUCTS")
    line()
    if len(product_indexes) == 0:
        print("No products found.")
        return None
    for i in range(len(product_indexes)):
        index = product_indexes[i]
        product = products[index]
        print(
            f"{i + 1}. {product[2]}"
            f" | {product[0]}"
            f" | {money(product[3])}"
            f" | Stock: {product[5]}"
        )
    print("0 - Back")
    choice = get_number(
        "Select a product: ",
        0,
        len(product_indexes)
    )
    if choice == 0:
        return None
    return product_indexes[choice - 1]

def browse_products():
    while True:
        gender = select_option(
            "SELECT DEPARTMENT",
            genders
        )
        if gender is None:
            return
        while True:
            season = select_option(
                "SELECT SEASON",
                seasons
            )
            if season is None:
                break
            while True:
                category = select_option(
                    "SELECT CATEGORY",
                    categories
                )
                if category is None:
                    break
                while True:
                    available_products = filter_products(
                        gender,
                        season,
                        category
                    )
                    product_index = show_products(
                        available_products
                    )
                    if product_index is None:
                        break
                    add_to_cart(product_index)

def add_to_cart(product_index):
    product = products[product_index]
    line()
    print("PRODUCT DETAILS")
    print("Department:", product[0])
    print("Category:", product[1])
    print("Product:", product[2])
    print("Price:", money(product[3]))
    print("Available stock:", product[5])
    if product[5] == 0:
        print("Sorry! This product is out of stock.")
        return
    if product[2] == "Perfume":
        color = "Not Applicable"
    else:
        color = select_option(
            "SELECT COLOR",
            colors
        )
        if color is None:
            return
    size = select_option(
        "SELECT SIZE",
        get_sizes(product)
    )
    if size is None:
        return
    model = select_option(
        "SELECT MODEL",
        models
    )
    if model is None:
        return
    quantity = get_number(
        "Enter quantity (0 to cancel): ",
        0,
        product[5]
    )
    if quantity == 0:
        return
    found = False
    for i in range(len(cart)):
        if cart[i][0] == product_index:
            if cart[i][1] == color:
                if cart[i][2] == size:
                    if cart[i][3] == model:
                        cart[i][4] += quantity
                        found = True
                        break
    if found == False:
        cart.append([
            product_index,
            color,
            size,
            model,
            quantity
        ])
    products[product_index][5] -= quantity
    line()
    print("Product successfully added to cart!")
    print("Product:", product[2])
    print("Color:", color)
    print("Size:", size)
    print("Model:", model)
    print("Quantity:", quantity)
    print(
        "Total price:",
        money(product[3] * quantity)
    )

def calculate_total():
    total = 0
    for i in range(len(cart)):
        product_index = cart[i][0]
        price = products[product_index][3]
        quantity = cart[i][4]
        total += price * quantity
    return total

def show_cart():
    line()
    print("YOUR SHOPPING CART")
    line()
    if len(cart) == 0:
        print("Your cart is empty.")
        return
    for i in range(len(cart)):
        item = cart[i]
        product = products[item[0]]
        details = [
            ["Department", product[0]],
            ["Category", product[1]],
            ["Product", product[2]],
            ["Color", item[1]],
            ["Size", item[2]],
            ["Model", item[3]],
            ["Quantity", item[4]],
            ["Unit Price", money(product[3])],
            ["Total Price", money(product[3] * item[4])]
        ]
        print("Item", i + 1)
        print("-" * 40)
        for j in range(len(details)):
            print(
                details[j][0],
                ":",
                details[j][1]
            )
    line()
    print("Subtotal:", money(calculate_total()))

def edit_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
        return
    show_cart()
    choice = get_number(
        "Select item to edit (0 to cancel): ",
        0,
        len(cart)
    )
    if choice == 0:
        return
    index = choice - 1
    item = cart[index]
    product_index = item[0]
    product = products[product_index]
    edit_options = [
        "Change Color",
        "Change Size",
        "Change Model",
        "Change Quantity"
    ]
    while True:
        option = select_option(
            "EDIT PRODUCT",
            edit_options
        )
        if option is None:
            break
        elif option == "Change Color":
            if product[2] == "Perfume":
                print("Color is not applicable.")
                continue
            new_color = select_option(
                "SELECT NEW COLOR",
                colors
            )
            if new_color is not None:
                item[1] = new_color
                print("Color updated successfully.")
        elif option == "Change Size":
            new_size = select_option(
                "SELECT NEW SIZE",
                get_sizes(product)
            )
            if new_size is not None:
                item[2] = new_size
                print("Size updated successfully.")
        elif option == "Change Model":
            new_model = select_option(
                "SELECT NEW MODEL",
                models
            )
            if new_model is not None:
                item[3] = new_model
                print("Model updated successfully.")
        elif option == "Change Quantity":
            old_quantity = item[4]
            maximum_quantity = (
                product[5] + old_quantity
            )
            new_quantity = get_number(
                "Enter new quantity: ",
                1,
                maximum_quantity
            )
            difference = new_quantity - old_quantity
            product[5] -= difference
            item[4] = new_quantity
            print("Quantity updated successfully.")
        for i in range(len(cart)):
            if i != index:
                if cart[i][:4] == item[:4]:
                    cart[i][4] += item[4]
                    cart.pop(index)
                    print("Identical items merged.")
                    show_cart()
                    return
        show_cart()

def remove_from_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
        return
    show_cart()
    choice = get_number(
        "Select item to remove (0 to cancel): ",
        0,
        len(cart)
    )
    if choice == 0:
        return
    index = choice - 1
    item = cart[index]
    product_index = item[0]
    quantity = item[4]
    confirm = select_option(
        "REMOVE THIS PRODUCT?",
        ["Yes", "No"]
    )
    if confirm == "Yes":
        products[product_index][5] += quantity
        cart.pop(index)
        print("Product removed successfully.")
    else:
        print("Removal cancelled.")

def clear_cart():
    if len(cart) == 0:
        print("Your cart is already empty.")
        return
    confirm = select_option(
        "REMOVE ALL PRODUCTS?",
        ["Yes", "No"]
    )
    if confirm == "Yes":
        for i in range(len(cart)):
            product_index = cart[i][0]
            quantity = cart[i][4]
            products[product_index][5] += quantity
        cart.clear()
        print("Shopping cart cleared.")

def search_products():
    gender = select_option(
        "SEARCH DEPARTMENT",
        ["All Departments"] + genders
    )
    if gender is None:
        return
    season = select_option(
        "SELECT SEARCH SEASON",
        seasons
    )
    if season is None:
        return
    while True:
        line()
        print("PRODUCT SEARCH")
        keyword = input(
            "Enter product or category (0 to return): "
        ).strip().lower()
        if keyword == "0":
            return
        if keyword == "":
            print("Please enter a search keyword.")
            continue
        results = []
        for i in range(len(products)):
            product = products[i]
            if gender != "All Departments":
                if product[0] != gender:
                    continue
            if product[4] == True:
                if season == "Spring & Summer":
                    continue
            for j in range(3):
                if keyword in product[j].lower():
                    results.append(i)
                    break
        if len(results) == 0:
            print("No matching products found.")
        else:
            product_index = show_products(results)
            if product_index is not None:
                add_to_cart(product_index)

def automatic_discount(total):
    if total >= 20000000:
        return 15
    elif total >= 10000000:
        return 10
    elif total >= 5000000:
        return 5
    else:
        return 0

def check_discount_code():
    while True:
        code = input(
            "Enter discount code (0 to skip): "
        ).strip().upper()
        if code == "0" or code == "":
            return 0
        for i in range(len(discount_codes)):
            if code == discount_codes[i][0]:
                print("Discount code accepted!")
                print(
                    "Extra discount:",
                    discount_codes[i][1],
                    "%"
                )
                return discount_codes[i][1]
        print("Invalid discount code.")

def checkout():
    if len(cart) == 0:
        print("Your cart is empty.")
        return False
    show_cart()
    subtotal = calculate_total()
    auto_percent = automatic_discount(subtotal)
    auto_amount = subtotal * auto_percent // 100
    after_auto_discount = subtotal - auto_amount
    code_percent = check_discount_code()
    code_amount = (
        after_auto_discount * code_percent // 100
    )
    total_discount = auto_amount + code_amount
    final_total = subtotal - total_discount
    total_quantity = 0
    for i in range(len(cart)):
        total_quantity += cart[i][4]
    line()
    print("PAYMENT SUMMARY")
    line()
    print("Total items:", total_quantity)
    print("Subtotal:", money(subtotal))
    print(
        "Automatic discount:",
        str(auto_percent) + "%"
    )
    print("Automatic discount amount:", money(auto_amount))
    print(
        "Discount code:",
        str(code_percent) + "%"
    )
    print("Code discount amount:", money(code_amount))
    print("Total discount:", money(total_discount))
    print("Final total:", money(final_total))
    confirm = select_option(
        "CONFIRM PURCHASE",
        ["Yes", "No"]
    )
    if confirm != "Yes":
        print("Checkout cancelled.")
        return False
    receipt_number = random.randint(100000, 999999)
    line()
    print("FINAL RECEIPT")
    line()
    print("Receipt number:", receipt_number)
    line()
    for i in range(len(cart)):
        item = cart[i]
        product = products[item[0]]
        price = product[3]
        quantity = item[4]
        print(f"Item {i + 1}: {product[2]}")
        print("Department:", product[0])
        print("Category:", product[1])
        print("Color:", item[1])
        print("Size:", item[2])
        print("Model:", item[3])
        print("Quantity:", quantity)
        print("Unit price:", money(price))
        print("Item total:", money(price * quantity))
        print("-" * 45)
    line()
    print("Total different items:", len(cart))
    print("Total quantity:", total_quantity)
    print("Subtotal:", money(subtotal))
    print("Automatic discount:", money(auto_amount))
    print("Coupon discount:", money(code_amount))
    print("Total savings:", money(total_discount))
    print("FINAL AMOUNT:", money(final_total))
    print("Order status: Confirmed")
    line()
    print("Thank you for shopping!")
    line()
    cart.clear()
    return True

def main():
    line()
    print("WELCOME TO OUR STORE")
    line()
    browse_products()
    while True:
        line()
        print("MAIN MENU")
        line()
        menu = [
            "Continue Shopping",
            "Search Products",
            "View Shopping Cart",
            "Edit Shopping Cart",
            "Remove Product",
            "Clear Shopping Cart",
            "Checkout",
            "Exit"
        ]
        for i in range(len(menu)):
            print(i + 1, "-", menu[i])
        choice = get_number(
            "Enter your choice: ",
            1,
            len(menu)
        )
        if choice == 1:
            browse_products()
        elif choice == 2:
            search_products()
        elif choice == 3:
            show_cart()
        elif choice == 4:
            edit_cart()
        elif choice == 5:
            remove_from_cart()
        elif choice == 6:
            clear_cart()
        elif choice == 7:
            completed = checkout()
            if completed == True:
                break
        elif choice == 8:
            if len(cart) > 0:
                confirm = select_option(
                    "You have items in your cart. Exit?",
                    ["Yes", "No"]
                )
                if confirm != "Yes":
                    continue
                for i in range(len(cart)):
                    product_index = cart[i][0]
                    quantity = cart[i][4]
                    products[product_index][5] += quantity
                cart.clear()
            print("Thank you for visiting Our Shop!")
            break

if __name__ == "__main__":
    main()

