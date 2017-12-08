import os
import glob
import shutil
#import pdb
import datetime

def QA_writer(basedir,outfile,writedir):

    for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')):
        os.chdir(file)
        print(file)
        sub=file.split('/')[7]
        dict_of_files = {}
        for (dirpath, dirnames, filenames) in os.walk(file):
            for filename in filenames:
                if filename.startswith('fsl') or filename.startswith('vert'):
                    print('skipping')
                elif filename.endswith('.png'): 
                    dict_of_files[filename] = os.sep.join([dirpath, filename])

        for key in dict_of_files:
            os.system("echo '<p>=============<p> %s %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(sub,key,dict_of_files[key],'100%', outfile))
            #shutil.copy(dict_of_files[key],writedir)
        if os.path.exists(os.path.join(basedir,'fails'))==False:
            os.makedirs(os.path.join(basedir,'fails'))

        if len(glob.glob(os.path.join(file,'stats','cope*.nii.gz')))==4:
            print(file+' has 4 cope files :D')
        else:
            print(file+' is missing copes, need to rerun')
            name=file.split('/')[9].split('.')[0]
            shutil.copytree(file,os.path.join(basedir,'fail',sub,name))

def main():
    basedir='/Users/gracer/Desktop/data/derivatives/task'
    writedir='/Users/gracer/Desktop/data/'
    datestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    outfile = os.path.join(writedir,'lev1_QA_%s.html'%datestamp)        
    QA_writer(basedir,outfile,writedir)
main()

os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts')