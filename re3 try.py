try:
    import re
    x = input("enter a 10 digit no:")
    if re.search("^[M][H][-][0-9][0-9][-][0-9]{4,4}$",x):
       print("ur no. is:",x)
    else:
       print("incorrect no.")
except ValueError:
    print("value entered not valid")
