'''
用Python实现用户登录过程.
要求:注意安全的可能性注意权限验证的便捷性，使得其他地方也能使用考虑性能、可扩展性.
说明如何达到的注意选择的技术栈，说明为什么这样选择请将代码提交到任意GitHub，注意代码规范以及commit规范。上述4点，请在readme文件中进行说明。
'''
import time
import hashlib

user_info = {
        'user1': hashlib.sha256('password123'.encode()).hexdigest()
}

# session
session_stor = {}

def user_login(user,password):
    # password_hash
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # judge
    if user in user_info and user_info[user] ==password_hash:
        # unie token
        token = user + '-' + int(time.time())
        session_stor[token] = user
        print('login success',token)
        return token
    else:
        print('user or password is error')
        # maybe need redirect
        return None
        
