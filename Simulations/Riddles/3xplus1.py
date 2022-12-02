GLOBAL_ITERATIONS = 100000
# IMPORTANT: Leave specific num 0 if you do NOT want a specific number being tested, just change the global
# iterations. You also do NOT have to change USE_SPECIFIC.
SPECIFIC_NUM = 0
USE_SPECIFIC = False
CHECK_FOR_NEGATIVE = True
# for larger iterations definitely recommended to be set to True  | reduces time more than half
IGNORE_PRINTS = True

# boolean if a loop was found
loopFound = False
foundNewLoop = False
newLoopNum = 0
operations = 0
totalOperations = 0
# if a specific number is selected
if SPECIFIC_NUM != 0:
    GLOBAL_ITERATIONS = 1
    USE_SPECIFIC = True
# iteration
print("CALCULATIONS STARTING...")
for i in range(1, GLOBAL_ITERATIONS + 1):
    int(i)
    # list of all used nums OR reset
    usedNums = []
    # if it is a specified number only  the specified num will be tested
    if USE_SPECIFIC:
        num = SPECIFIC_NUM
    else:
        num = i
    # as long as no loop is found
    if num <= 0 and CHECK_FOR_NEGATIVE:
        print("The number has to  be a positive integer.")
        break
    while not loopFound:

        if not IGNORE_PRINTS: print("Number is " + str(int(num)))
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
                if not IGNORE_PRINTS: print("Loop found with " + str(newLoopNum) + " at " + str(num))
                loopFound = True
                break

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
        operations = operations + 1
        # print(str(int(NUM)) + " is " + txt)

    # for the new iteration loopFound is set to False
    loopFound = False
    if not IGNORE_PRINTS: print("Took " + str(int(operations)) + " Operations")
    totalOperations = totalOperations + operations
    operations = 0

print("|-----------|SUMMARY|-----------|")
print("It took a total of " + str(int(totalOperations)) + " Operations")
if foundNewLoop:
    print("New loop has been found: " + str(newLoopNum))
else:
    print("No new loop has been found.")
