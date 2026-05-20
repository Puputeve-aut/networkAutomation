def formatName(fname, lname):
    if fname == "" or lname =="":
        return "You did not provide valid inputs"
    else:
        formatedFName = fname.title()
        formatedLName = lname.title()
        return f"{formatedFName} {formatedLName}"
    
print(formatName(input("What is your first name? "), input("What is your last name? ")))