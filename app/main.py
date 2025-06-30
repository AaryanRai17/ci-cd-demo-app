
from calculator import add, subtract, multiply, divide

def display_menu():
    print("\n📊 Calculator Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_input():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return None, None

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '5':
            print("👋 Exiting. Goodbye!")
            break

        a, b = get_input()
        if a is None or b is None:
            continue

        try:
            match choice:
                case '1':
                    print(f"✅ Result: {add(a, b)}")
                case '2':
                    print(f"✅ Result: {subtract(a, b)}")
                case '3':
                    print(f"✅ Result: {multiply(a, b)}")
                case '4':
                    print(f"✅ Result: {divide(a, b)}")
                case _:
                    print("❌ Invalid option.")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
