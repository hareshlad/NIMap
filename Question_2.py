def count_chars(str):
     upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          else: special_ctr += 1
     return upper_ctr, lower_ctr, number_ctr, special_ctr
           
str = input("Enter sring: ")
print("Password contains: ")
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)
if len(str) <8:
    print(8-len(str),' more characters should be added')
elif u>0 and l> 0 and n> 0 and s> 0:
    print('Strong password, good to go!')
else:
    print('Weak password')
