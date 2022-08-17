chars = ['A','K','A','S','H']
print(len(chars))
left = 0
right = len(chars) - 1

while left < right:
    tmp = chars[left]
    chars[left] = chars[right]
    chars[right] = tmp
    left +=1
    right -= 1
    
print(chars)

