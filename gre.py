for i in range(10):
    number = "5" + str(i) + "5"
    print("_____________________________________")
    print(number.rjust(4))
    print(" *5".rjust(4))
    print("____")
    print(int(number) * 5)
    print("_____________________________________")
