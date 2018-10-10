from commands import getoutput as go
from glob import glob
# print go('ls')

srcdir = '/Users/andrewkim/Documents/AA_TXM/mov/1_Cu_orig/'
dstdir = '/Users/andrewkim/Documents/AA_TXM/mov/1_Cu/'

srcs = sorted(glob(srcdir+'*.jpg'))

for src in srcs:
    suffix = src.split('/')[-1]
    nsuffix = suffix.replace('A','A_crop_')
    dest = src.replace('1_Cu_orig','1_Cu').replace(suffix,nsuffix)

    try:
        fo = open(dest,'r')
        print 'file exist'
    except:
        cmd = 'ffmpeg -i ' + src +' -vf "crop=1200:1200:424:214" ' + dest
        go(cmd)