#!/usr/bin/env python

import os
import glob
import argparse
import pdb
#output dir done
#input dirs done
#total number of inputs done
#threshold done
#cluster size done
#need to think of a way to automate the model generation
def create_fsf3(basedir,repl_dict, outdir, arglist):
    for item in arglist['COPE']:
        print item
        feats=glob.glob(os.path.join(basedir,'derivatives','task','sub-*','grace_edit','%s.gfeat'%arglist['TASK'],'cope%s.feat'%item))
        inputdir=len(feats)
        repl_dict.update({'INPUTDIR':inputdir})
#        cope='cope'+str(item)
        output=os.path.join(basedir,'derivatives','task','sub-*','%s_%s.gfeat'%(arglist['TASK'],item))
        repl_dict.update({'OUTPUT':output})
        i=0
        
        with open(os.path.join(basedir,'level3_test.fsf'),'r') as infile:
                data=infile.readlines()
                
        for sub in glob.glob(os.path.join(basedir,'derivatives','task','sub-*','grace_edit','%s.gfeat'%arglist['TASK'],'cope%s.feat'%item)):
            i=i+1
            data[272+i]=('set feat_files(%i) "%s"\n'%(i,sub))
            print(data[272+i])
            data[317+inputdir+i]=('set fmri(evg%i.1) 1'%(i))
            data[319+inputdir+i]=('set fmri(groupmem.%i) 1'%(i))
            
            with open(os.path.join(basedir,'new_level3_test.fsf'),'w') as tempfsf:
                tempfsf.writelines(data)
        tempfsf.close()
        print('test')
        pdb.set_trace()
            
        with open(os.path.join(basedir,'new_level3_test.fsf'),'r') as infile:
            tempfsf=infile.read()
            for key in repl_dict:
                tempfsf = tempfsf.replace(key, repl_dict[key])
                with open(os.path.join(outdir,'%s_cope%s.fsf'%(sub,item)),'w') as outfile:
                    outfile.write(tempfsf)
    if os.path.exists(os.path.join(basedir,'new_level3_test.fsf')):
        os.remove(os.path.join(basedir,'new_level3_test.fsf'))
#        for key in repl_dict:
#        tempfsf = tempfsf.replace(key, repl_dict[key])
#        with open(os.path.join(outdir,'%s_cope_%s.fsf'%(arglist['TASK'],arglist['COPE'])),'w') as outfile:
#        outfile.write(tempfsf)
#                tempfsf=infile.read()   
#                for key in repl_dict:
#                    tempfsf = tempfsf.replace(key, repl_dict[key])
#                    with open(os.path.join(outdir,'%s_cope%s.fsf'%(sub,item)),'w') as outfile:
#                        outfile.write(tempfsf)
#        
#        print("cool")
#        pdb.set_trace()
#	for x in range(1,29):
#		cope='cope'+str(x)
#		print(cope)
#		repl_dict.update({'COPE':cope})
#		print(repl_dict)
#		fsf_name=cope+'_risk_int.fsf'
#		name=fsf_name.strip('.fsf')
#		output=os.path.join(outdir,name)
#		repl_dict.update({'OUTPUT':output})
#		with open(os.path.join(script_path,'design3_risk_int.fsf'),'r') as infile:
#            	tempfsf=infile.read()
#            	for key in repl_dict:
#                    	tempfsf = tempfsf.replace(key, repl_dict[key])
#                    	with open(os.path.join(level3_path,fsf_name),'w') as outfile:
#                            	outfile.write(tempfsf)
#
#
def main():

    basedir='/Users/gracer/Desktop/data'
    outdir=os.path.join(basedir,'derivatives','task')
    parser=argparse.ArgumentParser(description='making fsf files')
    parser.add_argument('-noreg',dest='NOREG', action='store_true',
                        default=False, help='Did you already register your data (using ANTZ maybe)?')
    parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we using?')
    parser.add_argument('-copes',dest='COPE',nargs='+',
                        default=False, help='which copes are we using?')
    parser.add_argument('-thresh',dest='THRESH',nargs='+',
                        default='0.001', help='What p threshold do we want to use, we recommend p<0.001')
    parser.add_argument('-Z cluster',dest='CLUST',nargs='+',
                        default='3.1', help='What Z threshold do we want to use, we recommend 3.1')

    repl_dict={}
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    repl_dict.update({'THRESH':arglist['THRESH']})
    repl_dict.update({'CLUST':arglist['CLUST']})
#function called
    create_fsf3(basedir,repl_dict, outdir, arglist)

main()
