#Dave.py
import os

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

course = [
    "BS in Information Technology (BSIT)",
    "BS in Civil Engineering (BSCE)",
    "BS in Mechanical Engineering (BSME)",    
    "BS in Industrial Technology (Culinary Arts)",
    "BS in Industrial Technology (Electronics)",
]

while True:
    print("---------------------------")
    print("     School Management")
    print("---------------------------")
    print("1. List of Course")
    print("2. Register of Students")
    print("3. List of Students")
    print("4. DataBase")
    print("5. Exit")
    print("---------------------------")
    choice = int(input("Choice: "))
    clear()

    if choice == 1:
        print("---------------------------")
        print("     List of Course")
        print("---------------------------")
        print("1. BS in Information Technology (BSIT)")
        print("2. BS in Civil Engineering (BSCE)")
        print("3. BS in Mechanical Engineering (BSME)")    
        print("4. BS in Industrial Technology (Culinary Arts)")
        print("5. BS in Industrial Technology (Electronics)")
        print("---------------------------")
        print("0. Return ")
        print("---------------------------")
        choice = int(input("Choice: "))
        clear()

    if choice == 2:
        print("---------------------------")
        print("   Register of Students")
        print("---------------------------")
        print("        List of Course")
        print("1. BS in Information Technology (BSIT)")
        print("2. BS in Civil Engineering (BSCE)")
        print("3. BS in Mechanical Engineering (BSME)")    
        print("4. BS in Industrial Technology (Culinary Arts)")
        print("5. BS in Industrial Technology (Electronics)")
        print("---------------------------")
        name1 = input("Name Student 1: ")
        age1 = input("Age: ")
        add1 = input("Address: ")
        email1 = input("Email: ")
        course1_choice = int(input("Course (1-5): "))
        course1 = course[course1_choice - 1]
        print("---------------------------")
        name2 = input("Name Student 2: ")
        age2 = input("Age: ")
        add2 = input("Address: ")
        email2 = input("Email: ")
        course2_choice = int(input("Course (1-5): "))
        course2 = course[course2_choice - 1]
        print("---------------------------")
        name3 = input("Name Student 3: ")
        age3 = input("Age: ")
        add3 = input("Address: ")
        email3 = input("Email: ")     
        course3_choice = int(input("Course (1-5): "))
        course3 = course[course3_choice - 1]  
        clear()
        print("---------------------------")
        print("   Register Successfully")
        print("---------------------------")

    if choice == 3:
        print("---------------------------")
        print("     List of Students")
        print("---------------------------")
        print(f"Student 1: {name1}")
        print("---------------------------")
        print(f"Student 2: {name2}")
        print("---------------------------")
        print(f"Student 3: {name3}")
        print("---------------------------")
        print("0. Return")
        print("---------------------------")
        Choice = input("Choice: ")
        clear()

    if choice == 4:
        print("---------------------------")
        print("         DataBase")
        print("---------------------------")
        print("        Student 1")
        print(f"Name: {name1}")
        print(f"Age: {age1}")
        print(f"Address: {add1}")
        print(f"Email: {email1}")
        print(f"Course: {course1}")
        print("---------------------------")
        print("        Student 2")
        print(f"Name: {name2}")
        print(f"Age: {age2}")
        print(f"Address: {add2}")
        print(f"Email: {email2}")
        print(f"Course: {course2}")
        print("---------------------------")
        print("        Student 3")
        print(f"Name: {name3}")
        print(f"Age: {age3}")
        print(f"Address: {add3}")
        print(f"Email: {email3}")
        print(f"Course: {course3}")
        print("---------------------------")
        print("0. Return")
        print("---------------------------")
        choice = input("Choice: ")
        clear()

    if choice == 5:
        print("---------------------------")
        print("   Thank you & Goodbye!")
        print("---------------------------")
        break
#Dave.py
