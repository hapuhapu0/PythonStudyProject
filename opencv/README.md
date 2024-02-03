# 2024-02-03

만든것
-----------------
opencv 템플릿매칭 편하게 해주는 함수  



소감
-----------------
생각보다 opencv 예외처리가 중요하다는것을 알게되었다.  
numpy와도 관계가 많다.  



노트
----------------

cv2.error: OpenCV(4.9.0) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\templmatch.cpp:1164: error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() && _img.dims() <= 2 in function 'cv::matchTemplate'
이건 무슨에러지...  
클래스로 만드니까 신기한 에러가 뜬다..  
opencv, numpy 공부 후 다시시도..!  