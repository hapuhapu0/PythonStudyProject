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

    Screenshot = captureScreen((0, 0, 1920, 1080))
    for Pos in PosList:
        Image = Screenshot[Pos[1]: Pos[1] + Pos[3] - Pos[1], Pos[0]: Pos[0] + Pos[2] - Pos[0]]
        Image = cv2.resize(Image, (300, 300))
        Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow(str(Index), Image)

        hist = cv2.calcHist([Image], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist)
        histList.append(hist)

        Index = Index + 1
    # cv2.waitKey(0)

    MainHist = histList.pop(0)
    ResultList = list()
    Index = 2

    for Image in histList:
        Result = cv2.compareHist(MainHist, Image, cv2.HISTCMP_CORREL)
        ResultList.append({
            Index: Result
        })
        Index = Index + 1
        
    for i in range(len(ResultList)):
        for j in range(i + 1, len(ResultList)):
            if list(ResultList[i].values())[0] > list(ResultList[j].values())[0]:
                ResultList[i], ResultList[j] = ResultList[j], ResultList[i]

    keys_to_print = [list(v.keys())[0] for v in ResultList[:2]]
    print(":".join(map(str, keys_to_print)))

PosList = [
    (275, 186, 377, 331),
    (420, 189, 527, 331),
    (566, 189, 671, 333),
    (272, 379, 380, 524),
    (420, 379, 525, 521),
    (568, 379, 673, 516)
]

getHist(PosList)