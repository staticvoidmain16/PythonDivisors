user_input = int(input("Please enter a number: "))
new_list = []

num_range = range(2, user_input + 1)

for x in num_range:
    if user_input % x == 0:
        new_list.append(x)

print("")
print("%d has divisors of:" % (user_input), new_list)

        
