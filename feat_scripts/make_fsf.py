#import sys
import glob
import os
from subprocess import check_output
import pdb
import argparse
import fnmatch
#cs154_mkC.feat
#cs154_mkC
#things I will need
#Output directory
#TR
#Total volumes
#Input
#EV files
#Structural image
def create_fsf(basedir,repl_dict,outdir,args,argslist):
    os.chdir(basedir)
    for scan in glob.glob('sub-*/func/*_mcf.nii.gz'):
        print(scan)
        sub=scan.split('/')[2].split('.')[0].strip('_mcf')
        task=scan.split('/')[2].split('_')[1].split('-')[1]
        print(sub)
        repl_dict.update({'SUB':sub})
        funcrun=os.path.join(basedir,scan)
        repl_dict.update({'FUNCRUN':funcrun})
        ntmpts=check_output(['fslnvols',scan])
        repl_dict.update({'NTIMEPOINTS':ntmpts})
        trs=check_output(['fslval','%s'%(scan),'pixdim4',scan])
        repl_dict.update({'TRS':trs})
        output=os.path.join(outdir,sub,task)
        repl_dict.update({'OUTPUT':output})
        print(repl_dict)
        pdb.set_trace()
        #repl_dict.update({'DIR':dir})
        #repl_dict.update({'SUB':sub})
#    		os.chdir(os.path.join(subdir,dir))
##    		for name in glob.glob('BOLD/wtp_run*'):
#      		funcrun='filtered_func_data_clean.nii.gz'
##      		funcrun=funcrun.strip('BOLD/')
#      		repl_dict.update({'FUNCRUN':funcrun})
##      		runnum2=funcrun.split("_")[1]
#      			#print runnum2
##      		runnum=runnum2.strip('run0')
#      			#print runnum
##      		repl_dict.update({'RUNNUM':runnum})
#      		print repl_dict
##      		os.chdir(os.path.join(basedir,dir,name))
#      		ntmpts=check_output(['fslnvols','filtered_func_data_clean.nii.gz'])
#      		repl_dict.update({'NTIMEPOINTS':ntmpts})
#		sub_file=sub+'.fsf'
#     		with open(os.path.join(basedir, 'scripts','milkshake','design.fsf'),'r') as infile:
#        		tempfsf=infile.read()
#        		for key in repl_dict:
#         			tempfsf = tempfsf.replace(key, repl_dict[key])
##          			with open(basedir + dir + '/wtp_model/' + 'run0'+runnum + '.fsf','w') as outfile:
#          			with open(os.path.join(basedir, 'data','eric_data','design_files','milkshake','grace_edit',sub_file),'w') as outfile:
#            				outfile.write(tempfsf)
#            				os.chdir(os.path.join(basedir,'scripts','milkshake'))

def main ():
  basedir='/Users/gracer/Desktop/data'
  outdir=os.path.join(basedir,'derivatives','task')
  repl_dict={}
  parser=argparse.ArgumentParser(description='preprocessing')
  parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we working on today?')
  args = parser.parse_args()
  argslist={}
  for a in args._get_kwargs():
      argslist[a[0]]=a[1]
  print(argslist)
  create_fsf(basedir,repl_dict, outdir,args,argslist)
main()
