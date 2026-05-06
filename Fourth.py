def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%400==0):
        return True
    if(year%4!=0 or year%100==0):
        return False    
    else:
        return True    
year = int(input())
print(is_leap(year))