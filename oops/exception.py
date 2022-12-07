number = 10
while True:
    try:
        n = int(input("Enter a number"))
        if n < number:
            raise ValueTooSmallError
        elif n >number:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, Try again!")
        print("Congratulations! You have entered correct value")

