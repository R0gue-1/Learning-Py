# 3 while looops and how they evaluate true of false condition 


value = 'True'

# while value:
#     print(value)
#     value = False

value = 'y'
count = 0

while value: # this checks if value exists]\ or is it true
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0 # 0 == false
        continue