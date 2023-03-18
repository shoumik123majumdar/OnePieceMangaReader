import webbrowser
import schedule
import pandas as pd

url = 'https://opscans.com/manga/77/vol-tbe-chapter-'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

database = pd.read_csv('ReleaseDates.csv', index_col=None)

global currentChapterIndex
with open('index.txt', 'r') as f:
    currentChapterIndex = int(f.readlines()[-1])



def addIndex():
    global currentChapterIndex
    currentChapterIndex += 1
    with open('index.txt', 'a') as f:
        f.write(str(currentChapterIndex)+"\n")


schedule.every().friday.do(addIndex)

global comparableChapter
global currentChapter
currentChapter = database._get_value(currentChapterIndex, 'Chapters')
comparableChapter = currentChapter
if currentChapter == "WSJ Break" or currentChapter == "Oda Break":
    comparableChapter = database._get_value(currentChapterIndex - 1, 'Chapters')


isInput = True
prompt = "Enter one piece chapter (1000 and up) or enter 'current' to go to said chapter:"
while (isInput):
    chapterNumber = input(prompt)
    if (chapterNumber == "schedule"):
        print(database)
    elif(chapterNumber == "iterate"):
        addIndex()
        currentChapter = database._get_value(currentChapterIndex, 'Chapters')
    elif (chapterNumber == "current"):
        isInput = False
    elif (chapterNumber.isnumeric()):
        if (float(chapterNumber).is_integer() and int(chapterNumber) > 1000 and int(chapterNumber)<=int(comparableChapter)):
            isInput = False
        else:
            prompt = "Website doesn't support the chapter you selected, enter again:"
    else:
        if (chapterNumber == "schedule" or chapterNumber == "iterate"):
            prompt = "Enter one piece chapter (1000 and up) or enter 'current' to go to said chapter:"
        else:
            prompt = "This is not an acceptable input, please try again:"


if (chapterNumber == "current"):
    if currentChapter == "WSJ Break" or currentChapter == "Oda Break":
        print("Sorry, One Piece is on break this week, try again next week")
        print("Update is set to run next on " + str(schedule.next_run()))
        exit(code=0)
    url += str(currentChapter) + "/"
elif int(chapterNumber) < int(comparableChapter) - 3:
    url = 'https://opscans.com/manga/77/vol-tbe-ch-' + str(chapterNumber) + "/"
else:
    url += str(chapterNumber) + "/"

webbrowser.get(chrome_path).open(url)
print("Update is set to run next on " + str(schedule.next_run()))
