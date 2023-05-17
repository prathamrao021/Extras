from itertools import combinations, permutations

arr_all_username = []
def username_gen(fname, lname, bday, pname=""):
    arr_used_fields = [fname, lname, bday[:2], bday[3:5], bday[-4:], pname]
    arr_temp = []
    for n in range(1, len(arr_used_fields)+1):
        arr_temp += list(permutations(arr_used_fields,n))
    # print(arr_temp)    
    for i in range(len(arr_temp)):
        temp_str = ""
        for j in range(len(arr_temp[i])):
            temp_str += arr_temp[i][j]
        arr_all_username.append(temp_str)
    print(arr_all_username)

fname = input("Enter your first name*:")
lname = input("Enter your last name*:")
bday = input("Enter your birthday(dd/mm/yyyy)*:")
pname = input("Enter your alternative name:")
print(type(pname))
if (pname == ""):
    username_gen(fname, lname, bday)
else:
    username_gen(fname, lname, bday, pname)
