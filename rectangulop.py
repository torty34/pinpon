def rectangulop(a,b):
    ksc=0
    for i in range (2):
        if (((b[i]>=a[i])and(b[i]<=a[i+2]))or((b[i+2]>=a[i])and(b[i+2]<=a[i+2]))) :
            ksc+=1
    if (ksc==2):
        return True
    else:
        return False

#bb=[1.5,1.5,3.5,3.5]
#aa=[2.5,2.5,4.5,4.5]
#rectangulop(aa,bb)