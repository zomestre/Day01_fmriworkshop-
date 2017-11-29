import os
import glob
import shutil

basedir='/Users/gracer/Desktop/data/derivatives/task'

for dire in glob.glob(os.path.join(basedir,'sub-*','grace_edit','*.feat')):
  os.chdir(dire)
  if len(glob.glob('stats/cope*.nii.gz'))==2:
    print(dire+' has 2 cope files :D')
  else:
    print(dire+' is missing copes, need to rerun')
    shutil.rmtree(dire)
