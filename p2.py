def convert_var():
    int_in=input("Enter an integer value")
    try:
        x=str(int_in)
        result='hello'+x
        print(result)
    except ValueError:
        print("Enter a valid string")
convert_var()