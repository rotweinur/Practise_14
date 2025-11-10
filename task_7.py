input_string = input()
string_list = input_string.split()
numbers = []
for item in string_list:
    num = int(item)
    numbers.append(num)

even_sum = sum(x for x in numbers if x % 2 == 0)
odd_sum = sum(x for x in numbers if x % 2 != 0)
print(even_sum, odd_sum)