#import sys
import glob
import os
from subprocess import check_output
import pdb

#cs154_mkC.feat
#cs154_mkC
#things I will need
#Output directory
#TR
#Total volumes
#Input
#EV files
#Structural image
def create_fsf(basedir,repl_dict,outdir):
    os.chdir(basedir)
    for sub in glob.glob('sub-*'):
        repl_dict.update({'SUB':sub})
        print(sub)
        for scan in glob.glob(os.path.join(sub,'func','*_mcf.nii.gz')):
            pdb.set_trace()
            print(scan)
            task=scan.split('/')[2].split('_')[1].split('-')[1]
            funcrun=os.path.join(basedir,scan)
            repl_dict.update({'FUNCRUN':funcrun})
            ntmpts=check_output(['fslnvols',funcrun])
            repl_dict.update({'NTIMEPOINTS':ntmpts})
            trs=check_output(['fslval','%s'%(funcrun),'pixdim4',scan])
            repl_dict.update({'TRS':trs})
            output=os.path.join(outdir,sub,task)
            repl_dict.update({'OUTPUT':output})
            anat=os.path.join(basedir,sub,'anat','%s_T1w.nii.gz'%(sub))
            repl_dict.update({'ANAT':anat})
            print(repl_dict)
            with open(os.path.join(basedir,'design.fsf'),'r') as infile:
                tempfsf=infile.read()
                for key in repl_dict:
                    tempfsf = tempfsf.replace(key, repl_dict[key])
                    with open(os.path.join(outdir,sub,'%s.fsf'%(sub)),'w') as outfile:
                        outfile.write(tempfsf)
                       

def main ():
  basedir='/Users/gracer/Desktop/data'
  outdir=os.path.join(basedir,'derivatives','task')
  repl_dict={}
  create_fsf(basedir,repl_dict, outdir)
main()
