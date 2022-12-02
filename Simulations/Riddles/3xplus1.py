GLOBAL_ITERATIONS = 5000
# IMPORTANT: Leave specific num 0 if you do NOT want a specific number being tested, just change the global
# iterations. You also do NOT have to change USE_SPECIFIC.
SPECIFIC_NUM = 5
USE_SPECIFIC = False
OPERATIONS = 0
TOTAL_OPERATIONS = 0

# boolean if a loop was found
loopFound = False
foundNewLoop = False
newLoopNum = 0
# if a specific number is selected
if SPECIFIC_NUM != 0:
    GLOBAL_ITERATIONS = 1
    USE_SPECIFIC = True
# iteration
for i in range(1, GLOBAL_ITERATIONS + 1):
    # list of all used nums OR reset
    usedNums = []
    # if it is a specified number only  the specified num will be tested
    if USE_SPECIFIC:
        num = SPECIFIC_NUM
    else:
        num = i
    # as long as no loop is found
    while not loopFound:
        print("Number is " + str(int(num)))
        # the currently used number is appended to the list with all used numbers
        usedNums.append(num)
        # determine if the number is even or odd and do the calculations
        # txt = ""
        if num % 2 == 0:
            num = num / 2
            # txt = "even"
        else:
            num = num * 3 + 1
            # txt = "odd"
        OPERATIONS = OPERATIONS + 1
        # print(str(int(NUM)) + " is " + txt)

        # check if currently used number has already been used once, if it is True that means it is a loop
        for used in usedNums:
            if num == used:
                # if it is NOT the 4 2 1 loop the program found a new loop (which nobody has ever done)
                if used != 4 and used != 2 and used != 1:
                    foundNewLoop = True
                if USE_SPECIFIC:
                    newLoopNum = SPECIFIC_NUM
                else:
                    newLoopNum = i
                # so a loop has been found
                print("New loop found with " + str(newLoopNum) + " at " + str(num))
                loopFound = True
                break
    # for the new iteration loopFound is set to False
    loopFound = False
    print("Took " + str(int(OPERATIONS)) + " Operations")
    TOTAL_OPERATIONS = TOTAL_OPERATIONS + OPERATIONS
    OPERATIONS = 0

print("|-----------|SUMMARY|-----------|")
print("It took a total of " + str(int(TOTAL_OPERATIONS)) + " Operations")
if foundNewLoop:
    print("New loop has been found: " + str(newLoopNum))
else:
    print("No new loop has been found.")
