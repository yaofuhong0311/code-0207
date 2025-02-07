'''
用Python实现用户登录过程.
要求:注意安全的可能性注意权限验证的便捷性，使得其他地方也能使用考虑性能、可扩展性.
'''
import time
import hashlib
import os

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
        
