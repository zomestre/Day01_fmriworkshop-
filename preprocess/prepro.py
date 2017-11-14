#!/usr/bin/env python
import glob
import os
import pdb

#mcflirtdefault='-plots -sinc_final'
#'betfunc':"'bet %s/bold_mcf.nii.gz %s/bold_mcf_brain.nii.gz -F
#'bet %s %s -f 0.3 -R,

basedir='/Users/gracer/Google Drive/fMRI_workshop/data'

os.chdir(basedir)

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
