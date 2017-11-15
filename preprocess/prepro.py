#!/usr/bin/env python
import glob
import os
import pdb
#import sys
import argparse
import shutil
import fnmatch

def prepro(basedir, args, arglist, outhtml, out_bad_bold_list):
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
            
#motion correction
    if args.MOCO==False:
        print("please set a threshold for the FD, a good one is 0.9")
    else:
        print("starting motion correction")
        if os.path.exists(out_bad_bold_list):
            os.system("rm %s"%(out_bad_bold_list))
            os.system("rm %s"%(outhtml))
        os.chdir(os.path.join(basedir))
        for dir in glob.glob('sub-*/func'):
            if not os.path.exists(os.path.join(basedir,dir,'motion_assessment')):
                os.makedirs(os.path.join(basedir,dir,'motion_assessment'))
            os.chdir(os.path.join(basedir, dir))
            for input in glob.glob('*.nii.gz'):
                output=input.strip('.nii.gz')
                if input.endswith('mcf'):
                    print(output+' exists, skipping')
                else:
                    os.system("mcflirt -in %s -plots"%(output))
                    os.system("fsl_motion_outliers -i %s -o motion_assessment/confound.txt --fd --thresh=%s -p motion_assessment/fd_plot -v > motion_assessment/outlier_output.txt"%(output,arglist['MOCO']))
                    os.system("cat motion_assessment/outlier_output.txt >> %s"%(outhtml))
                    plotz=os.path.join(basedir,dir,'motion_assessment','fd_plot.png')
                    os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(output,plotz,'100%', outhtml))
                    if os.path.exists("%s_mcf.par"%(output)):
                        if os.path.exists(os.path.join(basedir,dir,'motion_assessment',"%s_mcf.par"%(output))):
                            usr_in=raw_input('looks like par exists, continue?')
                            if fnmatch.fnmatch(usr_in, 'n'):
                                print("not saving the par file in motion_assessment")
                            elif fnmatch.fnmatch(usr_in, 'y'):
                                os.remove(os.path.join(basedir,dir,'motion_assessment',"%s_mcf.par"%(output)))
                                shutil.move("%s_mcf.par"%(output),os.path.join(basedir,dir,'motion_assessment'))
                            else:
                                print("Please answer y for yes and n for n")
                                continue
                    pdb.set_trace()
 

def main():
    basedir='/Users/gracer/Desktop/data'
    writedir='/Users/gracer/Desktop/trash'
    
    # I'm using a big html file to put all QA info together.  If you have other suggestions, let me know!
    outhtml = os.path.join(writedir,'bold_motion_QA.html')
    out_bad_bold_list = os.path.join(writedir,'subs_lose_gt_45_vol_scrub.txt')

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
    parser.add_argument('-moco',dest='MOCO',
                        default=False, help='this is using fsl_motion_outliers to preform motion correction and generate a confounds.txt as well as DVARS')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    prepro(basedir, args, arglist, outhtml, out_bad_bold_list)
main()