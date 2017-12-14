# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:53:59 2017

@author: ZFrench
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    print('Hello data in the path '+basedir)
def main():
    basedir='C:\\Users\\ZFrench\\Desktop\\Research\\UNCworkshop\\ds000030_R1.0.4'
    prepro(basedir)

main()

input=glob.glob('C:\\Users\\ZFrench\\Desktop\\Research\\UNCworkshop\\ds000030_R1.0.4\\ds000030_R1.0.4\\sub-*\\func\\sub-*bart*.nii.gz')
print(input)

x=input[0]
print('my path is '+x)
y=x.split('\\')
print(y)
whatcomp=y[2]
sub=y[6]

#print(sub)

sub=input[1].split('/')[6]
print(sub)

print(os.system('echo $FSLDIR))
os.system(bet )