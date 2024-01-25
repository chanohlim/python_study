import os,shutil,random, re

try:
    os.mkdir('/Users/chanlim/Desktop/hello')
except:
    pass

a = random.randint(30,60)
e = random.randint(30,60)
for i in range(a):
    f = open(f'/Users/chanlim/Desktop/hello/{"{:02d}".format(random.randint(1,12))}-{"{:02d}".format(random.randint(1,30))}-{random.randint(1900,2023)}hi.txt','w')
    f.write('american date')
    f.close()

print(f'{a} files in american date')

for i in range(e):
    f = open(f'/Users/chanlim/Desktop/hello/{"{:02d}".format(random.randint(1,30))}-{"{:02d}".format(random.randint(1,12))}-{random.randint(1900,2023)}hi.txt','w')
    f.write('english date')
    f.close()

print(f'{e} files in euro date')

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$ 
                         """, re.VERBOSE)


amerfile_cnt = 0

for amerfile in os.listdir('/Users/chanlim/Desktop/hello'):
    mo = datePattern.search(amerfile)

    if mo == None:
        continue

    pre = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    suf = mo.group(8)

    euro = pre + day + '-' + month + '-' + year + suf

    absWorkingdir = os.path.abspath('/Users/chanlim/Desktop/hello')
    amerfilename = os.path.join(absWorkingdir,amerfile)
    eurofilename = os.path.join(absWorkingdir,euro)

    print(f'Renaming {amerfilename} to {eurofilename}...')
    shutil.move(amerfilename,eurofilename)

    amerfile_cnt += 1

print(f'{amerfile_cnt} files changed!')
