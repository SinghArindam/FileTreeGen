import os
from datetime import datetime

def list_files(startpath,dat):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '*' * 4 * (level)
        dat+='{}{}/'.format(indent, os.path.basename(root))
        subindent = '-' * 4 * (level + 1)
        for f in files:
            # path to get file size
            path_of_file = root+'\\'+f
            # file size
            size_in_bytes = os.path.getsize(path_of_file)
            # size in different units
            size_in_kilobytes = float(size_in_bytes/1024)
            size_in_kilobytes = round(size_in_kilobytes, 3)
            size_in_megabytes = float(size_in_kilobytes/1024)
            size_in_megabytes = round(size_in_megabytes, 3)
            size_in_gigabytes = float(size_in_megabytes/1024)
            size_in_gigabytes = round(size_in_gigabytes, 3)
            # size variable to be added in data , gives size in different units
            sz = f"\t: \t({size_in_bytes} bytes) = ({size_in_kilobytes} KB) = ({size_in_megabytes} MB) = ({size_in_gigabytes} GB)"
            # appending in data 
            dat+='{}{}{}\n'.format(subindent, f, sz)
    return dat

# Path definition
path = os.getcwd()

# For filename add path address and timestamp
# path address
l = path.split('\\')
l[0] = l[0][0:1]
st=''
for ij in l:
    st+=str(ij)+'_'
st = st[:-2]
# timestamp
now = str(datetime.now())
stamp = now[:19:]
stamp = stamp.replace(':','_')
stamp = stamp.replace('-','_')
stamp = stamp.replace(' ','__')
stamp = str(stamp)

# Data of file to be written in the text file
dat = '\t\t\t\t--Start--\n\n\n'
dat = list_files(path,dat)
dat+='\n\t\t\t\t--DONE--\n'
# creating and writing in txt file
ff = open(f'your_files_{st}_{stamp}.txt', 'w', encoding='utf-8')
ff.write(dat)
ff.close()
# printing output
print(dat)
input('--DONE--')
