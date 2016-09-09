import urllib
import time

sourceCode=[]
i=0
tCapture=0
#-----------Change these--------------#
logName="log.txt"
delay=0 #in seconds
precision=10000
web_page='http://vaios.xyz/index'
#-------------------------------------#
log=open(logName,"a") #Opening logName
try:
    while (1):
        t=time.time() #Current time
        if (t >= tCapture+delay): #Start capturing <delay> after last capture
            x=urllib.urlopen()
            sourceCode.append(x.read(web_page))
            if(len(sourceCode[i])!=len(sourceCode[i-1])):
                tCapture = time.time() #Time of capture
                log.write(sourceCode[i]+"\n----------CODE ENDS HERE----------\n"+time.asctime(time.localtime(tCapture))+"\n") #Write to log.txt
                sourceCode=[] #Resetting values
                i=-1
                log.close() #Saving file
                log=open(logName,"a")
            i+=1
            if(i>precision): #After <precision> queries reset
                sourceCode=[]
                i=0
                log.close()
                log=open(logName,"a")
except: 
    log.close()









