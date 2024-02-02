import requests
import time
from bs4 import BeautifulSoup

# 파이썬 네이버 뉴스 크롤링


class winhttp:
    def __init__(self, url: str, headers: dict) -> None:
        self.wh = requests.get(
            url=url,
            headers=headers
        )


    def getWebData(self) -> str:
        if (self.wh.status_code == 200):
            return self.wh.text
        if (self.wh.status_code != 200):
            print(f"status_code error code: {self.wh.status_code}")

    def writeText(self, text: str, filepath: str = "Log.txt") -> None:
        with open(filepath, "a") as f:
            f.write(text)

    def bs4HtmlParse(self, whReasponText: str) -> BeautifulSoup:
        self.ParseData = BeautifulSoup(whReasponText, "html.parser")
        
        result = self.ParseData.find_all("a", {"class", "news_tit"})
        ResultArr = list()
        for div in result:
            ResultArr.append({
                "title" : div['title'],
                "link"  : div['href']
            })
        return ResultArr
    

def main() -> None:
    # 검색어 설정
    searchWord = "파이썬 최고"

    # 네이버 url, header 설정
    Url = f"https://search.naver.com/search.naver?ssc=tab.news.all&query={searchWord}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    # 시간측정변수
    time1 = time.time()

    # 요청 후 결과값 ResponseText변수에 저장
    wh = winhttp(
        url=Url,
        headers=headers
    )
    ResponseText = wh.getWebData()

    # 요청 결과값을 ParseText에 BeautifulSoup객체로 변환
    ParseText = wh.bs4HtmlParse(ResponseText)
    
    # 결과값 프린트
    for v in ParseText:
        print(f"뉴스이름: {v['title']}\n뉴스링크: {v['link']}\n\n")

    print(f"소요시간: {time.time() - time1}")

if (__name__ == "__main__"):
    main()