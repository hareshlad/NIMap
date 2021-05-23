def sortListByLength(lst):
    lst.sort(key=len)
    return lst

n=int(input("Enter number of strings "))
if n<=0:
    print("Invalid Input")
else:
    input_string=input("Enter the list elements separated by comma")
    input_list= ['']*n
    input_list =  input_string.split(',')
    out_list=sortListByLength(input_list)
    print(out_list)
    print(out_list[0])

