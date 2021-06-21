import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b':
        k2 = inkey()
        k3 = inkey()
        if k3=='A':
            print ("up 80")
            s.write("/goStraight/run 80 \n".encode())
        if k3=='B':
            print ("down")
            s.write("/goStraight/run -80 \n".encode())
        if k3=='C':
            print ("right")
            #s.write("/turn/run 100 -0.3 \n".encode())
            s.write("/R/run 90 -60 \n".encode())
        if k3=='D':
            print ("left")
            s.write("/turn/run 100 0.3 \n".encode())
            #s.write("/L/run 40 -100\n".encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
    elif k=='q':
        print ("quit")
        return 0
    else:
        print ("not an arrow key!")
    return 1

if len(sys.argv) < 1:
    print ("No port input")
s = serial.Serial(sys.argv[1])
while True:
    a = s.readline()
    print("s.read: ", a.decode())

while get():
    i = 0
