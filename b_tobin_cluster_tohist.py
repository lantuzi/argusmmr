__author__ = 'lantuzi'
# read sift file and then convert to bin format, and then cluster to 1000 centers. at last compute the hist of each frame
import os
import numpy as np
import glob
from scipy import cluster

path="C:\\Users\\lantuzi\\Desktop\\argusvideo\\data"
foldername=['1301', '1304']
numfeature=100
dimension=128
inteval=12
#----------1. convert pkeys to bin------------
'''
bin_all=[]
bin_all_byfolder=[]
for i in xrange(len(foldername)):
    list=glob.glob(path+'\\sift\\'+foldername[i]+'\\*.pkeys')
    list.sort()
    binfolder=[]
    for j in xrange(len(list)):
        bin=[]
        with open(list[j]) as f:
            sift = []
            for line in f:
                line = line.split() # to deal with blank
                if line:            # lines (ie skip them)
                    line = [float(k) for k in line]
                    sift.append(line)
        if len(sift)==numfeature*inteval+1:
            for m in xrange(numfeature):
                temp=[]
                for n in xrange(2,2+inteval-1):
                    temp+=sift[m*inteval+n]
                bin.append(temp)
            bin=np.array(bin)
            np.savetxt(path+'\\bin\\'+foldername[i]+'\\'+str(j+1).zfill(4)+'.bin',bin,fmt='%i')
'''
#----------2.compute clustering centers from bin------------
'''
bin_all=[]
mark=[]
for i in xrange(len(foldername)):
    list=glob.glob(path+'\\bin\\'+foldername[i]+'\\*.bin')
    list.sort()
    nameframeeach=[]
    for j in list:
        print j
        nameframeeach.append(j.split('\\')[-1].split('.bin')[0])
        bin=np.loadtxt(j)
        if len(bin)!=numfeature:
            mark.append(j)
            continue
        if bin_all==[]:
            bin_all=bin
        else:
            bin_all=np.concatenate((bin_all, bin), axis=0)
    np.savetxt(path+'\\cluster\\namelist_'+foldername[i]+'.txt',nameframeeach,fmt='%s')
print len(bin_all)
print mark
bin_all=np.array(bin_all)
np.save('bin_all.npy',bin_all)
#bin_all=np.load('binall.npy')
res,idx = cluster.vq.kmeans2(bin_all,500,iter=20)
bin_all=[]
np.savetxt(path+'\\cluster\\clusterindex.txt',idx,fmt='%i')
'''
#----------3.convert labels to histogram------------
idx=np.loadtxt(path+'\\cluster\\clusterindex.txt',dtype='int')
lengtotal=0
for i in xrange(2):
    namelist=np.loadtxt(path+'\\cluster\\namelist_'+foldername[i]+'.txt',dtype='int')
    data=idx[lengtotal:lengtotal+len(namelist)*numfeature]
    hist=[]
    for j in xrange(len(namelist)):
        temp=data[j*numfeature:(j+1)*numfeature]
        hist1=np.bincount(temp, minlength=501)
        hist1[0]=namelist[j]
        hist.append(hist1)
    np.savetxt(path+'\\hist\\'+foldername[i]+'.txt',hist,fmt='%i')
    lengtotal+=len(namelist)

