import cv2
import numpy as np
from copy import deepcopy

colorDict={   #BGR
    "white":(255,255,255),
    "black":(0,0,0),
    "gray":(128,128,128),
    "red":(0,0,255),
    "blue":(255,0,0),
    "green":(0,255,0),
    "yellow":(0,255,255),
    "purple":(173,13,106),
    "brown":(0,75,150),
    "orange":(39,127,255)
}

def changeColor(frame,color):
    for i in range(len(frame)):
        renk=colorDict.get(color)
        frame[i]=renk
    print(renk)
    return frame

deneme=np.zeros(shape=[400,400,3],dtype=np.uint8)

white=deepcopy(changeColor(deneme,"white"))
black=deepcopy(changeColor(deneme,"black"))
gray=deepcopy(changeColor(deneme,"gray"))
red=deepcopy(changeColor(deneme,"red"))
blue=deepcopy(changeColor(deneme,"blue"))
green=deepcopy(changeColor(deneme,"green"))
yellow=deepcopy(changeColor(deneme,"yellow"))
purple=deepcopy(changeColor(deneme,"purple"))
brown=deepcopy(changeColor(deneme,"brown"))
orange=deepcopy(changeColor(deneme,"orange"))

backgroundDict={"white":white,
                "black":black,
                "gray":gray,
                "red":red,
                "blue":blue,
                "green":green,
                "yellow":yellow,
                "purple":purple,
                "brown":brown,
                "orange":orange }

materialList=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
#colorDict={white,black,gray,red,blue,green,yellow,purple,brown,orange}

for i in backgroundDict:
    for j in colorDict:
        for k in materialList:
            if i==j:
                continue
            color=colorDict.get(j)
            name="C:\\Users\\Hazim\\Desktop\\Materials_new\\"+str(i)+"-"+str(j)+"-"+str(k)+".png"
            # frame=cv2.putText()
            if k == "I":
                frame=deepcopy(cv2.putText(deepcopy(backgroundDict.get(str(i))),k,(150,300),2,11,color,11,cv2.FONT_HERSHEY_SIMPLEX))
            else:
                frame=deepcopy(cv2.putText(deepcopy(backgroundDict.get(str(i))),k,(92,300),2,11,color,11,cv2.FONT_HERSHEY_SIMPLEX))
            cv2.imwrite(name,frame)




if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()