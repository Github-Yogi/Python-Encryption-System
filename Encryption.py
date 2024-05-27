#All the Definitions are found at the top of the code including the main Caesar function
#Please note: You may have to change the encoding of the .txt file the program opens in, lines: x,x,x,x,x

########################################
import string #Opens access to more string functions such as ascii_uppercase                  
import collections #Deque from Collections provides you ability to append and delete elements from either side of the queue
def Caesar(Text,Shift): 
    Upper=collections.deque(string.ascii_uppercase)
    Upper.rotate(Shift)
    Upper="".join(list(Upper))
    return Text.translate(str.maketrans(string.ascii_uppercase, Upper)) #Create a mapping table, translate() method allows you to replace any 2 characters around
########################################
def OnlyStrLeft():   
    OnlyStrLeft=str.maketrans('''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789''',38*"-") #Replaces all punctuation and number with hyphen
    return OnlyStrLeft
########################################
def WordsinTotal(Message):
    import re #RegEx or re offers a set of functions that allows you to search a string for a match
    TotalWords= len(re.findall("[A-Z_]+",Message)) #Counts the total amount of items/words with Upper Case letters
    return TotalWords
########################################
def WordCount(str): 
    Dictionary=dict()
    Words=str.split()  #Creates a dictionary with the Word as the key and Number of Occurences as value
    for Word in Words:
        if Word in Dictionary:
            Dictionary[Word]+=1
        else:
            Dictionary[Word]=1
    return Dictionary
########################################
def SortByValue(Dict): 
    global SortedByValueDict #Allows Variable to be called upon outside the function
    SortedByValueDict=sorted(Dict.items(),key=lambda t:t[1], reverse=True) #Sorts the dictionary in desceneding order of value(Number of occurences)
    print()
    for Key, Value in SortedByValueDict[:10]:  #Only the 10 most common word are shown to the user
        print(Key,":",Value)
########################################
def MostCommonLetter(Text): 
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MostFrequentLetter=(max(Alphabet, key=Text.upper().count)) # max() function here will return letter with the highest number of occurence
    return MostFrequentLetter
########################################
def Metrics(Message): 
    ################################################################################ #Metrics
    Message=Message.translate(OnlyStrLeft())
    Message=Message.replace("-","") #At this point the message has been stripped of punctuation/numbers (although for this to work the input must be a string)
    
    TotalWords=WordsinTotal(Message)
    ################################################## 
    SplitMessage=Message.split() #Message is turned into a list containing each word in the message an element
    UniqueWords=set(SplitMessage) #List is cast into a set    52   sets have no indetical elements
    UniqueWords2=[] #Need multiple sets to strip the entire message into one set of unique words (could it be more efficent)
    UniqueWords3=[]
    for item in UniqueWords:
        if item.isalpha()!=True: #isalpha() m returns True if all characters in the string are alphabets
            UniqueWords2.append(item.translate(OnlyStrLeft())) #Item is stripped of punctuation and numbers
        else:
            UniqueWords2.append(item)
        
    for item in UniqueWords2:
        if item.strip()!="":
            UniqueWords3.append(item.replace(" ",""))
    ##################################################
    UniqueList=list(SplitMessage)
    
    UniqueList=[] #Need multiple lists process to count the total occurences of each word (could be more efficent, can't be set as they only hold unique values)
    UniqueList2=[]      
    for item in SplitMessage:
        if item.isalpha()!=True:
            UniqueList.append(item.translate(OnlyStrLeft()))
        else:
            UniqueList.append(item)
    for item in UniqueList:
        if item.strip()!="":
            UniqueList2.append(item.strip())
    
    UniqueSentence=' '.join(UniqueList2)
    WordOccurences=WordCount(UniqueSentence)
    SortByValue(WordOccurences)
    ##################################################
    MaxLength=max(len(item) for item in UniqueList2)
    MinLength=min(len(item) for item in UniqueList2) #min() does the opposite of the max function
    ##################################################
    MostFrequentLetter=MostCommonLetter(UniqueSentence)

    ################################################################################
    
    return TotalWords, len(UniqueWords3), MaxLength, MinLength, MostFrequentLetter #Returns metrics based on input message (return is better than print as i can use it later and call upon it elesewhere)

######################################## 
def StoreInMetricsTxt(Words,Unique,Max,Min):
    MetricsFile=open("Metrics.txt","w",encoding="utf8") #Had to change encoding to prevent programming from crashing
    MetricsFile.write("Total number of words: "+str(Words)+
           "\nNumber of unique words: "+str(Unique)+
           "\nMaximum word length: "+str(Max)+
           "\nMinimum word length: "+str(Min))
    MetricsFile.close()
######################################## 
def ListToString(EverythingAsString): #Needed later to turn a list into string
    StringConverter=[]
    for item in EverythingAsString:
        for i in item:
            StringConverter.append(i)
    Disregard="\n"
    StringConverter = [i for i in StringConverter if i != Disregard] #List Comprehension discards all instance of "\n" with the list 
    StringConverter="".join(StringConverter)
    return StringConverter
######################################## #Here, a bar chart is generated using the data collected from the plaintext message and saved as aa pdf
def BarGraph(SortedByValueDict):
    import matplotlib.pyplot as plt #Allows user access to a MATLAB python library
    
    for Key, Value in SortedByValueDict[:10]:
        plt.bar(Key,Value) #Sets Words as Key and Occurences as Value
    plt.xlabel('Most common words')  #X-axis label
    plt.ylabel('Number of occurences') #Y-axis label
    plt.title('Most commom words againts occurences') #Title of Graph
    
    plt.savefig("Metrics Bar Chart.pdf") #Saves as pdf
########################################





while True:
    Mode=input("\nPress 1 for encrypt\nPress 2 for decrypt\n: ") #Using input(...) rather than int(input(...) prevents program from crashing if user enters wrong data type
###############################################################################     
    if Mode.upper()=="1": #Encryption Process Starts
        while True:  
            try:
                RotationChoice=int(input("\nPress 1 to enter rotation key\nPress 2 to recieve randomly generated rotation key (between -100 and 100)\n: "))
            
                if RotationChoice==1:
                    try:
                        Rotation=int(input("\nEnter the rotation value: "))         
                        break
                    except:
                        print("Invalid input try again!") #This method of asking the user to reenter a value when the condition is not met, is  used throughtout the code, only some are labeled



                elif RotationChoice==2:
                    import random
                    RandomRotation=random.randint(-26,26) #A random rotation between (-26,26) is generated
                    print("Your randomly genrated rotation key is: ",RandomRotation)
                    Rotation=RandomRotation
                    break
                
                else:
                    print("Invalid input try again!")
                
            except:
                print("Invalid input try again!")
                
        
        
        while True: #As True will always be True, an endless loop is created and the only way to leave is by breaking it       
            ManualOrFile=input("\nPress 1 to enter the message manually\nPress 2 to read message from a file\n: ") 
        #######################    
            if ManualOrFile.upper()=="1": #Manual message entry
                while True:  
                    Message=input("\nEnter the message you want encrypted: ")
                    if Message=="": #User cant leave the message blank
                        print("Invalid input try again!")
                    else:
                        break  
                    
        #######################    
            elif ManualOrFile.upper()=="2": #Message is read from file
                while True:
                    FileName=input("\nEnter the file name or file path excluding (.txt): ") #(eg: C:\Users\Name\Desktop...\notepad) or just file name if file is located in the same directory as program     
                    try:
                        EncryptFromFile=open(FileName+".txt","r",encoding="utf8")
                        Message=EncryptFromFile.read() #Everything inside the file is stored before closing it 
                        EncryptFromFile.close() #Should close file after
                        break
                    except:
                        print("File cannot be found try again")
        #######################       
           
            else:
                print("Invalid input try again!") 
                continue
            
            break    
        
        Message=Message.upper()  #Turns everything upper case
        print("\n-------------------------\nEncrypted message: "+Caesar(Message, -Rotation)) #Prints encrypted message
       
        ########################################## 
        AllMyMetrics=Metrics(Message)    
        print("\nTotal number of words:",AllMyMetrics[0])
        print("Number of unique words:",AllMyMetrics[1],"\n")
        print("\nMaximum word length:",AllMyMetrics[2])
        print("Minimum word length:",AllMyMetrics[3])
        print("\nMost common letter:", AllMyMetrics[4])
        print("-------------------------")
        
        StoreInMetricsTxt(AllMyMetrics[0],AllMyMetrics[1],AllMyMetrics[2],AllMyMetrics[3]) #Metrics are stored in a txt file
        BarGraph(SortedByValueDict)
        ##########################################
        
###############################################################################    
    elif Mode.upper()=="2": #Decryption process starts 
        while True:
            AutoDecryptChoice=input("\nPress 1 to Decrypt using rotation key\nPress 2 to Auto-Decrypt from a file\n:")
            
            
            if AutoDecryptChoice=="1":
                while True:  
                    try:
                        Rotation=int(input("\nPlease enter the rotation key: "))      
                        break
                    except:
                        print("Invalid input try again!")
                        
                while True:
                    Message=input("Please enter a the text you want decrypted: ") 
                    if Message=="":
                        print("Invalid input try again!")
                    else:
                        break
                
                Message=Message.upper() #Turns everything upper case      
                Message=Message.translate(OnlyStrLeft())
                Message=Message.replace("-","")
                Message=Caesar(Message,Rotation)
                print("\n-------------------------\nDecrypted message: "+Message) #Prints decrypted message
                
                AllMyMetrics=Metrics(Message)    
                print("\nTotal number of words:",AllMyMetrics[0])
                print("Number of unique words:",AllMyMetrics[1],"\n")  
                print("\nMaximum word length:",AllMyMetrics[2]) 
                print("Minimum word length:",AllMyMetrics[3])
                print("\nMost common letter:", AllMyMetrics[4])
                print("-------------------------")
                StoreInMetricsTxt(AllMyMetrics[0],AllMyMetrics[1],AllMyMetrics[2],AllMyMetrics[3])
                break
################################################         
            elif AutoDecryptChoice=="2":
                
                CommomWordsFile=open("words.txt","r",encoding="utf8") 
                FileContents=CommomWordsFile.read() #Contents of the words.txt file is stored to be compared to
                FileContents=FileContents.split()
                
                while True:
                    FileName=input("\nEnter the file name or file path excluding (.txt): ") #Auto-Decrypt process starts
                    
                    print()
                    try:
                        DecryptFile=open(FileName+".txt","r",encoding="utf8") 
                        FirstSentenceRaw=DecryptFile.readline() #Only the first line of the file is stored at this point
                        for item in range(1,26):  #Only needs to be rotated a max of 25 times since there are only 25 other letters in the alphabet disregrading itself
                            FirstSentence=FirstSentenceRaw.upper() #Has to be uppercase for OnlyStrLeft function to work
                            FirstSentence=FirstSentence.translate(OnlyStrLeft())
                            FirstSentence=FirstSentence.replace("-","")
                            FirstSentence=(Caesar(FirstSentence,-item))
                            FirstSentence=FirstSentence.lower() #Has to be lowercase so it can be compared directly to the words in words.txt file
                            FirstSentenceSplit=FirstSentence.split()
                            
                            WordMatches=0
                            for element in FirstSentenceSplit: 
                                if element in FileContents:
                                    WordMatches+=1 #Counts number words that match in the first line and the words.txt file
                        
                            if WordMatches>=1: #if one or more words match then rest of the lies are decrypted with the same rotation value                       
                                print("\nNumber of word matches: ",WordMatches)
                                print("\nPossible decrypted first line of message: "+FirstSentence.upper())      
                                
                                DecryptFile.close() #Had to close and reopen file due to printing errors
                                DecryptFile=open(FileName+".txt","r",encoding="utf8")
                                
                                AllSentences=DecryptFile.readlines() 
                                EverythingInFile=AllSentences
                                EverythingInList=[]
                                EverythingAsString=[]
                                for Items in EverythingInFile: 
                                   Items=Items.translate(OnlyStrLeft())
                                   Items=Items.replace("-","")
                                   Items=(Caesar(Items,-item))
                                   EverythingInList.append(Items)      
                                EverythingAsString=EverythingInList
                                
                                
                                IsItCorrect=input("\nHas the message been correctly decrypted\nPress 1 for yes (rest of the file is decrypted) \nPress 2 for no (another rotation will be attempted)\n: ") #what happens in each scenario
                                print()
                                
                                if IsItCorrect=="1":
                                    EverythingAsString=(ListToString(EverythingAsString))
                                    print(EverythingAsString+"\n-------------------------")
                                    
                                    AllMyMetrics=Metrics(EverythingAsString)    
                                    print("\nTotal number of words:",AllMyMetrics[0]) 
                                    print("Number of unique words:",AllMyMetrics[1],"\n")
                                    print("\nMaximum word length:",AllMyMetrics[2]) 
                                    print("Minimum word length:",AllMyMetrics[3])
                                    print("\nMost common letter:", AllMyMetrics[4])
                                    print("-------------------------")
                                    StoreInMetricsTxt(AllMyMetrics[0],AllMyMetrics[1],AllMyMetrics[2],AllMyMetrics[3]) #Metrics of plain english decrypted message is overwritten into the Metrics file 
                                    break
                                
                                elif IsItCorrect=="2": 
                                    continue #Prevents programing form doing unwanted loops
                                
                                else:
                                    print("\nInvalid input try again!")                      

                    except:
                        print("File cannot be found")
                    
                    
                    if IsItCorrect=="1":
                        print("\nDecryption Successfull, Metrices Stored !")
                        break
                    else:
                        print("\nDecryption Unsuccessfull, Metrices Not Stored !")
                        break
            
            
                DecryptFile.close()
                CommomWordsFile.close()
                break
################################################     
            else:
                print("Invalid input try again!\n")
    else:
        print("Invalid input try again!")
###############################################################################
