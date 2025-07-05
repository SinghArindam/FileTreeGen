import os
from pathlib import Path
from datetime import datetime

def list_files(startpath,dat):
    for root, dirs, files in os.walk(startpath):
        # print(f"root : {root}")
        # print(f"dirs : {dirs}")
        # print(f"files : {files}")
        level = root.replace(startpath, '').count(os.sep)
        indent = '*' * 4 * (level)
        dat+='{}{}/'.format(indent, os.path.basename(root))
        # print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '-' * 4 * (level + 1)
        for f in files:
            path_of_file = root+'\\'+f
            # path6 = os.path.join(dirs, f)
            # if os.path.isfile(f):
            # size = f.stat().st_size
            size_in_bytes = os.path.getsize(path_of_file)
            size_in_kilobytes = float(size_in_bytes/1024)
            size_in_kilobytes = round(size_in_kilobytes, 3)
            size_in_megabytes = float(size_in_kilobytes/1024)
            size_in_megabytes = round(size_in_megabytes, 3)
            size_in_gigabytes = float(size_in_megabytes/1024)
            size_in_gigabytes = round(size_in_gigabytes, 3)
            # print(type(size))
            # print(f"pal \t: \t{path_of_file} \t: \t({size_in_bytes} bytes)\t:\t({size_in_kilobytes} KB)\t:\t({size_in_megabytes} MB)\t:\t({size_in_gigabytes} GB)\t:\t")
            sz = f"\t: \t({size_in_bytes} bytes) = ({size_in_kilobytes} KB) = ({size_in_megabytes} MB) = ({size_in_gigabytes} GB)"
            dat+='{}{}{}\n'.format(subindent, f, sz)
            # print('{}{}'.format(subindent, f))
            # print('{}{}{}'.format(subindent, f, size))
    return dat

dat = '\t\t\t\t--Start--\n\n\n'
path = "C:\\Users\\hp\\Videos\\"
l = path.split('\\')
l[0] = l[0][0:1]
st=''
for ij in l:
    st+=str(ij)+'_'
st = st[:-2]

now = str(datetime.now())
stamp = now[:19:]
stamp = stamp.replace(':','_')
stamp = stamp.replace('-','_')
stamp = stamp.replace(' ','__')
stamp = str(stamp)


print(l,st)
dat = list_files(path,dat)
dat+='\n\t\t\t\t--DONE--\n'
# with open('files.txt','w+') as ff:
#     ff.write(dat)

ff = open(f'your_files_{st}_{stamp}.txt', 'w', encoding='utf-8')
ff.write(dat)
ff.close()

# print(dat)
input('--DONE--')
