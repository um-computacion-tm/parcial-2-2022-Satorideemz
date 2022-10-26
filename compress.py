from tkinter import Text
from xml.dom.expatbuilder import parseString


class Compress:
    def __init__(self,text=None) :
        self.text=text
    def compress(self,text):
        # token=None
        listadetexto=text.split()
        listadetexto2=text.split()
        listadetexto3=[]
        thisdict={}
        listadetexto2 = list(dict.fromkeys(listadetexto2))

        #print(listadetexto2)
        #print(listadetexto2[0])
        for i in range (len(listadetexto2)-5):
            if listadetexto2[i].find(".")!=-1 and i!=(len(listadetexto2)-5):
                #print(listadetexto2[i]+"\n"+listadetexto2[i+1])
                listadetexto2[i]=listadetexto2[i]+"\n"+listadetexto2[i+1]
                del listadetexto2[i+1]
                
        for i in range (len(listadetexto2)):
            #print(listadetexto2[i])
            thisdict[listadetexto2[i]] = i+1

        for i in range(len(listadetexto)):
            if text.find(thisdict(thisdict.values()).index(thisdict.get(listadetexto2[i])))!=-1:
               print(thisdict.get(listadetexto2[i]))
               listadetexto3.append(thisdict.get(listadetexto2[i]))

        return [],thisdict
 
    def uncompress(self):
        pass
    


    










        #    thisdict[listadetexto[i]] = i+1
        # print()
        
  

