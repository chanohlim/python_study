'''
import threading
import time
def takeNap():
    for i in range(5):
        time.sleep(1)
        print('Wake up!')

def rep(*args):
    for i in args:
        time.sleep(1.3)
        print(i)

th1 = threading.Thread(target = rep, args = ['Cats','Dogs','Frogs'])
th2 = threading.Thread(target = takeNap)

th1.start()
th2.start()
'''

import requests, os, bs4, threading,time


os.chdir('/Users/chanlim/Desktop')
os.makedirs('xkcd', exist_ok = True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print(f'downloading page {urlNumber}')
        r = requests.get(f'http://xkcd.com/{urlNumber}')
        r.raise_for_status()

        soup = bs4.BeautifulSoup(r.text,features='html.parser')

        comicElem = soup.select('#comic > img')
        if comicElem == []:
            print('no comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print(f'Downloading image {comicUrl}')
            r = requests.get('https:'+comicUrl)
            r.raise_for_status()


            #이미지 저장
            imgFile = open(os.path.join('xkcd',f'_img{urlNumber}'+os.path.basename(comicUrl)),'wb')

            for chunk in r.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()

downloadThreads = []
s = time.time()
for i in range(0,2820, 94):
    thread = threading.Thread(target = downloadXkcd, args = (i, i+93))
    downloadThreads.append(thread)
    thread.start()

#대기하기
for dt in downloadThreads:
    dt.join() #리스트에 있는 모든 thread가 끝날때까지 기다려주는 code
end = time.time()
print(f'Done! It took {round(end-s,0)} seconds to download.')
