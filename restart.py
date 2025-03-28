import psutil, time, os

def stop():
    os._exit(1)

while (True):
    try:
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and not "main.py" in p.cmdline()[1]:
                print("Restart")
                os.chdir('/data/data/com.termux/files/home/assecc')
                os.system('python main.py')
            time.sleep(10)
    except:
        pass
