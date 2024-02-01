import threading
import time

def printF(text: str) -> None:
    for k in range(1, 30, 1):
        print(f"{text} {k}번째 반복중")
        time.sleep(0.5)

def daemonF() -> None:
    while True:
        print("데몬쓰레드 살아있음!")
        time.sleep(1)

Thread1 = threading.Thread(
    target = printF,
    args = ("직원1", )
)

DaemonThraed = threading.Thread(
    target = daemonF
)

DaemonThraed.daemon = True

DaemonThraed.start()
Thread1.start()
print(f"활성화 쓰레드 갯수: {threading.active_count()}")
print("메인은 놀기")
time.sleep(10)