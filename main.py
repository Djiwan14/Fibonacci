def menu():
    print("Set of commands for our series")
    print("1. Generate series with 2 given numbers: ")
    print("2. Generation of the Fibonacci up to given limit: ")
    print("3. Check if given number in: ")
    print("4. Exit")
    choice = input("Please choose an option to continue: ")

    if choice == "1":
        array = []
        input1 = int(input("First number: "))
        input2 = int(input("Second number: "))
        sizeOfArray = int(input("Size of array: "))
        array.append(input1)
        array.append(input2)
        for i in range(sizeOfArray - 2):
            array.append(array[i] + array[i + 1])
        return array

    elif choice == "2":
        limit = int(input("Please insert limit: "))
        array = [0, 1]
        while True:
            next_value = array[-1] + array[-2]
            if next_value > limit:
                break
            array.append(next_value)
        return array

    elif choice == "3":
        number = int(input("Please insert number: "))
        limit = int(input("Please insert limit: "))
        array = [0, 1]
        while True:
            next_value = array[-1] + array[-2]
            if next_value > limit:
                break
            array.append(next_value)
        if number in array:
            return True
        else:
            return False
print(menu())