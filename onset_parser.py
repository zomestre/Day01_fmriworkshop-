#!/usr/bin/python
#get onsets


import numpy as np
import glob
import os
import pdb
import pandas
import argparse

def ons_parse(basepath,args, arglist,writedir):
    os.chdir(basepath)
    print arglist['COLS']
    pdb.set_trace()  
    for ons_file in glob.glob('sub-*/func/sub-*bart_events.tsv'):
        print("starting %s"%ons_file)
        sub=ons_file.split('/')[0]
        if os.path.exists(os.path.join(basepath, sub, 'func','onsets'))==False:
            os.makedirs(os.path.join(basepath, sub, 'func','onsets'))
        x=pandas.read_csv(ons_file, sep='\t')
#        header=x.columns.tolist()
        var=arglist['COLS']
#        print(var)
#        pdb.set_trace()
        use=x[['onset','duration','%s'%var]]
        print(use)
        pdb.set_trace()
#        a = np.array(header)
#        RT = [0, 1, 2]
#        RTcols=list(a[RT])
#        print(header)
        pdb.set_trace() 
        x.to_csv(os.path.join(writedir,'%s_%s_output.csv'%(sub,arglist['COLS'])), columns = use, index=False, header=False)
        
        pdb.set_trace()        


def main():
    basepath='/Users/gracer/Desktop/data'
    writedir='/Users/gracer/Desktop/trash'
    

    parser=argparse.ArgumentParser(description='onset parser, expecting a tsv file')
    parser.add_argument('-cols',dest='COLS',
                        default=False, help='which columns do you want? Each file will contain the onset, duration, and the column of choice. You can list multiple columns')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    ons_parse(basepath, args, arglist,writedir)    
main()

    
    


#%cd /Users/gracer/Google\ Drive/fMRI_workshop/scripts/
