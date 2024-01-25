import requests, json
import public_ip as ip
import socket

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)


IP = ip.get()


request_url = 'https://geolocation-db.com/jsonp/' + IP

response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result  = json.loads(result)
print(result)

key = 'd92f40b146ba352bb15629e8b744a81f'
lat = result['latitude']
lon = result['longitude']

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={key}'+str('&units={metric}')
r = requests.get(url)

weaterdata = json.loads(r.text)
print('현재 기온:'+str(round(weaterdata['current']['temp']-273.15,1))+'°C'+'\t체감 기온:', '체감 기온: '+str(round(weaterdata['current']['feels_like']-273.15,1))+'°C')


'''
1. ip 주소로 현재위치
2. api 호출
3. 정보 추출
'''