import requests
import bs4
#登陆网址
url='https://github.com/login'
#创建Session对象
sess=requests.Session()
#初次登陆
re=sess.get(url)
soup=bs4.BeautifulSoup(re.content)
authenticity=soup.find_all('input')[1]['value']
#表单数据
data={'commit':'Sign in',
        'utf8':'✓',
        'authenticity_token':authenticity,
        'login':'wanshantian@gmail.com',
        'password':'ShannonT333' ,
        'webauthn-support':'unsupported'}
#post请求网址
url='https://github.com/session'
sess.post(url,data=data)
#验证
res=sess.get('https://github.com/WanshanTian?tab=stars')
soup=bs4.BeautifulSoup(res.content)
print(soup)
