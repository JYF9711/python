import threading
import time
def thread():
    time.sleep(2)
    print('---子线程结束---')

def main():
    t1=threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
    print('---主线程---')
if __name__=='__main__':
    main()