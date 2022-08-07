import json
import requests
with open("task2.json","r+") as file:
    data=json.load(file)
def decate(movies):
    dic={}
    list=[]
    for m in movies:
        # print(m)
        a=int(m)
        mod=a%10
        dec=a-mod
        print(dec)
        if dec not in list:
            list.append(dec)
            print(list)
            
    list.sort()
    print(list)
    for j in list:
        dic[j]=[]
    for j in dic:
        print(j)
        dic1=j+9
        for k in movies:
            if int(k)<=dic1 and int(k)>=j:
                for l in movies[k]:
                    dic[j].append(l)
                with open("task3.json","w+") as file:
                    json.dump(dic,file,indent=4)
                    b=json.dumps(dic)
    return dic
print(decate(data))
            
                    
                    
                    
                    
                
            
            
        
        
        
        
        
        
    
        
        
        

        
        
    

