#!/usr/bin/python
#get onsets



import glob
import os
import pdb
import pandas
import argparse
  
def ons_parse(basepath,args, arglist):
    os.chdir(basepath)
    print arglist['COLS']
    for item in arglist['COLS']:
        for ons_file in glob.glob('sub-*/func/sub-*%s_events.tsv'%arglist['TASK']):
            print("starting %s"%ons_file)
            sub=ons_file.split('/')[0]
            if os.path.exists(os.path.join(basepath, sub, 'func','onsets'))==False:
                os.makedirs(os.path.join(basepath, sub, 'func','onsets'))
            x=pandas.read_csv(ons_file, sep='\t')
            use=x[['onset','duration','%s'%item]]
            print(use[item].dtype) 
            if use[item].dtype == 'float64' or use[item].dtype == 'int64':
                print("this looks like a number, lets demean it")
                meanie=use[item].mean()
                use[item]=use[item] - meanie
            else:
                print("this looks categorical, let's change it to 0s and 1s")
                use.iloc[:,2]=use.iloc[:,2].astype('category')
                varbs=use.iloc[:,2].unique()
                pdb.set_trace()
                for name in varbs:
                    save_name=os.path.join(basepath,sub,'func','onsets','%s_%s_%s_%s_output.txt'%(sub,arglist['TASK'],item,name))
                    print(save_name)
                    pdb.set_trace()
                    tosave=use.loc[use.iloc[:,2] == name]
                    pdb.set_trace()
                    def score_to_numeric(x):
                        if x== name:
                            return 1
                    tosave.iloc[:,2] = tosave.iloc[:,2].apply(score_to_numeric)
                    pdb.set_trace()
                    tosave.to_csv(save_name, sep=" " ,index=False, header=False)
                pdb.set_trace()
                use[item] = pandas.get_dummies(use[item])
                use.to_csv(os.path.join(basepath,sub,'func','onsets','%s_%s_%s_output.txt'%(sub,arglist['TASK'],item)), sep=" " ,index=False, header=False)
                
            print(use)
            use.to_csv(os.path.join(basepath,sub,'func','onsets','%s_%s_%s_output.txt'%(sub,arglist['TASK'],item)), sep=" " ,index=False, header=False)
               


def main():
    basepath='/Users/gracer/Desktop/data'
    

    parser=argparse.ArgumentParser(description='onset parser, expecting a tsv file')
    parser.add_argument('-task',dest='TASK',
                        default=False, help='which task would you like to parse?')
    parser.add_argument('-cols',dest='COLS',nargs='+',
                        default=False, help='which columns do you want? Each file will contain the onset, duration, and the column of choice. You can list multiple columns')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    ons_parse(basepath, args, arglist)    
main()

    
    


#%cd /Users/gracer/Google\ Drive/fMRI_workshop/scripts/