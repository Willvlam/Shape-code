import math
pi = float(3.14)
choice = input('Angles(1), Percent(2), Quadratic(3), or pythagorean theorum (4) : ')

# --- QUADRATIC SOLVER --- 
if choice == '3':
    while True:
        print("-" * 20)
        print("Equation format: ax^2 + bx + c = 0")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        
        # Calculate the discriminant
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"\n>>> TWO REAL ROOTS: x = {round(x1, 2)} and x = {round(x2, 2)}")
        elif discriminant == 0:
            x = -b / (2 * a)
            print(f"\n>>> ONE REAL ROOT: x = {round(x, 2)}")
        else:
            # Handling imaginary numbers (Integrated 2 specialty!)
            real_part = round(-b / (2 * a), 2)
            imag_part = round(math.sqrt(abs(discriminant)) / (2 * a), 2)
            print(f"\n>>> IMAGINARY ROOTS: {real_part} + {imag_part}i and {real_part} - {imag_part}i")
            
        if input('\nNext? (y/n): ').lower() == 'n':
            break

# --- PERCENT SECTION (STAYS THE SAME) ---
elif choice == '2':
    while True:
        print("-" * 20)
        P = float(input('Base number (P): ')) 
        r_raw = float(input('Percent (r): '))
        r = r_raw / 100
        t = float(input('Years (t): '))
        c_type = input('Compounding: Yearly/Monthly/etc(1) or Continuous(2): ')
        direction = input('Growth(1) or Decay(2): ')
        
        if c_type == '2':
            answer = P * math.exp(r * t) if direction == '1' else P * math.exp(-r * t)
        else:
            n_in = input('Enter n (Enter for 1): ')
            n = float(n_in) if n_in != "" else 1.0
            answer = P * (1 + (r/n))**(n*t) if direction == '1' else P * (1 - (r/n))**(n*t)
            
        print(f"\n>>> RESULT: {round(answer, 2)}")
        if input('\nNext? (y/n): ').lower() == 'n': break

# --- ANGLES SECTION (STAYS THE SAME) ---
elif choice == '1':
    type_ang = input('Interior(1) or Exterior(2): ')
    while True:
        print("-" * 20)
        sides = int(input("Sides/Angles: "))
        answer = ((sides - 2) * 180 / sides) if type_ang == '1' else (360 / sides)
        print(f"\n>>> RESULT: {round(answer, 2)}")
        if input('\nNext? (y/n): ').lower() == 'n': 
            break
elif choice == '4': 
    while True:
        abac = float(input('do you have a and b (1) or a and c (2) '))
        if abac == '1':
            a_side = float(input('what is a '))
            b_side = float(input('what is b '))
            answer = ((a_side ** 2 + b_side ** 2)/2 )
            print(answer)
        elif abac == '2':
            a_side = float(input('what is a '))
            c_side = float(input('what is c '))
            answer = ((c_side ** 2 - a_side ** 2)/2 )
            print(answer)
        if input('\nNext? (y/n): ').lower() == 'n': 
            break
