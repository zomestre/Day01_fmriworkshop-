#!/usr/bin/env python
import glob
import subprocess 
import os

#mcflirtdefault='-plots -sinc_final'
#'betfunc':"'bet %s/bold_mcf.nii.gz %s/bold_mcf_brain.nii.gz -F
#'bet %s %s -f 0.3 -R,

basedir='/Users/gracer/Google Drive/fMRI_workshop/data'

os.chdir(basedir)

for nifti in glob.glob('cs*/BOLD/*.nii.gz'):
	print("Starting BET on "+nifti)
	INPUT=os.path.join(basedir,nifti)
	output=INPUT.strip('.nii.gz')
	BET_OUTPUT=os.path.join(basedir,output+'_brain')
	print(BET_OUTPUT)
	subprocess.call(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/bet",INPUT,OUTPUT,"-F"])
