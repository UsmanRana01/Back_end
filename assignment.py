num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# Question 01:

for num in num_list:
    print(num)

# Question 02:

for num in num_list:
    if (num > 45):
        print(num)

# Question 03:

for num in num_list:
    if(num > 45):
        print("Over 45: ",num)
    else:
        print ("Under 45: ",num)

# Question 04:

for index, num in enumerate(num_list):
    if(num == 36):
        print("Number found at position: ",index ,":",num)

#Question 05, 06, 07, 08:

count = 0
for index, num in enumerate(num_list):
    if(num == 36):
        count += 1
        print("Number found at position: ",index ,":",num)
        break

print ("Total Count: ",count)
