products = [ 
{"id": 1, "name": "Laptop", "price": 45000}, 
{"id": 2, "name": "Smartphone", "price": 15000}, 
{"id": 3, "name": "Headphones", "price": 2000}, 
{"id": 4, "name": "Keyboard", "price": 1200}, 
{"id": 5, "name": "Mouse", "price": 800}, 
{"id": 6, "name": "Charger", "price": 500}, 
{"id": 7, "name": "USB Cable", "price": 300}, 
{"id": 8, "name": "Backpack", "price": 2500} 
] 
cart=[]
def viewProducts():
    print('view products is executed')
    for p in products:
        # print(p["id"],p["name"],p["price"])
        print(f"product name is {p['name']} and price is {p['price']}")
def viewCart(cart):
    for item in cart:
        print(item)
def addToCart(products,cart,product_id,quantity):
    product=None
    for items in products:
        if items["id"]==product_id:
            product=items
            break
        if not product:
            print("THe cart is empty")  

    for item in cart:
        if item["id"]==product_id:
            item["quantity"]+=quantity
    new_item={
        "id":product["id"],
        "name":product["name"],
        "price":product["price"]*quantity,
        "quantity":quantity

    }
    cart.append(new_item)
    print(f"UPdated items are {new_item["name"]} and {new_item["price"]}")
    viewCart(cart)

def updateCart(cart):    
    id=int(input("Enter the ID"))
    for item in cart:
        if item['id']==id:
            item['quantity']+=1
            print(" Item Quantity Updated sucessfully")
            break
    else:
            print("Product Not Found")
def removeFromCart():
    print("remove from cart is executed")
def checkOut():
    print("checkout")

def menu():
    ip=int(input("enter choice :"))
    if ip ==1:
        viewCart()
    elif ip==2:
        addToCart(products,cart,1,2)
    elif ip==3:
        viewProducts()
    elif ip==4:
        updateCart(cart)
    elif ip==5:
        removeFromCart()
    elif ip==6:
        checkOut()
    else:
        print('invalid option')
menu()
