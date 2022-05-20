from dataclasses import replace
from math import comb
import os
import numpy as np
import pandas as pd 
from itertools import combinations
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.lines import Line2D

files =['01.txt','02.txt','03.txt','04.txt','05.txt','06.txt','07.txt','08.txt','09.txt','10.txt']
#print(files)

def textreader(ticker): 
    with open('./'+ticker,'r') as text:
        newtext=text.read().lower().replace('"',"").replace('\n',' ').replace('?','.').replace('*','').split('. ')
        for num in range(0,len(newtext)):
            newtext[num]=newtext[num].strip()
        return newtext

wordslist=set()
wordsdict={}
for element in files:
    text=textreader(element)
    for sentence in range(0,len(text)):
        words=text[sentence].replace("--"," ").replace(",","").replace(".","").replace("...","").replace(":","").replace("!","").replace("_","").strip().split(" ")
        for word in words:
            if word:
                word.replace(" ","")
                wordslist.add(word)


count=0
for element in wordslist:
    wordsdict[element]=count
    count = count + 1

#print(wordsdict)


#print(wordsdict['fond'])
#Create the numerical vector sequences
numericaltext={}
allsentences=[]
for element in files:
    text=textreader(element)
    #print(len(text))
    numericalsentencelist=[]
    for sentence in range(0,len(text)):
        words=text[sentence].replace("--"," ").replace(",","").replace(".","").replace("...","").replace(":","").replace("!","").replace("_","").strip().split(" ")
        #print(words)
        numericalsentence=[]
        allsentences.append(text[sentence])
        for word in words:
            #print(word)
            if word:
              word.replace(" ","")
              numericalsentence.append(wordsdict[word])
        numericalsentencelist.append(numericalsentence)
    numericaltext[element]=numericalsentencelist
#print(numericaltext['02.txt'])

""" for sen1 in combinations(allsentences,2):
    if sen1[0] == sen1[1]:
        print(sen1[0],len(sen1[0])) """
    


#Compare documents¨

#comparison={}
#print(numericaltext)
template={}
for obj in files:
    templist=[]
    for sentence in numericaltext[obj]:
        if sentence:
            templist.append([len(sentence),''])
    template[obj]=templist
""" for obj in template:
    print(obj)
    print(template[obj]) """

result = {}
#info = {}
#template= {}
for i in combinations(files,2):
    #print(i)
    list=[]
    #list2=[]
    countj=0
    for j in numericaltext[i[0]]:
        temp=''
        countn=0
        for n in numericaltext[i[1]]:
            if np.array_equiv(j, n) and len(j)>=3:
                list.append([j,[countj,countn]])
                #temp=i[1]
            countn=countn+1
        
        #list2.append([len(j),temp])
        countj=countj+1
    result[i]=list
    #info[i]=list2
    #template[i[0]]=list2

#print(result)
#info2 = {}
for obj in result:
    if result[obj]:
        for item in result[obj]:
            template[obj[0]][item[1][0]]=[template[obj[0]][item[1][0]][0],obj[1]]
            template[obj[1]][item[1][1]]=[template[obj[1]][item[1][1]][0],obj[0]]

""" for obj in template:
    print(obj)
    print(template[obj]) """



""" test=[]
for text in files:
    for obj in info:
        if obj[0] == text:
            index=0
            for f,b in zip(info[obj], template[obj[0]]):
                if f[1] != '':
                    template[obj[0]][index]=f
                index=index+1 """
""" for obj in template:
    print(obj)
    print(template[obj]) """



    #print(obj)
    #print(info[obj])
""" result = {}
info = {}
for i in files:
    for j in files:
        if i != j:
            list=[]
            list2=[]
            for sen1 in numericaltext[i]:
                temp=''
                for sen2 in numericaltext[j]:
                    if np.array_equiv(sen1, sen2):
                        list.append(sen1)
                        temp=j
                list2.append([len(sen1),temp])
    result[str(i+j)]=list
    info[i]=list2 """

#print(result)


""" for obj in result:
    print(obj)
    for list in result[obj]:
        sentence=[]
        for obj in list:
            sentence.append([*wordsdict][obj])
        print(sentence)  """


#Barplot
bars =[0,1,2,3,4,5,6,7,8,9,10]
colors = {'01.txt':'lime','02.txt':'red','03.txt':'yellow','07.txt':'aquamarine','06.txt':'gold','10.txt':'cyan',
            '04.txt':'deepskyblue','05.txt':'orange','08.txt':'magenta','09.txt':'peru'}
colors_legend= (Line2D([0],[0],marker='o',color='lime',lw=0),
                Line2D([0],[0],marker='o',color='red',lw=0),
                Line2D([0],[0],marker='o',color='yellow',lw=0),
                Line2D([0],[0],marker='o',color='deepskyblue',lw=0),
                Line2D([0],[0],marker='o',color='orange',lw=0),
                Line2D([0],[0],marker='o',color='gold',lw=0),
                Line2D([0],[0],marker='o',color='aquamarine',lw=0),
                Line2D([0],[0],marker='o',color='magenta',lw=0),
                Line2D([0],[0],marker='o',color='peru',lw=0),
                Line2D([0],[0],marker='o',color='cyan',lw=0))
x=1
for element in template:
    total=sum(item[0] for item in template[element])
    ypos=0
    #print(template[element])
    rotatelist=reversed(template[element])
    for item in rotatelist:
        col='lightgrey'
        if item[1] in colors.keys():
            col=colors[item[1]]
        plt.bar(x, height=((item[0]/total)*100), width = 0.2 , bottom=ypos , align='center',color=col)
        ypos=ypos+((item[0]/total)*100)+0.1
    x=x+1
    #for item in info[element]:
plt.legend(colors_legend,['01.txt','02.txt','03.txt','04.txt','05.txt','06.txt','07.txt',
            '08.txt','09.txt','10.txt'],bbox_to_anchor=(1.1,0.85))
plt.yticks([])
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.show()
#print(obj,result[obj])
#res = {'text1':[[3,0],[2,0],[4,1]];'text2':[4,1]}
#print(numericaltext['05.txt'])

#print(wordsdict)
#temp = [*wordsdict]
#print(temp[0])
    



