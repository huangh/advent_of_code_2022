
# breakpoint()

#  a      b      c
#  x      y      z
# rock paper scissor
#  1     2      3
#

score = 0

def my_score(me):
    if me == 'X':
        return 0
    if me == 'Y':
        return 3
    if me == 'Z':
        return 6

def wlt(them,me):
    if them == 'A' and me == 'Y':
        return 6
    if them == 'B' and me == 'Z':
        return 6
    if them == 'C' and me == 'X':
        return 6
    if them == 'A' and me == 'X':
        return 3
    if them == 'B' and me == 'Y':
        return 3
    if them == 'C' and me == 'Z':
        return 3                          
    return 0

#  a      b      c
# rock paper scissor
#  1     2      3
#
# x = lose y draw z win

def wlt2(them,me):
    # rock
    if them == 'A' and me == 'X':
        return 3         
    if them == 'A' and me == 'Y':
        return 1 
    if them == 'A' and me == 'Z':
        return 2         

    #paper
    if them == 'B' and me == 'X':
        return 1         
    if them == 'B' and me == 'Y':
        return 2 
    if them == 'B' and me == 'Z':
        return 3 
    
    #scissors
    if them == 'C' and me == 'X':
        return 2         
    if them == 'C' and me == 'Y':
        return 3 
    if them == 'C' and me == 'Z':
        return 1                         

# # def lose(them,me):
# #     if them == 'A' and me == 'Z':
# #         return 0
# #     if them == 'B' and me == 'X':
# #         return 0
# #     if them == 'C' and me == 'Y':
# #         return 0        
# #     return 0

# def tie(them,me):
      
#     return 0

with open("test_data/input.txt") as file:
    # rstrip gets rid of the new line char
    lines = [line.rstrip() for line in file]
    for line in lines:
        them, me = line.split()
        # print(my_score(me))
        # print(wlt2)/
        # part 1
        # score = score + my_score(me) + wlt(them, me)
        # part 2
        score = score + my_score(me) + wlt2(them, me)
        
    #     print("new line")
print(score)


    # if '\n' in lines[7]:
    #     print("new line"
# print(lines)
# print(elves)
# elves.append(0)
# # print("aa")
# # print(elves)
# for line in lines:
#     # print(line)
#     # if 
#     if line == '':
#         print('next')
#         ii = ii+1
#         elves.append(0)
#     else:
#         # print("zero")
#         elves[ii] = elves[ii] + int(line)
    
# #     if line is "\n"
# print("Elves")
# print(elves)
# # print(max(elves))
# # elves = elves.sort()
# elves.sort()
# breakpoint()
# print(elves)

