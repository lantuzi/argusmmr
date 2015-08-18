import numpy as np
from matplotlib import pylab
import Image

leng=50
foldername=['1301', '1304']
imagepath='../wetransfer-6d2a1a/'

for i in foldername:
    # list=np.loadtxt('namelist_'+i+'.txt')
    # fig=pylab.figure(figsize=(10,8),dpi=100)
    # for j in xrange(leng):
    #     name=imagepath+i+'/'+str(int(list[j])).zfill(4)+'.jpg'
    #     jpgfile = Image.open(name)
    #     pylab.subplot(leng/10,10,j+1)
    #     pylab.imshow(jpgfile)
    #     pylab.axis('off')
    # pylab.show()
    if i==0:
        continue

    rows=10
    list=np.loadtxt('namelist_'+i+'.txt')
    list=list[0:50]
    mostimp=list[0:rows]
    listtime=np.copy(list)
    listtime.sort()
    maxlen=0
    rowdata=[]
    all=[]
    for m in xrange(len(listtime)):
        if listtime[m] not in mostimp:
            rowdata=rowdata+[listtime[m]]
        else:
            rowdata=rowdata+[listtime[m]]
            all.append(rowdata)

            if len(rowdata) > maxlen:
                maxlen = len(rowdata)
            rowdata=[]

    for m in xrange(len(all)):
        addon=maxlen - len(all[m])
        all[m] = [-1]*addon  + all[m]



    fig=pylab.figure(figsize=(10,8),dpi=100)
