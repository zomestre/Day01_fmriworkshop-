import os
import glob
import shutil



def QA_writer(basedir,f,writedir):

    for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')):
        os.chdir(file)
        print(file)
        f.write("<p>============================================")
        f.write("<p>%s"%(file))
        f.write("<IMG SRC=\"files/%s.design.png\">"%(file.replace("/", "_")))
        f.write("<IMG SRC=\"files/%s.design_cov.png\" >"%(file.replace("/", "_")))
        f.write("<IMG SRC=\"files/%s.disp.png\">"%(file.replace("/", "_")))
        f.write("<IMG SRC=\"files/%s.trans.png\" >"%(file.replace("/","_")))
        f.write("<p><IMG SRC=\"files/%s.example_func2highres.png\" WIDTH=1200>"%(file.replace("/","_")))
        f.write("<p><IMG SRC=\"files/%s.example_func2standard.png\" WIDTH=1200>"%(file.replace("/","_")))
        f.write("<p><IMG SRC=\"files/%s.highres2standard.png\" WIDTH=1200>"%(file.replace("/","_")))
        plotz=os.path.join(file,'reg','highres2standard.png')
        os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(file,plotz,'100%', f))
        shutil.copy(plotz,writedir)
#        os.system("cp %s/design.png files/%s.design.png"%(file, file.replace("/","_")))
#        os.system("cp %s/design_cov.png files/%s.design_cov.png"%(file, file.replace("/","_")))
#        os.system("cp %s/mc/disp.png files/%s.disp.png"%(file, file.replace("/","_")))
#        os.system("cp %s/mc/trans.png files/%s.trans.png"%(file, file.replace("/", "_")))
#        os.system("cp %s/reg/example_func2standard.png files/%s.example_func2standard.png"%(file,  file.replace("/","_")))
#        os.system("cp %s/reg/example_func2highres.png files/%s.example_func2highres.png"%(file, file.replace("/","_")))
#        os.system("cp %s/reg/highres2standard.png files/%s.highres2standard.png"%(file, file.replace("/","_")))
#        if len(glob.glob(os.path.join(file,'stats','cope*.nii.gz')))==2:
#            print(file+' has 2 cope files :D')
#        else:
#            print(file+' is missing copes, need to rerun')
#            shutil.rmtree(file)
#    f.close()

def main():
    basedir='/Users/gracer/Desktop/data/derivatives/task'
    writedir='/Users/gracer/Desktop/data/files'
    try:
        os.makedirs(os.path.join(writedir))
        outfile = os.path.join(writedir,'lev1_QA.html')
        f = open(outfile, "w")
    except OSError:
        os.remove(outfile)
        shutil.rmtree(os.path.join(writedir))
        
    QA_writer(basedir,f,writedir)
main()

os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts')