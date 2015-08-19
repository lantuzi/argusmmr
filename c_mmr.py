__author__ = 'lantuzi'
import numpy as np
from scipy.spatial.distance import cosine
from scipy.stats import gmean

sumlenall=[51,101]
path="C:\\Users\\lantuzi\\Desktop\\argusvideo\\data"
foldername=['1301', '1304']
sumframename=[]

for sumlen in sumlenall:
    for i in xrange(len(foldername)):
        data=np.loadtxt(path+'\\hist\\hist'+foldername[i]+'.txt')
        namelist=data[:,0]
        hist=data[:,1:]
        leng,numfeature =hist.shape
        # simmat=np.zeros([leng,leng])
        # for m in xrange(leng):
        #     for n in xrange(leng):
        #         if simmat[m,n]==0:
        #             simmat[m,n]=1.0-cosine(hist[m,:],hist[n,:])
        #             simmat[n,m]=simmat[m,n]
        simmat=np.load(path+'\\hist\\simmat_'+foldername[i]+'.npy')
        # first frame in mmr
        result=[]
        tempsim=0
        rec=-1
        for m in xrange(leng):
            ttp=simmat[m,:]
            ttp2=ttp[ttp!=0]
            tempsim2=gmean(ttp2, axis=0)**len(ttp2)**(1.0/len(ttp))
            if tempsim2 > tempsim:
                rec=m
                tempsim = tempsim2
        result.append(rec)
        # MMR procedure
        lamda=0.7
        for k in xrange(sumlen-1):
            if k==int(sumlen*0.7):
                lamda=1.0-lamda
            simtemp=-100000
            for m in xrange(leng):
                if m in result:
                    continue
                # mmr1
                temp=simmat[m,:]
                temp2=np.delete(temp, result+[m])
                mmr1=np.mean(temp2)
                # mmr2
                mmr2=np.max(temp[result])
                #mmr
                mmr=lamda*mmr1-(1.0-lamda)*mmr2
                if mmr > simtemp:
                    simtemp = mmr
                    rec = m
            result.append(rec)
        np.savetxt(path+'\\summary\\namelist_'+foldername[i]+'_'+str(sumlen-1)+'.txt',namelist[result],fmt='%i')
