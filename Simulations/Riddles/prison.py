# simulation of the mathematical riddle of 100 prisoners and 100 boxes with sheets inside
# Video recommendation | by Veritasium: https://www.youtube.com/watch?v=iSNsgj1OCLA

# imports
import random

# how many times the prisoners failed or succeeded
success = 0
fails = 0

GLOBAL_ITERATIONS = 1000
BOXES = 100
# there should be the same number of prisoners as there are boxes
PRISONERS = BOXES

for i in range(0, GLOBAL_ITERATIONS):
    # list with all numbers of boxes
    boxList = range(1, BOXES + 1)

    # list with all numbers of sheets in the boxes (randomized box list, because the sheets have to be random)
    sheetList = random.sample(boxList, len(boxList))

    # list of the numbers of the prisoners
    prisonerList = range(1, PRISONERS + 1)

    # for loop for every prisoner's number
    for prisonerNum in prisonerList:
        foundBox = False
        boxToSearch = prisonerNum
        tries = 0
        
        while not foundBox:
            tries = tries + 1
            # the value of the box is the index of the box to search - 1 in the sheetList (which is randomized)
            boxValue = sheetList[boxToSearch - 1]
            # if they found their correct number the loop will end
            if boxValue == prisonerNum:
                foundBox = True
                break
            # else they have to search the box with the number of the sheet that was in the previous box
            else:
                boxToSearch = boxValue

        # if they need more tries than there are boxes/2
        if tries >= BOXES/2:
            # print("Everyone died after " + str(tries) + " tries by prisoner number " + str(prisonerNum) ".")
            fails = fails + 1
            break
        # else they succeeded
        else:
            # print("Prisoner number " + str(prisonerNum) + " survived after " + str(tries) + "tries.)
            if prisonerNum == PRISONERS:
                success = success + 1

print("Successes: " + str(success))
print("Fails: " + str(fails))
