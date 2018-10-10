from commands import getoutput as go
from glob import glob
# print go('ls')

srcdir = '/Users/andrewkim/Documents/AA_TXM/mov/1_Cu_orig/'
dstdir = '/Users/andrewkim/Documents/AA_TXM/mov/1_Cu/'

srcs = sorted(glob(srcdir+'*.jpg'))

for src in srcs[0:1]:
    suffix = src.split('/')[-1]
    nsuffix = suffix.replace('A','A_crop_')
    
    dest = src.replace('1_Cu_orig','1_Cu').replace(suffix,nsuffix)
    
    # print dest

    cmd = 'ffmpeg -i ' + src +' -vf "crop=1200:1200:424:214" ' + dest
    
    print go(cmd)