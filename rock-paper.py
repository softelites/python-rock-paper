import random
lst = ["rock","paper","scissors"]
for i in range(0,10,1):
    cpu  = random.choices(lst)
    user = input("*************************************** \n Rock, Paper & scissors \n 1. rock \n 2. paper \n 3. scissors\n 4. exit \n Your Choice =  ")
    print("\n")
    #first case
    if user=='rock' and cpu == 'paper':
        print("User = {0}\ncpu = {1}\nCPU Wins ! \n".format(user,cpu))
    elif user=='rock' and cpu == 'rock':
        print("User = {0}\ncpu = {1}\nGame Tied ! \n".format(user,cpu))
    elif user=='rock' and cpu == 'scissors':
        print("User = {0}\ncpu = {1}\nUser Wins ! \n".format(user,cpu))
    #secound case
    elif user=='paper' and cpu == 'paper':
        print("User = {0}\ncpu = {1}\nGame Tied ! \n".format(user,cpu))
    elif user=='paper' and cpu == 'rock':
        print("User = {0}\ncpu = {1}\nUser Wins ! \n".format(user,cpu))
    elif user=='paper' and cpu == 'scissors':
        print("User = {0}\ncpu = {1}\nCPU Wins ! \n".format(user,cpu))
    #third case
    elif user=='scissors' and cpu == 'paper':
        print("User = {0}\ncpu = {1}\nUser Wins ! \n".format(user,cpu))
    elif user=='scissors' and cpu == 'rock':
        print("User = {0}\ncpu = {1}\nCPU Tied ! \n".format(user,cpu))
    elif user=='scissors' and cpu == 'scissors':
        print("User = {0}\ncpu = {1}\nGame Tied ! \n".format(user,cpu))
