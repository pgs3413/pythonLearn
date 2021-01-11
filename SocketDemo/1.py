import socket

for port in range(1,10000):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.01)
    state=s.connect_ex(("192.168.1.95",port))
    if state==0:
        print(f"port:{port} is open")
    s.close