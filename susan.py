####################################
#                                  # 
#                                  #
#      Susan Version 2 ALPHA       #
#         By Logan Miller          #
#                                  #
#   http://www.loganberry.pe.hu    #
#                                  #
#                                  #
####################################

#wake susan + debug option
print("\nSUSAN BETA TETSING\nSusan is sleeping, press enter to wake her")
wake = input()
if wake == "debug": #enable debug mode if user types in debug
    print("\nDebug mode activated")

#importing os module
try:
    import os
    if wake == "debug": #if debug mode is enabled print debug text
        print("\n[DEBUG] Successfully imported os")
except ImportError: #if os is cannot be imported
    print("\n[DEBUG] Failed to import os")
    wait = input("\nPress enter to exit")

#opening and defining topic files
topicArray = []
if wake == "debug":
    print("\n[DEBUG] Opening topic files..")
for repeats in range(50): #repeating 50 times
    filePath = "topicInputs\-"[:-1] + str(repeats) + ".txt" #defining file name as xFile.txt in topic folder ([:-1] used because \ cannot be at end of string)
    try:
        file = open(filePath, "r") #opening file that was defined above
        if wake == "debug":
            print("[DEBUG] Successfully opened", filePath)
        topicArray.append(file.readlines()) #appends files lines to list
        if wake == "debug":
            print("[DEBUG] Successfully defined", filePath)
    except FileNotFoundError: #if files not found
        if wake == "debug":
            print("[DEBUG] Failed to open", filePath)

#primary loop
outputHappened = False
if wake == "debug":
    print("\n[DEBUG] Launching primary loop...")
while True:
    userInput = input("\n>: ") #user input
    x = userInput.lower() #putting user input to lower case

    for repeats in range(50): #repeat this 50 times (amount of topics)
        if wake == "debug":
            print("[DEBUG] Testing", topicArray[repeats])
        for values in topicArray[repeats]: #for every keyword in topicArray[current topic being tested]
            if wake == "debug":
                print("[DEBUG] Testing", values[:-1])
            if values[:-1] in x: #if the keyword has been found minus the \n line break
                try:
                    outputPath = os.getcwd(), "\\topicOutputs\-"[:-1] + str(repeats) + ".mp3" #define the path as a list of current directory and file name corresponding to topic activated
                    os.system("start " + outputPath[0] + outputPath[1]) #print both parts of list (list used due to bug)
                    if repeats == 22: #if the goodbye topic is activated end Susan
                        exit()
                    outputHappened = True #announcing that something has been outputted
                    if wake == "debug":
                        print("[DEBUG] Successfully found key word on repeat", repeats)
                except FileNotFoundError: #if the audio file corresponding to keyword was not found
                    if wake == "debug":
                        print("[DEBUG] Failed to open", str(repeats) + ".mp3")
    if outputHappened != True: #if no outputs have happened try to play noTopic.mp3
        try:
            outputPath = os.getcwd(), "\\topicOutputs\\noTopic.mp3"
            os.system("start " + outputPath[0] + outputPath[1])
            if wake == "degbug":
                print("[DEBUG] Failed to find key word on repeat", repeats)
        except FileNotFoundError: #if noTopic.mp3 was not found
            if wake == "debug":
                print("[DEBUG] Failed to open", str(repeats) + ".mp3")
        outputHappened = False #resseting variable for next user input
