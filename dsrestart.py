import psutil, time, os

while (True):
    try:
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and not "dsmain.py" in p.cmdline()[1]:
                print("Restart")
                os.chdir('/data/data/com.termux/files/home/DS-Bot-API')
                os.system('python dsmain.py')
        time.sleep(5)
    except:
        print('Краш1')
