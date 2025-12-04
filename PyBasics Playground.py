#Function to handle "Conditional" option
def option_one():
    print("\nYou selected option 1!")
    print("Simulating Conditionals Statement...\n")
    conditional()
 
 #Functio to handle "Loop" option
def option_two():
    print("\nYou selected option 2!")
    print("Simulating Python Loops...\n")
    loop()
 
 #Function to handle "List" option
def option_three():
    print("\nYou selected option 3!")
    print("Simulating Python Lists...\n")
    lists()
 
#Function that adds two numbers entered by the user 
def python_function(num1, num2):
    return num1 + num2
 
 #Function to handle "Function" option
def option_four():
    print("\nYou selected option 4!")
    print("Simulating Python Functions...\n")
    result = python_function(1, 2)
    print("The sum is:", result)
 
 #Function using conditinal statements to assign grade
def conditional():
    score = int(input("Enter Your Score: ")) #Asks user for score and convert it to integer
    if score >= 90:
        grade = "A👌"
    elif score >= 80:
        grade = "B☝️"
    elif score >= 70:
        grade = "C👊"
    else:
        grade = "F👎"
    print("Your grade is:", grade) #Show the grade
 
#Function to show how list works 
def lists():
    fruits = []
    favorite = input("What's your favorite fruit?🍎 ")
    fruits.append(favorite)
    print("My Favorite Fruit is", fruits)
 
 #Function to demomnstrate loops
def loop():
    # Demonstrate a for loop
    print("Using a for loop to count from 1 to 5:")
    for i in range(1, 6): # Will repeat 5 times (1 to 5)
        print(f"for loop count: {i}")

    # Demonstrate a while loop
    print("\nNow using a while loop to count from 1 to 5:")
    count = 1
    while count <= 5: # Loop continues as long as count <= 5
        print(f"while loop count: {count}")
        count += 1 # Increase count by 1 each time
 
 
def python_function(num1, num2): #Asks user to input two numbers and convert them into integers
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    addition = num1 + num2 #Add the numbers 
    return addition #Return the result
 
 #Main program menu loop
def main_menu():
    while True:
        print("👾=== MAIN MENU ===👾")
        print("1. Run Conditionals Module")
        print("2. Run Loops Module")
        print("3. Run Lists Module")
        print("4. Run Function Module")
        print("0. Exit")
        choice = input("Enter your choice: ") #Let the user input its choice
 
        if choice == "1":
            option_one() #Run Conditionals
        elif choice == "2":
            option_two() #Run Loops
        elif choice == "3":
            option_three() #Run Lists
        elif choice == "4":
            option_four() #Run Functions
        elif choice == "0":
            print("Exiting, Thank You for trying our program... Goodbye!👋")
            break #Exits the loop and program
        else:
            print("\n🗙Invalid choice! Please enter a valid number🗙.\n")
 
 #Start the program by calling the menu
main_menu()