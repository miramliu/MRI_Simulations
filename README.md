# MRI_Simulations
 These are simulations written for visual demonstrations of basic principles of MRI.\
 Packages required include numpy, matplotlib, os, glob, fnmatch, mpl_toolkits, csv, scipy, pickly, seaborn, and tkinter.\
 It is split into three folders. "Basic MR" focuses on simple T1 and T2 MR sequences. "k-space" goes through an example of how k-space and the spatial domain relate using an analogy of music and an example of reconstructing an image of a healthy brain. "MRAcquisition" goes through how frequency and phase ancoding work visually and in fourier space. \
 The code is provided, rather than just images, so that the basic mathematics and physics written out in the functions provided can be seen, modified, and hopefully understood! They are all run in basic jupyter notebooks, and are less GUI just so you can see a bit more behind the scenes. And these are all just for fun demonstration :)
 
 Any questions can be sent to Mira Liu at liusarkarm@uchicago.edu\
May 2023

# Basic MR
 MR_Physics_Diagrams shows basic MR signal oscillation and decay in 2D, and in 3D. Further explanation is included in the chapter about MR physics.
 
 PulseSequenceDiagrams attempts to show hypothetical signal for Inversion Recovery (IR), Gradient Echo (GRE), and Spin Echo (SE). It lays out mathematical signal equations over time as functions of hypothetical T1, T2, TE, TR, and TI times. The signal equations plotted are written as functions.
 
# k-space

Here are code and simulations written for the south side science festival, condensed into RunMe.ipynb. It links the way we interpret sounds like guitar chords to how MRI uses fourier space to image with 2D spatial frequency. The intended audience was for students around middle school age.

For more complex code and simulations, see RunMe-Original, and ScratchCode, which include more in-depth simulations that were removed for the demonstration. For static images, see MMRAcquisition/MRI_Acquisition.ipynb

For more focus on how fourier space relates to spatial frequency, see PlanarWave_FFT_Scratch.

# MRAcquisition

MRI_Acquisition attempts to show: 1) how frequency encoding works to sample frequency strength over time along the x-axis in the spatial domain. 2) How shifting of the phase step translates to rotation of a spatial frequency in the spatial dommain. 3) How that rotation is recorded in k-space. 4) How the acquisition in k-space leads to sampling of spatial frequencies for acquisition of the fourier transform that MRI uses. 

MRI_VaryingSpatialFrequency attempts to show the 1D analysis of spatial frequency over time through basic fourier analysis. It shows the frequency and the phase as the location in k-space (and k-space trajectory) and the commplex portion of a fourier transform. 




