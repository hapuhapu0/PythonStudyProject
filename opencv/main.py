import cv2
import mss
import numpy as np
import os

class Image:
    def __init__(self) -> None:
        pass

    def captureScreen(self, Pos: tuple) -> np.ndarray:
        with mss.mss() as sct:
            monitor = {"top": Pos[1], "left": Pos[0], "width": Pos[2] - Pos[0], "height": Pos[3] - Pos[1]}
            screenshot = sct.grab(monitor)
            screenshot = np.array(screenshot)
            return screenshot
        
    def Search(self, Pos: tuple, threshold: float, Target, method: int = cv2.TM_CCOEFF_NORMED) -> list:
        # 캡쳐
        screen = self.captureScreen(Pos)

        # 서치
        Result = cv2.matchTemplate(screen, Target, method)

        # 임계값 정리
        locations = np.where(Result >= threshold)

        # 리턴리스트 초기화
        ReturnList = list()

        # 좌표 정리
        for Pos in zip(*locations[::-1]):
            x, y = Pos
            ReturnList.append({
                "x": x,
                "y": y
            })

        # 리턴
        return ReturnList
        
    def drawRectangles(self, DrawImage: np.ndarray, locations: np.ndarray, width: int, height: int) -> cv2:
        for loc in locations:
            x, y = loc
            x_end, y_end = x + width, y + height
            cv2.rectangle(DrawImage, (x, y), (x_end, y_end), (0, 255, 0), 2)

        return DrawImage

# 찾을 이미지 로드
Target = cv2.imread("opencv\\Image\\4.png")

# 초기화
Search = Image()

Result = Search.Search(
    (8, 357, 230, 590),
    0.8,
    Target
)

print(Result)