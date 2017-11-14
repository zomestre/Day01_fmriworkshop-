#!/usr/bin/env python
import glob
import os
import pdb
#import sys
import argparse

def prepro(basedir, args, arglist):
#bet
    #print(args)
    #pdb.set_trace()
    if args.STRIP==True:
        print("starting bet")
        os.chdir(os.path.join(basedir))
        for nifti in glob.glob('sub-*/func'):
            os.chdir(os.path.join(basedir, nifti))
            for input in glob.glob('*.nii.gz'):
                output=input.strip('.nii.gz')
                if os.path.exists(output+'brain.nii.gz'):
                    print(output+' exists, skipping')
                else:
                    BET_OUTPUT=output+'_brain'
                    x=("/usr/local/fsl/bin/bet %s %s -F"%(input, BET_OUTPUT))
                    print(x)
                    os.system(x)
                    pdb.set_trace()
#reorienting
    if args.REOR==True:
        print("starting reorientation, please check that it is correct at the break if yes, click c, if no click q")
        os.chdir(os.path.join(basedir))
        for nifti in glob.glob('sub-*/func'):
            os.chdir(os.path.join(basedir, nifti))
            for input in glob.glob('*.nii.gz'):
                output=input.strip('.nii.gz')
                os.system("fslswapdim %s z -x -y %s_swapped"%(output, output))
                pdb.set_trace()

#trimming
    if args.TRIM==True:
        if args.EX==False:
            print("please set how many TRs to trim")
        elif args.TOT==False:
            print("please set the maximum TRs possible")
        else:
            print("looks good")
            print(arglist['EX'])
            os.chdir(os.path.join(basedir))
            for nifti in glob.glob('sub-*/func'):
                os.chdir(os.path.join(basedir, nifti))
                for input in glob.glob('*.nii.gz'):
                    output=input.strip('.nii.gz')
                    os.system("fslroi %s %s_trimmed %s %s"%(output, output, arglist['EX'], arglist['TOT']))
                    pdb.set_trace()
            

def main():
    basedir='/Users/gracer/Google Drive/fMRI_workshop/data'
    parser=argparse.ArgumentParser(description='preprocessing')
    parser.add_argument('-bet',dest='STRIP',action='store_true',
                        default=False, help='bet via fsl using defaults for functional images')
    parser.add_argument('-reorient',dest='REOR',action='store_true',
                        default=False, help='using fslswapdim to fix orientation problems')
    parser.add_argument('-trim',dest='TRIM',action='store_true',
                        default=False, help='this trims extra trs, this requires the -extra and -total flags')
    parser.add_argument('-extra',dest='EX',
                        default=False, help='TRs to remove')
    parser.add_argument('-total',dest='TOT',
                        default=False, help='total TRs')
    parser.add_argument('-moco',dest='MOCO',action='store_true',
                        default=False, help='this is using fsl_motion_outliers to preform motion correction and generate a confounds.txt as well as DVARS')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    prepro(basedir, args, arglist)
main()