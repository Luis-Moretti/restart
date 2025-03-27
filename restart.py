import psutil, time, os

while (True):
    print('123')
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name().count('python') > 0:
            print(p.cmdline())
            if len(p.cmdline()) > 1 and not "main.py" in p.cmdline()[1]:
               print("Restarting")
               os.chdir('..')
               os.chdir('./assecc')
               os.system('python main.py')
    time.sleep(5)
