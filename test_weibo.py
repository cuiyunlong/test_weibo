import  urllib.parse
import   urllib.request

login_url='https://passport.weibo.cn/sso/login'
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data=urllib.parse.urlencode([
     ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')

])



headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Referer':'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'}
req=urllib.request.Request(login_url,login_data.encode('utf-8'),headers=headers)
#req.add_header('User-Agent','User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
#req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
reponse=urllib.request.urlopen(req)
print('Data',reponse.read().decode('utf-8'))
