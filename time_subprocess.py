#Python 3.11.7 이하로만 지원
import time,sys,datetime,os

'''
print('Press Enter Key to begin.(Cmd + C to End)')
input()

def stopWatch(start,end):
    elapsed = round(end-start,2)
    return elapsed


startTime = time.time()
lastlap = startTime
lapcnt = 1


try:
    while True:
        input()
        laptime = time.time()
        print(f'lap {lapcnt}: {stopWatch(lastlap, laptime)}s, Total Elapsed: {stopWatch(startTime, laptime)}s')
        lastlap = laptime
        lapcnt += 1
except KeyboardInterrupt:
    print('Super Stopwatch program finished.')
'''  

'''
sys.set_int_max_str_digits(10000000)

def calcprod():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

start = time.time()
prod = calcprod()
end = time.time()

print(prod)
print(end - start,'초 경과')
'''

'''
for i in range(10):
    print(datetime.datetime.fromtimestamp(round(time.time(),0)))
    time.sleep(1)
'''

'''
delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
print(delta.days,delta.seconds)
print(delta.total_seconds())
print(delta)
'''

'''
birthday = input('생일을 입력해주세요 (예: 2015-07-23): ')
y,m,d = map(int,birthday.split('-'))

now = datetime.datetime.now()

if now.month > m:
    bd = datetime.datetime(year=now.year+1,month=m,day=d)
elif m == now.month:
    if d < now.day:
        bd = datetime.datetime(year=now.year+1,month=m,day=d)
    else:
        bd = datetime.datetime(year=now.year,month=m,day=d)
else:
    bd = datetime.datetime(year=now.year,month=m,day=d)

real_bd = datetime.datetime(year=y,month=m,day=d)

if not (bd-now).days+1:
    print('생일 축하드려요!')
elif bd > now:
    print((bd-now).days+1,'일 남음')

else:
    print((now-bd).days,'일 남음')

print(f'태어나신지 {(now-real_bd).days}일이 지났습니다!')
'''

'''
import subprocess

subprocess.Popen(['open', '/Applications/Microsoft Word.app'])

t = float(input('Enter wanted timer in secods: '))

def stopWatch(start,end):
    elapsed = round(end-start,2)
    return elapsed

start = time.time()
endTime = start+t

while time.time() < endTime:
    print(stopWatch(time.time(),endTime))
    time.sleep(0.05)
    os.system('clear')

subprocess.Popen(['open','/Users/chanlim/Desktop/ /code/python_study/automate_online-materials/alarm.wav'])
print('timer done!')
'''