def is_leap_year(year):
    """Calculate if the year is leap or not."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False
    
    

print(is_leap_year(int(input("Pleas give me a year to check: "))))