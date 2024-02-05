import cv2
import mss
import numpy as np

def captureScreen(Pos: tuple) -> np.ndarray:
    with mss.mss() as sct:
        monitor = {"top": Pos[1], "left": Pos[0], "width": Pos[2] - Pos[0], "height": Pos[3] - Pos[1]}
        screenshot = sct.grab(monitor)
        screenshot = np.array(screenshot)
        return screenshot

def getHist(PosList: tuple) -> list:
    histList = list()
    Index = 1
    for Pos in PosList:
        Image = captureScreen(Pos)
        # Image = cv2.resize(Image, (300, 300))
        # Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        cv2.imshow(str(Index), Image)
        Index = Index + 1
        hist = cv2.calcHist([Image], [0], None, [256], [0, 256])
        histList.append(hist)
    cv2.waitKey(0)

    MainHist = histList.pop(0)
    ResultList = list()
    Index = 2

    for Image in histList:
        Result = cv2.compareHist(MainHist, Image, cv2.HISTCMP_CHISQR)
        # Result = cv2.compareHist(MainHist, Image, cv2.HISTCMP_CORREL)
        ResultList.append({
            Index: Result
        })
        Index = Index + 1
        
    for i in range(len(ResultList)):
        for j in range(i + 1, len(ResultList)):
            if list(ResultList[i].values())[0] > list(ResultList[j].values())[0]:
                ResultList[i], ResultList[j] = ResultList[j], ResultList[i]
    print(ResultList)

PosList = [
    (266, 176, 386, 339),
    (413, 176, 532, 338),
    (560, 176, 678, 338),
    (266, 367, 386, 530),
    (412, 368, 532, 530),
    (559, 369, 678, 530)
]

getHist(PosList)