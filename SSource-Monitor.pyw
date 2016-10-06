import urllib
import time

sourceCode=[]
i=0
tCapture=0
#-----------Change these--------------#
logName="log.txt"
delay=250 #in seconds
precision=10000 #10000 is recommended; increasing it you have higher precision rate but consumes more memory, while lower percision value gives lower percision rate with the benefit of consuming less memory
web_page='url'
#-------------------------------------#
log=open(logName,"a") #Opening logName
try:
    while (1):
        t=time.time() #Current time
        if (t >= tCapture+delay or len(sourceCode)==0): #Start capturing <delay> after last capture
            x=urllib.urlopen(web_page)
            sourceCode.append(x.read())
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









