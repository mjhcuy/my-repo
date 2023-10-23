import os

fp ="temp.txt"
# fp = "temp1.txt"

file = open(fp,"w")

if os.path.exists(fp):
    print("ok")
else : 
    print("error")


# exception file read

import os

fp ="temp.txt"

if os.path.exists(fp) :
    f = open(fp,"r")
    for line in f :
        print(line)
else :
    f =open (fp,"w")
    for i in range(100) :
        f.write(str(i)+"\n")
    #print("error")

f.close()

#
import os

fp ="new.txt"

f =open(fp,"w")
f.close()

os.remove(fp)
print("complete")


# dir 
""""""
import os

fp ="new.txt"

f = open(fp,"w")
f.close()

os.remove(fp)
print("complete")



import os
def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)


        fp ="new.txt"

        fp="new.txt"

        f = open(fp,"w")
        f.close()

        dir_print("./")
        print("======================\n\n")
        dir_print("./")
        

        #

        import os

        fp = "new.txt"

        f = open(fp,"w")
        f.close()

        os.rename(fp,"new1.txt")
        print("complete")


        #
        import os
        def dir_print(p):
            for f in files :
                print(f)

    fp = "new.txt"
    tp = "new1.txt"

    f=open(fp,'w')
    f.close()
    dir_print("./")
    print("\n===================")


    if os.path.exists(tp):
        os.remove(tp)
        dir_print("./")



    #