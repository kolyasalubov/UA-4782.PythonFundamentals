import math

def calculate_rectangle_area(width, height):
    """Обчислює площу прямокутника."""
    return width * height

def calculate_triangle_area(base, height):
    """Обчислює площу трикутника."""
    return 0.5 * base * height

def calculate_circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * (radius ** 2)

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = input("Введіть номер вашого вибору (1-3): ")
    
    if choice == "1":
        w = float(input("Введіть ширину прямокутника: "))
        h = float(input("Введіть висоту прямокутника: "))
        area = calculate_rectangle_area(w, h)
        print(f"Площа прямокутника: {area:.2f}")
        
    elif choice == "2":
        b = float(input("Введіть основу трикутника: "))
        h = float(input("Введіть висоту трикутника: "))
        area = calculate_triangle_area(b, h)
        print(f"Площа трикутника: {area:.2f}")
        
    elif choice == "3":
        r = float(input("Введіть радіус кола: "))
        area = calculate_circle_area(r)
        print(f"Площа кола: {area:.2f}")
        
    else:
        print("Неправильний вибір! Будь ласка, запустіть програму знову та оберіть 1, 2 або 3.")

if __name__ == "__main__":
    main()