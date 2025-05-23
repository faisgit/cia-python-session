# while loop
# count = 0
# while count < 10:
#     # print("crashing the system...")
#     print(count)
#     count = count + 1

# a = 10
# while a >= 10:
#     print(a)
# else:
#     print(f"a = {a}")


# a = 45
# while(65):
#     if(a == 55):
#         a = a + 1
#         continue
#     else:
#         print(a)
        
#     a = a + 1
# else:
#     print(a)

# marks = [78, 65, 90, 65, 88, 92, 65, 76, 81, 65, 59, 65, 73, 85]
# marksListLen = len(marks)
# z = 0
# while(True):
#     if(z == 65):
#         z = z+ 1
#         continue
#     else:
#         print(z)
#         z = z+ 1


# for(z  in )
# x = ""       
# for i in "chetanya":
#     x+=i
# print(x)
# min = int(input("Enter a minimum number : "))
# max = int(input("Enter a maximum number : "))
# num = int(input("Enter a number: "))
# for i in range(min,max + 1):
#     print(i * num)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# for key in person:
#     print(key)

for key, value in person.items():
    if(key == 'first_name' or key == 'last_name' or key == 'skills'):
        print(f"{key} - {value}")

