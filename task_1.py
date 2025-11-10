numbers = []
for i in range(10):
    num = int(input())
    numbers.append(num)

new_list = []
for i in range(8):
    sum_three = numbers[i] + numbers[i+1] + numbers[i+2]
    new_list.append(sum_three)

print(new_list)