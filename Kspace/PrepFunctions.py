# PrepCode
# This contains functions used in Scratch and RunMe for the demonstrations.

import numpy as np
import matplotlib
import matplotlib.pyplot as pl
import csv
import scipy.optimize as op
import scipy.stats
from scipy.optimize import curve_fit
import scipy.io
from scipy.stats import rice

import random
import pickle
import seaborn as sns

import numpy as np
from scipy.stats import ttest_ind, ttest_ind_from_stats, wilcoxon,ttest_rel, pearsonr
from scipy.special import stdtr
import csv
import pandas as pd

import sys 
import os

import tkinter as tk
from tkinter import ttk

    


# code used in RunMe
def ShowThreeWaves(x,wave1,wave2,wave3):
    fig, (ax1,ax2,ax3,ax4) = pl.subplots(4,1,figsize = (7,7))
    ax1.plot(x,wave1,color = 'red')
    ax1.set_title('Middle C')
    ax1.set_ylabel('261 Hz')

    ax2.plot(x,wave2,color = 'purple')
    ax2.set_title('Middle E')
    ax2.set_ylabel('330 Hz')

    ax3.plot(x,wave3,color = 'green')
    ax3.set_title('Middle G')
    ax3.set_ylabel('392 Hz')

    ax4.plot(x,wave1+wave2+wave3)
    ax4.set_title('C Chord')
    ax4.set_xlabel('time (s)')
    #ax4.set_title('261 Hz + 330 Hz + 392 Hz')
    fig.tight_layout()
    pl.show()
    return

def ShowFTOfWaves(x,ft_freq,wave1,wave2,wave3,ft_sin1,ft_sin2,ft_sin3,wavesum,ft_sinsum):

    # Set up subplots
    fig, ((ax1, ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = pl.subplots(4,2,figsize = (7,7))

    # plot wave 1 with 5 cycles per second
    ax1.plot(x,wave1, color = 'red')
    ax1.set_title('261 Hz (Middle C)')
    ax2.plot(ft_freq,abs(ft_sin1),color = 'red')
    ax8.vlines(x=261,ymin =0,ymax=5000,color = 'red',label = 'C')
    ax2.set_title('FT of 261 Hz')
    ax2.set_xlim([0,500])

    # plot wave 2 with 329
    ax3.plot(x,wave2,color = 'purple')
    ax3.set_title('329 Hz (E)')
    ax4.plot(ft_freq,abs(ft_sin2),color = 'purple')
    ax4.set_title('FT of 329 Hz')
    ax8.vlines(x=320,ymin =0,ymax=4000,color = 'purple',label = 'E')
    ax4.set_xlim([0,500])

    # plot wave 3 with 392 
    ax5.plot(x,wave3,color = 'green')
    ax5.set_title('392 Hz (G)')
    ax6.plot(ft_freq,abs(ft_sin3),color = 'green')
    ax6.set_title('FT of 392 Hz')
    ax8.vlines(x=400,ymin =0,ymax=4000,color = 'green',label = 'G')
    ax6.set_xlim([0,500])

    # plot of Chord
    ax7.plot(x,wavesum)
    ax7.set_title('C Chord')
    ax8.plot(ft_freq,abs(ft_sinsum))
    ax8.set_title('FT of C Chord')
    ax8.set_xlim([0,500])
    ax8.legend(prop={'size': 6})


    fig.tight_layout()
    return


def ShowFTof2Dwaves(x,ft_freq,img,kspace):
    fig, ((ax1, ax2),(ax3,ax4)) = pl.subplots(2,2)

    ax1.imshow(img,cmap = 'gray',extent = [0,1,0,1])
    ax1.set_title('2d planar wave')
    ax2.plot(x,img[51])
    ax2.set_title('Cross section of 2d planar wave')

    #so this has wavelength of 30
    # pixel size of 3

    ax3.imshow(np.abs(kspace),cmap = 'gray',extent = [-50,50,-50,50])
    ax3.set_title('Fourier Transform of 2d planar wave')
    ax4.plot(ft_freq,np.abs(kspace)[50])
    ax4.set_title('Cross section of Fourier Transform')
    fig.tight_layout()
    pl.show()


    return




# Code from previous scratch
def readimage(filepath):
    ds = dicom.dcmread(filepath)
    img = ds.pixel_array
    print(np.shape(img))

    pl.imshow(img,cmap = 'gray')
    pl.colorbar()
    pl.show()
    fov_img = np.shape(img)[0]
    return img, fov_img

def fouriertransform(img):
    ft = np.fft.ifftshift(img)
    ft = np.fft.fft2(ft)
    kspace = np.fft.fftshift(ft) #moves zero frequency component to center
    kx_ax = np.fft.fftfreq(np.shape(img)[0],1) #goes from -.5 to +.5 frequency
    print('min kx:',min(kx_ax),'\nmax kx:', max(kx_ax),'\nDelta kx = ',1/fov_img)
    fig, (ax1, ax2) = pl.subplots(1,2)
    ax1.imshow(img,cmap = 'gray')
    ax2.imshow(np.abs(kspace),vmin = 0,vmax = 4000,extent = [-.5, .5, -.5, .5],cmap = 'gray')
    #pl.colorbar()
    pl.show()
    
    return kspace



# assumed odd and equal nummber of nx and ny
# makes list of indices to do a spiral
# see 8/20/22 notes
def Spiral(nx):
    SpiralArray_x = [] 
    SpiralArray_y = []
    center = int(nx/2)
    # add center as first 
    x,y = center,center
    SpiralArray_x.append(x)
    SpiralArray_y.append(y)
    for j in np.arange(1,nx,2): #from 0 to the number of nx there is in steps of 2
        # do x = x+1 and then y = y-1 a certain number of times
        for k in range(j):
            x = x+1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
        for m in range(j):
            y = y-1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
        for p in range(j+1):
            x = x-1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
        for q in range(j+1):
            y = y+1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
    for v in range(nx-1):
        x = x+1
        SpiralArray_x.append(x)
        SpiralArray_y.append(y)
        
    SpiralArray = np.vstack((SpiralArray_x,SpiralArray_y))
    
    return SpiralArray

#this will avoid doubling with mirroring (see 8/29/22)
def cropped_spiral(nx):
    SpiralArray_x = [] 
    SpiralArray_y = []
    center = int(nx/2)
    # add center as first 
    x,y = center,center
    SpiralArray_x.append(x)
    SpiralArray_y.append(y)
    for j in range(int(nx/2)):
        y = center + j
        x = center
        SpiralArray_x.append(x)
        SpiralArray_y.append(y)
        for k in range(j):
            x = x+1 
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
        for m in range(j*2):
            y = y - 1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
        for p in range(j-1):
            x = x-1
            SpiralArray_x.append(x)
            SpiralArray_y.append(y)
    
    SpiralArray = np.vstack((SpiralArray_x,SpiralArray_y))
    
    return SpiralArray


#given image and region of k-space, watch spatial domain growth as more kspace is imaged 
def watchFigureConstruction(kspace,fov_img,xlim,filename):
    cropped_kspace = kspace[round(fov_img/2)-xlim:round(fov_img/2)+xlim,round(fov_img/2)-xlim:round(fov_img/2)+xlim]
    kspace_dim = len(cropped_kspace) #dimensions of selected k-space
    kspace_points = len(SpiralAcquisition[0]) #number of points in selected k-space

    SpiralAcquisition = cropped_spiral(kspace_dim) #get spiral acuisition points
    center = int(kspace_dim/2)

    # empty data wanted
    spiraling_k = np.zeros(np.shape(cropped_kspace))
    superimpose_img = np.zeros(np.shape(cropped_kspace))
    stacked_iffts = np.zeros((kspace_dim,kspace_dim,int(kspace_points/10)+1))
    stacked_kspace = np.zeros((kspace_dim,kspace_dim,int(kspace_points/10)+1))
    
    ten_counter = np.arange(0,kspace_points,10) #all points in kspace in steps of 10
    counter = 0
    for j in np.arange(0,kspace_points): #for each point in this spiral, i.e. all of k-space
        # get mask that gets that point and it's corresponding buddy 
        mask = np.zeros(np.shape(cropped_kspace))

        kx = SpiralAcquisition[0][j]
        ky = SpiralAcquisition[1][j]
        mask[kx,ky]  = 1
        # now get it reflected across the origin as well 
        dkx = center - kx
        dky = center - ky

        mirror_kx = center + dkx 
        mirror_ky = center + dky
        mask[mirror_kx, mirror_ky] = 1

        # now get those points in k-space
        kspace_point = cropped_kspace*mask 

        #show k-space growing
        spiraling_k = spiraling_k + kspace_point # and add it to show the growing k-space


        # now get inverse ft of that point only every 10
        if j in ten_counter:
            stacked_kspace[:,:,counter] = np.abs(spiraling_k)
            ift = np.fft.fftshift(spiraling_k)
            ift = np.fft.ifft2(ift)
            iimg = np.fft.ifftshift(ift) # want to save this! 
            stacked_iffts[:,:,counter] = np.abs(iimg)
            counter = counter + 1
            
    savename = '/data/' + filename + '_superposition.pickle'
    with open(savename,'wb') as handle: 
        pickle.dump(stacked_iffts,handle)
    savename = savename = '/data/' + filename + '_superposition_kspace.pickle'
    with open(savename,'wb') as handle: 
        pickle.dump(stacked_kspace,handle)
        
    return 

#given image and region of k-space, watch spatial domain growth as more kspace is imaged 
def watchKspacePlanar(kspace,fov_img,xlim,filename):
    cropped_kspace = kspace[round(fov_img/2)-xlim:round(fov_img/2)+xlim,round(fov_img/2)-xlim:round(fov_img/2)+xlim]
    kspace_dim = len(cropped_kspace) #dimensions of selected k-space
    kspace_points = len(SpiralAcquisition[0]) #number of points in selected k-space

    SpiralAcquisition = cropped_spiral(kspace_dim) #get spiral acuisition points
    center = int(kspace_dim/2)

    # empty data wanted
    spiraling_k = np.zeros(np.shape(cropped_kspace))
    superimpose_img = np.zeros(np.shape(cropped_kspace))
    stacked_maskiffts = np.zeros((kspace_dim,kspace_dim,int(kspace_points/10)+1))
    counter = 0
    for j in np.arange(0,kspace_points,10): #for each point in this spiral, i.e. all of k-space
        # get mask that gets that point and it's corresponding buddy 
        mask = np.zeros(np.shape(cropped_kspace))

        kx = SpiralAcquisition[0][j]
        ky = SpiralAcquisition[1][j]
        mask[kx,ky]  = 1
        # now get it reflected across the origin as well 
        dkx = center - kx
        dky = center - ky

        mirror_kx = center + dkx 
        mirror_ky = center + dky
        mask[mirror_kx, mirror_ky] = 1

        # now get those points in k-space
        kspace_point = cropped_kspace*mask 

        #show k-space growing
        spiraling_k = spiraling_k + kspace_point # and add it to show the growing k-space
        # now get inverse ft of that point
        ift = np.fft.fftshift(kspace_point)
        ift = np.fft.ifft2(ift)
        iimg = np.fft.ifftshift(ift) # want to save this! 
        stacked_maskiffts[:,:,counter] = np.abs(iimg)
        counter = counter + 1
            
    savename = '/data/' + filename + '_superposition_masks.pickle'
    with open(savename,'wb') as handle: 
        pickle.dump(stacked_maskiffts,handle)
        
    return 

def Display_Reconstruction(filename):
    image_name = '/data/' + filename + '_superposition.pickle'
    masks_name = '/data/' + filename + '_superposition_masks.pickle'
    kspace_name = '/data/' + filename + '_superposition_kspace.pickle'
    with open(image_name,'rb') as handle1:
        stack_image = pickle.load(handle1)
    with open(masks_name,'rb') as handle2:
        stack_waves = pickle.load(handle2)
    with open(kspace_name,'rb') as handle3:
        stack_kspace = pickle.load(handle3)

    fig, (ax1, ax2, ax3,ax4) = pl.subplots(1,4)
    ax4.imshow(img,cmap = 'gray')
    for i in np.arange(0,np.shape(stack_image)[2],4):
        ax1.imshow(stack_kspace[:,:,i],vmin = 0,vmax = 6000,extent = [-.5, .5, -.5, .5],cmap = 'gray')
        ax1.set_title('k-space')
        ax2.imshow(stack_waves[:,:,i],cmap = 'gray')
        ax2.set_title('Planar\nWaves')
        ax3.imshow(stack_image[:,:,i],cmap = 'gray')
        ax3.set_title('Image\nForming')
        pl.pause(.01)
