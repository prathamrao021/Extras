import numpy as np
from numpy import random
import random


def password_generator(pass_len):
    
    arr_small_alpha = "abcdefghijklmnopqrstuvwxyz"
    arr_nums = "0123456789"
    arr_cap_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr_spec_char = "!@#$%^&*"
    pass_len = int(pass_len)
    arr_everything = [arr_small_alpha, arr_nums, arr_cap_alpha, arr_spec_char]
    actual_password = ''
    arr_ran_gen = []
    arr_check = np.arange(0,4)
    while True:
        if (len(actual_password)==pass_len):
            break
        elif(len(actual_password)<pass_len):
            ran = random.randint(0,3)
            # print("Random:",ran)
        if (len(arr_check)>0):
            if int(ran) in arr_check:
                actual_password += str(random.choice(arr_everything[ran]))
                arr_check = np.delete(arr_check, np.where(arr_check == ran))
                # print(arr_check)
            elif ran not in arr_check:
                if (pass_len - len(actual_password) == len(arr_check)):
                    # print("bal bal baache")
                    for i in arr_check:
                        actual_password += str(random.choice(arr_everything[i]))
                        arr_check = np.delete(arr_check, np.where(arr_check == i))
                elif (pass_len - len(actual_password) > len(arr_check)):
                    # print("chalega")
                    actual_password += str(random.choice(arr_everything[ran]))
                    arr_check = np.delete(arr_check, np.where(arr_check == ran))
        elif(len(arr_check)==0):
            actual_password += str(random.choice(arr_everything[ran]))
    print("Password: "+actual_password)
    

pass_len = int(input("Enter the length of password:"))
if (pass_len>=8):
    password_generator(str(pass_len))
else:
    print("Password should be of length 8 or higher.")