#imports
import os
import subprocess
import time
import json

#load modules:

#script wide vars
mainCondition = True
packageversion = "Beta - July-2021"

#OUTSIDE SOURCES:
#CREDIT TO POSTER IN: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
#I DO NOT TAKE CREDIT FOR THIS BELOW progressBar method
#CODE USED TO IMPROVE VISUAL APPEAL OF PROGRAM WHILE RUNNING 
#Print iterations progress
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()
#END OUTSIDE SOURCES

#_cls: Defines the terminal clear command to clear terminal while program runs when needed
#Returns: Nothing
def _cls():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")    

#_directoryPrint(): Defines a method to print the directory of the PC running the script for this tool
def _directoryPrint():
    print("<------------------[Current Directory]-------------------->")
    currentDir = _dirParser()
    currentDir = currentDir.split("/")
    if len(currentDir) == 2:
        print(currentDir[-1] + "[> / (root directory)" + " <--- You Are Here")
    elif len(currentDir) > 1:
        for x in currentDir[:-1]:
            if x == "":
                print("[> /")
            else:
                print("[> " + x + "/")
        print("[> " + currentDir[-1] + "/" + " <--- You Are Here")
    print("<-----------------[Directory Contents]-------------------->")
    dirContent = os.listdir()
    fileNumbs = 0
    for x in dirContent:
        print("[> " + x)
    print("<--------------------------------------------------------->")
    print()        

#_dirSwap(): Defines a nested method for input collection for changing directores
def _dirSwap():
    _directoryPrint()
    while True:
        try:
            directory = input("[!] Please Insert the Full Directory Here: ")
            os.system("cd")
            os.chdir(directory)
            break
        except:
            print("[ERROR] Invalid Directory")
            time.sleep(1)

#_interpreter: Defines the command interpreter to parse information depending on the command. Leverages a paramter (user) from userinput.
def _interpreter(user):
    #SingleAudio---------------------------------------------------------/
    if user == "1":
        _cls()
        _singleAudioMP3()
    #MultiAudio---------------------------------------------------------/
    if user == "2":
        _cls()
        _multiAudioMP3()
    #SingleVideo---------------------------------------------------------/
    elif user == "3":
        _cls()
        _singleVideo()
    #MultiVideo---------------------------------------------------------/  
    elif user == "4":
        _cls()
        _multiVideo()
    #List-Directory---------------------------------------------/
    elif user == "7":
        _directoryPrint()
        time.sleep(3)
    #Change-Directory---------------------------------------------/
    elif user == "8":
        _cls()
        _dirSwap()
    #Exit---------------------------------------------------------/
    elif user == "9":
        _exitApp()
    else:
        print("[ERROR] Command Not Recognized.")
        time.sleep(1)
        return

#_dirParser(): Defines a method to parse the pwd directory to be used by other methods
def _dirParser():
    currentDir = subprocess.check_output("pwd")
    currentDir = str(currentDir)
    currentDir = currentDir[2:(len(currentDir)-3)]
    return currentDir

#_exitApp(): Defines the method when the user enters exit in an input in the application shell to exit the program
def _exitApp():
    _cls()
    print("Exited Youtube-DL CLI Tool")
    exit()


#_userInput: Defines the user input command with a leveraged _interpreter for deciphering commands. 
def _userInput():
    _cls()
    print("<--------------------[Youtube-DL-Menu]-------------------->")
    print("|[Audio]                                                  |")
    print("|1. Single MP3 - Audio                                    |")
    print("|2. Multi MP3 - Audio                                     |")
    print("|                                                         |")
    print("|[Video]                                                  |")
    print("|3. Single - Video                                        |")
    print("|4. Multi - Video                                         |") 
    print("|                                                         |")
    print("|[Settings]                                               |")
    print("|7. Current Directory                                     |")
    print("|8. Change Directory                                      |")
    print("|9. Quit                                                  |")
    print("<--------------------------------------------------------->")
    print()
    user = input("[!] Select an option:  ") #grab input;
    print()
    _interpreter(user) #convert input to command;

##AUDIO##
#_singleAudioMP3(): Defines the method which requests an MP3 version of the Youtube Link to be downloaded
def _singleAudioMP3():
    _cls()
    print("<-----------------[Single MP3 Download]------------------->")
    _directoryPrint()
    print("<--------------------------------------------------------->")
    print("| [!] Default Output is Youtube-DL 'Best Quality'         |")
    print("| [!] Right Click On Video -> Copy Video URL -> Paste     |")
    print("| [!] [ENTER + No URL] Back To Main Menu.                 |")
    print("<--------------------------------------------------------->")
    print()
    url = input("[URL] Youtube Link: ")
    if "https://" in url:
        _procCommandAudio(url)
        print()
        another = input("[!] Would you like to do another? (Yes / No) ")
        if another == "Yes" or another == "yes":
            _singleAudioMP3()
        elif another == "No" or another == "no":
            return
    elif url == "":
        return
    else:
        print("[ERROR] Please Enter a Valid HTTPS URL to a YouTube Video")
        time.sleep(1)

#_multiAudioMP3(): Defines the method which requests a bulk batch MP3 version of a set of Youtube Links
def _multiAudioMP3():
    _cls()
    print("<------------------[Multi MP3 Download]------------------->")
    _directoryPrint()
    print("<--------------------------------------------------------->")
    print("| [!] Default Output is Youtube-DL 'Best Quality'         |")
    print("<--------------------------------------------------------->")
    print()
    urls = []
    urlNumbs = _urlNumbs()
    _batchProcessAudio(urlNumbs, urls)
    another = input("[!] Would you like to do another? (Yes / No) ")
    if another == "Yes" or another == "yes":
        _multiAudioMP3()
    elif another == "No" or another == "no":
        return

#_urlNumbs(): Defines a method to grab and return the number of URL numbers as an input function
def _urlNumbs():
    urlCount = 0
    while True:
        try:
            urlCount = int(input("[!] How many URLs would you like to process? "))
            break
        except ValueError:
            print("[ERROR] Please enter a valid number.")
    return urlCount    

#_batchProcessAudio(): Defines a method to batch process taking an input of the number of URLs to process through
def _batchProcessAudio(urlNumbs, urls):
    for i in range(urlNumbs):
        urlInput = input("[!] Enter a URL: ")
        if "https://" in urlInput:
            urls.append(urlInput)
        else:
            print("[ERROR] Invalid HTTPS URL - URL will NOT be processed")
            urls.append("")
    #Error Checking  Begin {
    _cls()
    print("[!] Processing...")
    blanks = 0
    for i in urls:
        if i == "":
            blanks = blanks + 1
    if blanks == urlNumbs:
        print("[ERROR] No URLS. Nothing Processed")
        time.sleep(2)
        return
    #Error Checking End }
    for item in progressBar(urls, prefix = 'Progress:', suffix = 'Complete', length = 50):
        if item == "":
            print("[!] Nothing Processing. Moving to Next...")
            time.sleep(0.1)
            print()
            _cls()
        else:
            _procCommandAudio(item)
            print()
            time.sleep(0.1)
            print()
            _cls()
    time.sleep(3)
    _cls()
    print("[!] Refreshing Directories...")
    print("[!] All requests processed. Check the directory output below")
    time.sleep(1)
    _directoryPrint()

#_procCommandVideo(): Defines a method to process the command for the particular method - Audio
def _procCommandAudio(url):
    print()
    header = "youtube-dl -x --audio-format mp3 "
    command = header + url
    os.system(command)

##VIDEO##
#_singleVideoMP4(): Defines the method which requests an MP4 Video version of the Youtube Link to be downloaded
def _singleVideo():
    _cls()
    print("<-----------------[Single Video Download]----------------->")
    _directoryPrint()
    print("<--------------------------------------------------------->")
    print("| [!] Default Output is Youtube-DL 'Best Quality'         |")
    print("| [!] Right Click On Video -> Copy Video URL -> Paste     |")
    print("| [!] [ENTER + No URL] Back To Main Menu.                 |")
    print("<--------------------------------------------------------->")
    print()
    url = input("[URL] Youtube Link: ")
    if "https://" in url:
        _procCommandVideo(url)
        print()
        another = input("[!] Would you like to do another? (Yes / No) ")
        if another == "Yes" or another == "yes":
            _singleVideo()
        elif another == "No" or another == "no":
            return
    elif url == "":
        return
    else:
        print("[ERROR] Please Enter a Valid HTTPS URL to a YouTube Video")
        time.sleep(1)
        _singleVideo()

#_procCommandVideo(): Defines a method to process the command for the particular method - Video
def _procCommandVideo(url):
    print()
    header = "youtube-dl -f best "
    command = header + url
    os.system(command)

#_batchProcessVideo(): Defines a method to batch process taking an input of the number of URLs to process through
def _batchProcessVideo(urlNumbs, urls):
    for i in range(urlNumbs):
        urlInput = input("[!] Enter a URL: ")
        if "https://" in urlInput:
            urls.append(urlInput)
        else:
            print("[ERROR] Invalid HTTPS URL - URL will NOT be processed")
            urls.append("")
    #Error Checking  Begin {
    _cls()
    print("[!] Processing...")
    blanks = 0
    for i in urls:
        if i == "":
            blanks = blanks + 1
    if blanks == urlNumbs:
        print("[ERROR] No URLS. Nothing Processed")
        time.sleep(2)
        return
    #Error Checking End }
    for item in progressBar(urls, prefix = 'Progress:', suffix = 'Complete', length = 50):
        if item == "":
            print("[!] Nothing Processing. Moving to Next...")
            time.sleep(0.1)
            print()
            _cls()
        else:
            _procCommandVideo(item)
            print()
            time.sleep(0.1)
            print()
            _cls()
    time.sleep(3)
    _cls()
    print("[!] Refreshing Directories...")
    print("[!] All requests processed. Check the directory output below")
    time.sleep(1)
    _directoryPrint()

#_multiVideoMP4(): Defines the method which requests a bulk batch MP4 version of a set of Youtube Links
def _multiVideo():
    _cls()
    print("<-----------------[Multi Video Download]------------------>")
    _directoryPrint()
    print("<--------------------------------------------------------->")
    print("| [!] Default Output is Youtube-DL 'Best Quality'         |")
    print("<--------------------------------------------------------->")
    print()
    urls = []
    urlNumbs = _urlNumbs()
    _batchProcessVideo(urlNumbs, urls)
    another = input("[!] Would you like to do another? (Yes / No) ")
    if another == "Yes" or another == "yes":
        _multiVideo()
    elif another == "No" or another == "no":
        return

#THREADS
#_runningThread: Defines the running thread to keep the program persistent until killed. 
def _runningThread(mainCondition):
    while mainCondition:
        _userInput()

#Running
_runningThread(mainCondition)