import sys
import subprocess
import getopt

def dictionaryGen():
    wordlist=list(''.join(load['charlist']))
    #print(wordlist)
    maxi=int(load['maxLim'])
    mini=int(load['minLim'])
    print('#' * 10)
    for i in range(mini,maxi+1):
        temp=len(wordlist)**i
        #print(temp)
        #input()
        for c in range(0,temp):
            word=[]
            for k in range(0,i):
                index=int(c/(len(wordlist)**k)%(len(wordlist)))
                #print('c:%d,i:%d,k:%d' % (c,index,k))
                word.append(wordlist[index])
            password=("".join(word))
            query="hydra -l demo -p %s 192.168.2.62 http-post-form “/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login Failed"

            #subprocess.call(query,shell=True)

            if(password=="tEstin12"):
                print("\rpassword Found: %s " % (password))
                break
            else:
                print("\rtrying password: %s" % (password), end="")


load={}
def arguementInputter():
    Arglist=sys.argv[1:]
    s_opt="c:h:l:"
    l_opt=["charlist=","highest=","lowest="]
    try:
        args,opts=getopt.getopt(Arglist,s_opt,l_opt)

        for key,value in args:
            if(key in ('-c','--charlist')):
                load.update({'charlist':value})
            elif (key in ('-h', '--highest')):
                load.update({'maxLim':value})
            elif (key in ('-l', '--lowest')):
                load.update({'minLim':value})
        return load
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))


arguementInputter()
#PATH=subprocess.check_output("cd",shell=True)
dictionaryGen()