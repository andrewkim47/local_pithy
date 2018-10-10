from commands import getoutput as go


names = [
# 'AK1',
# 'AK2',    
# 'AK3',
# 'AK4',
# 'AK5',
# 'AK6',
# 'AK7',
# 'AK8'
# 'AK9',
# 'AK10',    
# 'AK11',
# 'AK12'
'AK14',
'AK15',    
'AK16',
'AK17'
]

for name in names:
    cmd = 'particle flash ' + name +' /Users/andrewkim/Downloads/firmware.bin'
    print go(cmd)
# 'particle flash AK8 /Users/andrewkim/Downloads/firmware.bin'