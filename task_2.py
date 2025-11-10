input_string = input()

string_list = input_string.split()

numbers = []
for item in string_list:
    num = int(item)
    numbers.append(num)

numbers.remove(3)

print(numbers)