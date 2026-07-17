orders = []
dishes = {
    "1": "Noodles",
    "2": "Pizza",
    "3": "Burger",
    "4": "Briyani",
    "5": "SoyaChaap"
}
def showMenu():
    print("\n\n.............Menu.............\n")
    print("\n1. Noodles")
    print("\n2. Pizza")
    print("\n3. Burger")
    print("\n4. Briyani")
    print("\n5. SoyaChaap")

    cho = input("\n What do you want : ")
    orders.append(dishes[cho])
    ask = input("Do you want to order more? (y/n): ")
    if(ask == "y"):
        showMenu()
    else:
        print("\nHere is your order: \n")
        billing()
        
def billing():
    if not orders:
        print("\nNo orders to bill.")
        return
    print("\n"+ "="*30)
    print("\t	BILL")
    print("="*30)
    sum = 0
    for item in orders:
        if(item == dishes["1"]):
            price = 500
            print(f"\n {item} \t {price}")
            sum += price
        elif(item == dishes["2"]):
            price = 550
            print(f"\n {item} \t {price}")
            sum += price
        elif(item == dishes["3"]):
            price = 650
            print(f"\n {item} \t {price}")
            sum += price
        elif(item == dishes["4"]):
            price = 750
            print(f"\n {item} \t {price}")
            sum += price
        elif(item == dishes["5"]):
            price = 850
            print(f"\n {item} \t {price}")
            sum += price
    print(f"\n\n Total \t {sum}")        
    print("\n"+ "="*30)
    
showMenu()
