import uiautomator2 as u2
import time

device_id = "R3CN904YLYW"

d = u2.connect(device_id)

# XPath 식
xpath_expression = '//*[@resource-id="com.kakao.talk:id/chat_log_recycler_list"]//*'

# 해당 UI 요소들 찾기
elements = d.xpath(xpath_expression).all()

# UI 요소가 존재하는지 확인
for element in elements:

    if element.info['contentDescription'] == "친구 추가":
        saveElement = element.info
        
    if element.info['contentDescription'] == "프로필 보기" and saveElement:
        print("찾음")
        d.click(element.bounds[0] + (element.bounds[2] - element.bounds[0]) / 2, element.bounds[1] + (element.bounds[3] - element.bounds[1]) / 2)
        saveElement = ""