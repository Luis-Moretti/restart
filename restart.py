import psutil, time, os

while(True):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name().count('python') > 0:
            if len(p.cmdline()) > 1 and not "main.py" in p.cmdline()[1]:
               os._exit(1)
               os.chdir('..')
               os.chdir('./assecc')
               os.system('python main.py')
    time.sleep(5)
