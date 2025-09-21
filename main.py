balance = 0
inventory = {}

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Shop")
        print("2. Village")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            shop()
        elif choice == "2":
            village()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def shop():
    while True:
        print("\n=== SHOP ===")
        print("1. Pickaxe - 150 - Farm Faster by 1.1x speed")
        print("2. Back to Main Menu")
        
        displayInventory()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You bought a pickaxe!")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def village():
    while True:
        print("\n=== VILLAGE ===")
        print("1. Break Rock")
        print("2. Cut Tree")
        print("3. Mine Ore")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            breakRock()
        elif choice == "2":
            cutTree()
        elif choice == "3":
            mineOre()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def breakRock():
    rock = 5
    print("\nYou are breaking a rock")
    while rock > 1:
        input("Press Enter to break rock")
        rock -= 1
        print(f"You have {rock} hits left")
    
    print("You have broken the rock")
    addToInventory("Rock", 1)
    displayInventory()

def cutTree():
    print("You cut down a tree")
    addToInventory("Wood", 1)
    displayInventory()

def mineOre():
    print("You mined some ore")
    addToInventory("Iron", 1)
    displayInventory()

def addToInventory(item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"You collected {quantity} {item}")

def displayInventory():
    print(f"Balance: {balance}")
    if inventory:
        items = [f"{item}:{quantity}" for item, quantity in inventory.items()]
        print(f"Inventory: {', '.join(items)}")
    else:
        print("Inventory: Empty")

if __name__ == "__main__":
    main()