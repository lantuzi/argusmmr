import numpy as np
from matplotlib import pylab
from PIL import Image


foldername=['1301', '1304']
imagepath='../data/'

for i in foldername:
    if i=='1301':
        continue
    list=np.loadtxt(imagepath+'summary/namelist_'+i+'.txt')

    list3=list[1:51]
    list3.sort()
    leng=len(list3)
    fig=pylab.figure(figsize=(100,80),dpi=100)
    fig.subplots_adjust(hspace=0.,wspace=0.05)
    for j in xrange(leng):
        name=imagepath+'image/'+i+'/'+str(int(list3[j])).zfill(4)+'.jpg'
        jpgfile = Image.open(name)
        pylab.subplot(leng/10,10,j+1)
        pylab.imshow(jpgfile)
        pylab.axis('off')
    pylab.show()


    # rows=10
    # list=np.loadtxt('namelist_'+i+'.txt')
    # list=list[1:51]
    # mostimp=list[0:rows]
    # listtime=np.copy(list)
    # listtime.sort()
    # maxlen=0
    # rowdata=[]
    # all=[]
    # for m in xrange(len(listtime)):
    #     if listtime[m] not in mostimp:
    #         rowdata=rowdata+[listtime[m]]
    #     else:
    #         rowdata=rowdata+[listtime[m]]
    #         all.append(rowdata)
    #
    #         if len(rowdata) > maxlen:
    #             maxlen = len(rowdata)
    #         rowdata=[]
    #
    # for m in xrange(len(all)):
    #     addon=maxlen - len(all[m])
    #     all[m] = [-1]*addon  + all[m]
    #
    #
    #
    # fig=pylab.figure(figsize=(10,8),dpi=100)
