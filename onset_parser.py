#!/usr/bin/python
#get onsets



import glob
import os
#import pdb
import pandas
import argparse

def ons_parse(basepath,args, arglist):
    os.chdir(basepath)
    print arglist['COLS']
    for item in arglist['COLS']:
        for ons_file in glob.glob('sub-*/func/sub-*bart_events.tsv'):
            print("starting %s"%ons_file)
            sub=ons_file.split('/')[0]
            if os.path.exists(os.path.join(basepath, sub, 'func','onsets'))==False:
                os.makedirs(os.path.join(basepath, sub, 'func','onsets'))
            x=pandas.read_csv(ons_file, sep='\t')
            use=x[['onset','duration','%s'%item]]
            print(use[item].dtype)
#            pdb.set_trace()  
            if use[item].dtype == 'float64' or use[item].dtype == 'int64':
                print("this looks like a number, lets demean it")
                meanie=use[item].mean()
                use[item]=use[item] - meanie
            else:
                print("this looks categorical, let's change it to 0s and 1s")
                use[item] = pandas.get_dummies(use[item])
            print(use)
            use.to_csv(os.path.join(basepath,sub,'func','onsets','%s_%s_output.csv'%(sub,item)), index=False, header=False)
        
#            pdb.set_trace()        


def main():
    basepath='/Users/gracer/Desktop/data'
#    writedir='/Users/gracer/Desktop/trash'
    

    parser=argparse.ArgumentParser(description='onset parser, expecting a tsv file')
    parser.add_argument('-cols',dest='COLS',nargs='+',
                        default=False, help='which columns do you want? Each file will contain the onset, duration, and the column of choice. You can list multiple columns')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    ons_parse(basepath, args, arglist)    
main()

    
    


