__author__ = 'yingboli'
import colorsys
import numpy as np
import glob
from PIL import Image
from skimage.color import convert_colorspace
import matplotlib.pyplot as plt

path='../data/image/'
folder=['1301','1304']

for i in xrange(len(folder)):
    list=glob.glob(path+folder[i]+'/*.jpg')
    list.sort()
    for j in list:
        im = Image.open(j)
        im = convert_colorspace(im, 'RGB', 'HSV')
        h=np.bincount(np.round(im[:,:,0].flatten()*255.).ravel().astype(int),minlength=256)
        h=h*1.0/(np.sum(h))
        s=np.bincount(np.round(im[:,:,1].flatten()*255.).ravel().astype(int),minlength=256)
        s=s*1.0/(np.sum(s))
        hsvhist=np.concatenate((h,s),axis=0)
        np.savetxt('../data/hsv/'+j.split('image/')[-1].split('.jpg')[0]+'.txt',hsvhist)
