#!/usr/bin/python
#get onsets


import numpy as np
import glob
import os
#import fnmatch
import pdb
import pandas

basepath='/Users/gracer/Desktop/data'
os.chdir(basepath)

onsets=[]
duration=[]
RT=[]
trialT=[]
action=[]
for ons_file in glob.glob('sub-*/func/sub-*bart_events.tsv'):
    print("starting %s"%ons_file)
    sub=ons_file.split('/')[0]
    if os.path.exists(os.path.join(basepath, sub, 'func','onsets'))==False:
        os.makedirs(os.path.join(basepath, sub, 'func','onsets'))
    x=pandas.read_csv(ons_file, sep='\t')
    header = ["onset", "duration", "reaction_time"]
    x.to_csv('~/Desktop/trash/%s_output.csv'%sub, columns = header, index=False, header=False)
    pdb.set_trace()        
#    onsets.append(x.iloc[:,0])
#    duration.append(x.iloc[:,1])
#    RT.append(x.iloc[:,2])
#    trialT.append(x.iloc[:,4])
#    action.append(x.iloc[:,6])
#    with open(ons_file,'r') as f:
#        for line in f.readlines()[:]:
#            print("HI GRACE")
#            l_s=line.strip().split('\t')
#            onsets.append(l_s[0])
#            duration.append(l_s[1])
#            RT.append(l_s[2])
#            trialT.append(l_s[4])
#            action.append(l_s[6])
#    filename=ons_file.split('/')[2].split('.')[0]
#    print(filename)
#    ons_array=np.array(onsets)
#    pdb.set_trace()
#    print ons_array
#    pdb.set_trace()
#    baloon=np.zeros(ons_array.size)
#    print(baloon)
#    pdb.set_trace()
#    baloon[np.array(trialT)=='BALOON']='1'
#    baloon[np.array(trialT)=='CONTROL']='0'
#    cash=np.array(onsets)
#    cash[np.array(action)=='ACCEPT']='0'
#    cash[np.array(action)=='CASHOUT']='1'
#    cash[np.array(action)=='EXPLODE']='-1'
#    meanrt=np.mean(RT)
#    finalrt=RT-meanrt
#    
#  
#    f_RT=open(os.path.join(basepath, sub, 'func','onsets','ons_RT_'+filename+'.txt'), 'w')
#    f_TT=open(os.path.join(basepath, sub, 'func','onsets','ons_TT_'+filename+'.txt'), 'w')
#    f_ACT=open(os.path.join(basepath, sub, 'func','onsets','ons_ACT_'+filename+'.txt'), 'w')
#    
#    for t in range(len(onsets)):
#        f_RT.write('%f\t%f\t%f\n' %(onsets[t],duration[t],finalrt[t]))
#        f_ACT.write('%f\t%f\t%f\n' %(onsets[t],duration[t],cash[t]))
#        f_TT.write('%f\t%f\t%f\n' %(onsets[t],duration[t],baloon[t]))
#        
#
#    f_RT.close()    
#    f_TT.close()
#    f_ACT.close()
#    pdb.set_trace()
#    

    
    



