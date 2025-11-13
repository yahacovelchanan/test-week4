def caesar1(text:str):
    y=["a","b","c","d","e","f","g"]
    r=[]
    count=0
    for i in text:
        for j in y:
            if i==j:
                count+=len(i)+len(j)
                r.append(y[count])
    print(r)            
    return r
            
            

caesar1("bd")
              
      
        



        