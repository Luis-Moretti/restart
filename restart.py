import psutil, time, os

while (True):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        print(p.cmdline()[1])
        if len(p.cmdline()) > 1 and not "main.py" in p.cmdline()[1]:
            print("Restarting")
            os.chdir('..')
            os.system('ls')
            os.chdir('./assecc')
            os.system('python main.py')
    time.sleep(5)
