# 입력 암호화

import getpass

# pw = getpass.getpass("pass : ")
pw = input("pass :")
print(pw)

 # 해시함수
 
import hashlib

hl = hashlib.sha256()
# target = "hello"
# target = "hi"
# target = "world"
# target ="python"
# target ="media"
# target = "media program"
# target = "1234567890"

target = "to be or not to be, that is a question!"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())


#keccak256
""""""
import crypto.hash as kek
# target = "hello"
# target = "hi"
# target = "world"
# target ="python"
# target ="media"
# target = "media program"
# target = "1234567890"
target = "to be or not to be, that is a question!"

kksh = kek.new(digest_bits = 256)
kksh.update(target.encode("utf-8"))


print(kksh.digset())
print(kksh.hexdigest())


#
import getpass
import hashlib

pw = getpass.getpass("pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())

#
import hashlib
import os

def pwInsert():
   if os.path.exists('pw.txt'):
      pw = input('insert pass:')
      hs = hashlib.sha256()
      hs.update(pw.encode("utf-8"))
      with open('pw.txt','r') as fp:
          return hs.hexdigest() == fp.read()
   else:
       return True
   
if pwInsert():
    pw = input('new pass :')
    with open('pw.txt','w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password")



# 시스템정보 확인

import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)     

ps = pf.system()
paint(ps)


#


import urllib.request as ur

ur1 = 'https://www.google.com'
# ur1 = "https://daum.net"
# ur1 = "https://xkcd.com"

# res = urllib.request.urlopen(ur1)
res = urllib.request.urlopen(ur1)


web = res.read()

with open("u1.html","wb") as fp:
    fp.write(web)
    
# print(web.decode('utf-8'))
print(web)



#웹페이지 읽기2
"""
import http.client as hc

# ur1 = 'https://www.google.com'
# ur1 = "www.daum.net"
ur1 = "v.daum.net"
# conn = http.client.HTTPSConnection(ur1)
conn = hc.HTTPSConnection(ur1)
# conn.request("GET","/")
conn.request("GET","/v/20231103063908539")

r= conn.getresponse()

with open("ulcl.html", "wb") as fp :
    fp.write(r.read())
    
    conn.close()
    
    print(r)
    
    
    #
    
    import requests
    
    ur1 = "https://www.google.com"
    res = requests.get(ur1)
    web = res.content
    
    print(web)
     """  
     
"""import threading
import time
    
    #
    
def counter(str_name):
        for i in range(50000):
            print(f"Countdown{i},name : {str_name}\n")
            
start = time.time()
for i in range(3) :
     counter(f"num{i}")
     
end = time.time()

#print("single end")
print("single enf",end - start)


#
#
#
    
thread1 = threading.Thread(target=counter, args=("1num",))
thread2 = threading.Thread(target=counter, args=("2num", ))
thread3 = threading.Thread(target=counter, args=("3num", ))

staet = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time

print("muitl end",end - start)"""
#
import multiprocessing
import time
def counter(str_name):
    for i in range(50000):
        print(f"Countdown{i},name : {str_name}\n")
        
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))

start = time.time()

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()