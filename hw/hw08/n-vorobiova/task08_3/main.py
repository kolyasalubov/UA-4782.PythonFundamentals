import calculator

def main():
    print("Яку фігуру ви хочете порахувати?")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = input("Введіть номер (1, 2 або 3): ")
    
    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        res = calculator.rectangle_area(a, b)
        print(f"Площа прямокутника: {res}")
        
    elif choice == "2":
        a = float(input("Введіть основу трикутника a: "))
        h = float(input("Введіть висоту трикутника h: "))
        res = calculator.triangle_area(a, h)
        print(f"Площа трикутника: {res}")
        
    elif choice == "3":
        r = float(input("Введіть радіус кола r: "))
        res = calculator.circle_area(r)
        print(f"Площа кола: {res}")
        
    else:
        print("Некоректний вибір!")

if __name__ == "__main__":
    main()