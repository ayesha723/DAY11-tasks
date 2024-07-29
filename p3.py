def convert_var():
    int_in=input("Enter a float value")
    try:
        x=int(int_in)
        result=10+x
        print(result)
    except ValueError:
        print("Enter a valid integer")
convert_var()