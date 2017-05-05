import uuid
import os

if not os.path.exists('F:/mima'):
    os.mkdir('F:/mima')
# 保存在相应密码文件夹里
f = open("F:/mima/1.txt","w+")
#accounts参数标准为 软件名+昵称
accounts = ['微博:123','微信:456','知乎:789']
#简单密码规则
def get_pwd(accounts):
    for account in accounts:
        pwd = uuid.uuid5(uuid.NAMESPACE_OID,account)
        pwd = str(pwd)[5:25].replace('-','')
        print(account,'密码:%s'%pwd)
        f.write(account+pwd+'\n')

get_pwd(accounts)

