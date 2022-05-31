from tempfile import tempdir
import pandas as pd
data = pd.read_csv("C:/Users/ronit/OneDrive/Desktop/Example_Technical_Skills.csv")

raw= pd.read_csv("C:/Users/ronit/OneDrive/Desktop/Raw_Skills_Dataset.csv")
skills=[]

temp=[]

data1=raw['RAW DATA']
data1=data1.astype(str)
## print(data1)
sk= input("Enter the Technical skill key words mentio9ned below \t \n (SQL, PYTHON, CLOUD, SAP, ANALYTICS, SCHEDULING, TRACKING, SOLIDITY, MONITORING): \t") 
## as in the assignment it was mentioned technical "hard skills" so i mentioned only SQL, PYTHON, CLOUD, SAP, ANALYTICS, SCHEDULING, TRACKING, SOLIDITY, MONITORING

sk= sk.upper()
## print(sk)
for x in data1:
    
    temp=x.split()
    for y in temp:
        if y.upper()== sk:
            skills.append(x)
    temp=[]
#print(skills)
print(len(skills))
skill={"SQL":skills,}
skill=pd.DataFrame(skills)
skill.to_csv("ML.csv")