import psutil, time, os

while (True):
    try:
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and not "main.py" in p.cmdline()[1]:
                print("Restart")
                os.chdir('/data/data/com.termux/files/home/assecc')
                os.system('python main.py')
            if len(p.cmdline()) > 1 and not "unmain.py" in p.cmdline()[1]:
                os.chdir('/data/data/com.termux/files/home/assecc')
                os.system('python unmain.py')
        time.sleep(5)
    except:
        print('Краш1')
