# simulation of the mathematical riddle of 100 prisoners and boxes with sheet
# Video recommendation | by Veritasium: https://www.youtube.com/watch?v=iSNsgj1OCLA

# imports
import random

# how many times the prisoners failed or succeeded
success = 0
fails = 0

GLOBAL_ITERATIONS = 1000
BOXES = 100
# recommended to be same number of prisoners as boxes
PRISONERS = BOXES

# for loop (how many iterations)
for i in range(0, GLOBAL_ITERATIONS):
    # list with all numbers of boxes
    boxList = range(1, BOXES + 1)

    # list with all numbers of sheets in the boxes (randomized box list, because the sheets have to be random)
    sheetList = random.sample(boxList, len(boxList))

    # list of the numbers of the prisoners
    prisonerList = range(1, PRISONERS + 1)

    # for loop for every prisoner number
    for prisonerNum in prisonerList:
        # at first the box is not found; the box that has to be searched is the prisoners number; it took the
        # prisoner 0 tries from now
        foundBox = False
        boxToSearch = prisonerNum
        tries = 0

        # as long as the prisoner didn't found their box
        while not foundBox:
            # they try
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

        # if they took more than half tries than there are boxes
        if tries >= BOXES/2:
            # print("Everyone died after " + str(tries) + " tries by prisoner number " + str(prisonerNum))
            fails = fails + 1
            break
        # else they succeeded
        else:
            # print("Survived after " + str(tries) + " tries by prisoner number " + str(prisonerNum))
            if prisonerNum == PRISONERS:
                success = success + 1

print("Successes: " + str(success))
print("Fails: " + str(fails))
