import task2_calc

while True:
    answer = input("Hi, if you would like to calculate the area of a triangle, rectangle or circle just write its name - ")
    answer = answer.lower()

    if answer == 'triangle':
        x = float(input('Enter the first side length of your triangle - '))
        y = float(input('Enter the second side length of your triangle - '))
        z = float(input('Enter the third side length of your triangle - '))
        area = task2_calc.area_of_triangle(x,y,z)

        if area is None:
            print("Such triangle cannot exist.")
            break
        else:
            print("The area of your triangle is", area)
            break
    
    elif answer == 'rectangle':
        width = float(input('Enter the length of your rectangle - '))
        length = float(input('Enter the width of your rectangle - '))

        print("The area of your rectangle is", task2_calc.area_of_rectangle(width, length))
        break
    
    elif answer == 'circle':
        radius = float(input('Enter the radius of your circle - '))
    
        print("The area of your circle is", task2_calc.area_of_circle(radius))
        break
    
    else:
        print("It seems you have entered some other figure, try again!" + '\n')
