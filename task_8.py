def process_string(s):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

s = input()
result = process_string(s)
print(result)