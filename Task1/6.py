def is_leap(year):
    leap = False
    result = True 
    if year%4 ==0:
     if year%100!=0:
        return result 
     elif year%400 ==0:
        return result
     else :
        return leap
    else:   
       return leap
year = int(input())
print(is_leap(year))