import os
import glob
import shutil

path_to_fake_files = "/opt/zapret/files/fake/"
path_to_ipset_hostlist = "/opt/zapret/ipset/"



def processer(x):
    filename=os.path.basename(files[x]).replace(".bat","")
    print(filename)
    with open(files[x],'r') as f:
        content=f.readlines()
        del content[0:15]
        conc="".join(content).replace("\n","").replace("%GameFilter%","0").replace("^","").replace("%BIN%",path_to_fake_files).replace("%LISTS%",path_to_ipset_hostlist)
        new_file="config"+filename
        with open("config.blank","r") as fr, open(new_file,"w") as fw:
            for line in fr:
                fw.write(line.replace('NFQWS_OPT=""','NFQWS_OPT="'+conc+'"\n'))

path = os.getcwd()+'/*.bat'
files = glob.glob(path)

if(len(files)>1):
    print('Больше одного файла...')
    print('Обработка по очереди')
    count = len(files)
    for file_index in range(0,count):
        processer(file_index)
    exit

else:
    print('Один файл.')
    processer(0)
    exit
