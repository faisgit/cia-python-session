# a = 3
# b = a
# print(a)
# print(b)
# a = 4
# print(b)



# name = input("Enter your name:- ")
# print(f"my name is {name}")


# a = int(input("Enter First No:  "))
# b = int(input("Enter Second No: "))
# print(f"{a} + {b} = {a + b}")

# Write a Code which gives grade to students according to their grad
# 90-100 --> Grade
# 70-89 --> Grade
# 60-69 --> Grade
# 50-59 --> Grade 
# 0-49 --> Grade


# print("ell world")

# from ab import a
# print(a)

# a = "abcd"
# print(bool(a))

# print(9 == int(9.3))

# print(0 == True)

# print(len("abc") == len("pqr"))


# String Formating
# a =3
# b = 5
# print("{} + {} = {}".format(a,b,a + b)



user = input("Enter a Character: ")

if(len(user) == 1):
    if(user == 'a' or user == 'e' or user  == "i" or user== "o" or user == "u"):
        print(f"{user} is a vowel")
    else:
        print(f"{user} is a consonant")
else:
    print("Invalid Input")