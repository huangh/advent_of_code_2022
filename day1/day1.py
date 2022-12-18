
# breakpoint()
ii = 0
elves = []
# a = ''
# b = '123'

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    # for i in range(7):
    #     print(lines[i])
    
    #     print("new line")

    # if '\n' in lines[7]:
    #     print("new line"
print(lines)
print(elves)
elves.append(0)
# print("aa")
# print(elves)
for line in lines:
    # print(line)
    # if 
    if line == '':
        print('next')
        ii = ii+1
        elves.append(0)
    else:
        # print("zero")
        elves[ii] = elves[ii] + int(line)
    
#     if line is "\n"
print("Elves")
print(elves)
# print(max(elves))
# elves = elves.sort()
elves.sort()
breakpoint()
print(elves)

