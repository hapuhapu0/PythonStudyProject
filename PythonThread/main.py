import threading
import time

def printText(text: str, sleepTime: int) -> None:
    for k in range(1, 10, 1):
        print(f"{text} {k}번째 반복")
        time.sleep(sleepTime)
        
ThreadList = [
    ("Thread1", printText, ("Thread1", 0.1)),
    ("Thread2", printText, ("Thread2", 0.2)),
    ("Thread3", printText, ("Thread3", 0.3)),
    ("Thread4", printText, ("Thread4", 0.4)),
    ("Thread5", printText, ("Thread5", 0.5))
]

threads = {}

for ThreadName, ThreadFunc, ThreadArgs in ThreadList:
    thread = threading.Thread(
        target = ThreadFunc,
        args = ThreadArgs
    )
    threads[ThreadName] = thread
    thread.start()


# Thread1 = threading.Thread(
#     target = printText,
#     args = ("직원1",
#             0.1
#     )
# )

# Thread2 = threading.Thread(
#     target = printText,
#     args = ("직원1",
#             0.2
#     )
# )

# Thread3 = threading.Thread(
#     target = printText,
#     args = ("직원1",
#             10
#     )
# )

# Thread1.start()
# Thread2.start()
# Thread3.start()