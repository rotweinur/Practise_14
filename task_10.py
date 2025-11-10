input_str1 = input()
lst1_str = input_str1.split()
lst1 = []
for num_str in lst1_str:
    num = int(num_str)
    lst1.append(num)

input_str2 = input()
lst2_str = input_str2.split()
lst2 = []
for num_str in lst2_str:
    num = int(num_str)
    lst2.append(num)

range_input = input()
range_str = range_input.split()
start = int(range_str[0])
end = int(range_str[1])

segment = lst1[start+1:end+1]
lst2.extend(segment[::-1])
del lst1[start+1:end+1]

print(lst1)
print(lst2)