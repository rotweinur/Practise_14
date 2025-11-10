input_string = input()
string_list = input_string.split()
lst = []
for item in string_list:
    num = int(item)
    lst.append(num)

command = input()
direction = command[0]
steps = int(command[1:])
steps = steps % len(lst)

if direction == 'R':
    lst = lst[-steps:] + lst[:-steps]
elif direction == 'L':
    lst = lst[steps:] + lst[:steps]

print(lst)