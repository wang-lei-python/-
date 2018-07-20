# coding:utf8
from flask import Blueprint, current_app, make_response
from flask_wtf.csrf import generate_csrf

html = Blueprint('html', __name__)


# 提供静态的html的文件(index.html,register.html,login.html等等)
@html.route('/<re(r".*"):file_name>')
def get_html_file(file_name):
    '''提供html文件'''
    # 根据用户访问的路径指明的html文件名file_name
    if not file_name:
        # 表示用户访问的是index.html
        file_name = 'index.html'

    if file_name != 'favicon.ico':
        file_name = 'html/' + file_name

    # 使用wtf帮助我们生成csrf_token字符串,实际是body中设置csrf_token
    csrf_token = generate_csrf()

    # 为用户设置cookie,csrf_token相当于在cookie中设置csrf_token

    resp = make_response(current_app.send_static_file(file_name))
    resp.set_cookie('csrf_token', csrf_token)

    return resp
