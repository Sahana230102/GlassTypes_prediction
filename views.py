from django.shortcuts import render
import pandas as pd
import sklearn 
from sklearn.neighbors import KNeighborsClassifier
# Create your views here.
def PROJECT1(request):
    path= "C:\\Users\\infin\\OneDrive\\Desktop\\WEB\\WEB\\glass.csv"
    data=pd.read_csv(path)
    
   
    inputs=data.drop('Type','columns')
    output=data.drop(['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe'],'columns')
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
    
    model=KNeighborsClassifier(n_neighbors=15)
    model.fit(x_train,y_train) 
    y_pred=model.predict(x_test)
    from sklearn.metrics import confusion_matrix
    cm=confusion_matrix (y_test, y_pred)
    print (cm)


    if(request.method=="POST"):
        data=request.POST
        RI=data.get('TXTRI')
        Na=data.get('TXTNa')
        Mg=data.get('TXTMg')
        Al=data.get('TXTAl')
        Si=data.get('TXTSi')
        K=data.get('TXTK')
        Ca=data.get('TXTCa')
        Ba=data.get('TXTBa')
        Fe=data.get('TXTFe')
        if('SUBMIT' in request.POST):
            res=model.predict([[RI,Na,Mg,Al,Si,K,Ca,Ba,Fe]])
            if (res==1):
                op=("Type 1")
            elif res==2:
                op=("Type 2")
            elif res==3:
                op=("Type 3")
            elif res==4:
                op=("Type 4")
            elif res==5:
                op=("Type 5")
            elif res==6:
                op=("Type 6")
            elif res==7:
                op=("Type 7")
            else:
                op=("Invalid Data")

            return render(request,'PROJECT1.html',context={'op':op})  
    return render(request,'PROJECT1.html')