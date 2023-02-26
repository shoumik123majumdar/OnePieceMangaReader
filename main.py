import webbrowser
import schedule

url = 'https://opscans.com/manga/72/vol-tbe-chapter-'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

global currentChapter
currentChapter= 1076

def addChapterNumber():
    global currentChapter
    currentChapter+=1


schedule.every().friday.do(addChapterNumber)

isInput = True
prompt = "Enter one piece chapter (1000 and up) or enter 'current' to go to said chapter:"
while(isInput):
    chapterNumber = input(prompt)
    if(chapterNumber == "current"):
        isInput = False
    elif (float(chapterNumber).is_integer() and int(chapterNumber) > 1000):
        isInput = False
    else:
        prompt = "This is not an acceptable input, please try again:"


if(chapterNumber == "current"):
    url += str(currentChapter)+"/"
elif int(chapterNumber) < currentChapter-3:
    url = 'https://opscans.com/manga/72/vol-tbe-ch-'+str(chapterNumber)+"/"
else:
    url += str(chapterNumber) + "/"

webbrowser.get(chrome_path).open(url)
