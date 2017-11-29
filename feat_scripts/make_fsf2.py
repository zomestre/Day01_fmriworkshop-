#!/usr/bin/env python

import os
import glob
import fnmatch
import argparse

def create_fsf2(basedir,repl_dict, indir,arglist,fsfdir):
    if arglist['TASK']==False:
        print("please say which task to run on")
    else:
        for dirp in glob.glob(os.path.join(indir,'sub-*')):
            os.chdir(dirp)
            for feat in glob.glob('*.feat'):
                if fnmatch.fnmatch(feat,'%s2.feat'%arglist['TASK']):
                    print('this is the second fake run')
                    funcrun2=os.path.join(dirp,feat)
                    repl_dict.update({'SECOND':funcrun2})
                elif fnmatch.fnmatch(feat,'%s.feat'%arglist['TASK']):
                    print('this is the real run')
                    funcrun=os.path.join(dirp,feat)
                    repl_dict.update({'FUNCRUN':funcrun})
                else:
                    print('this isnt the right task')
        
            sub=dirp.split('/')[-1]
            repl_dict.update({'SUB':sub})
            output=os.path.join(dirp,'%s.gfeat'%arglist['TASK'])
            repl_dict.update({'OUTPUT':output})
            print(repl_dict)
            with open(os.path.join(fsfdir,'design2.fsf'),'r') as infile:
                tempfsf=infile.read()
                for key in repl_dict:
                    tempfsf = tempfsf.replace(key, repl_dict[key])
                    with open(os.path.join(dirp,'%s.fsf'%(arglist['TASK'])),'w') as outfile:
                        outfile.write(tempfsf)
                    outfile.close()
            infile.close()      

def main():
#globals
    repl_dict={}
    basedir='/Users/gracer/Desktop/data'
    fsfdir='/Users/gracer/Google Drive/fMRI_workshop/scripts/fsf_files'
    indir=os.path.join(basedir,'derivatives','task')
    repl_dict={}
    parser=argparse.ArgumentParser(description='making fsf files')
    parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we using?')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)

    create_fsf2(basedir,repl_dict, indir,arglist,fsfdir)

main()
os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')