mevalar=['olma','anor','anjir','shaftoli','tarvuz','qovun','banan']
mevalar_b=list(filter(lambda meva: meva.startswith('b'),mevalar))
print(mevalar_b)
mevalar2=list(filter(lambda meva :len(meva)<=5,mevalar))
print(mevalar2)
