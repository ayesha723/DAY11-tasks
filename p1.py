def convert_var():
    str_in=input("Enter a string value")
    try:
        x=int(str_in)
        result=10+x
        print(result)
    except ValueError:
        print("Enter a valid integer")
convert_var()
