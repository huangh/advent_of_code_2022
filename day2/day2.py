
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