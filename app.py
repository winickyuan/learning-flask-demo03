
from flask import Flask, render_template #使用render_template渲染页面，并在路由中返回指定的页面,页面放在templates文件夹里

app = Flask(__name__)



@app.route('/') #装饰器
def hello_world():
    return render_template("index.html")


@app.route('/blog/<blog_id>') #装饰器
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="知了")


@app.route('/static') #测试使用css，在static中准备文件夹css，以及里面创建css文件, 尝试加载css和js文件
def static_demo():
    return render_template("static.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) # host=192.168.31.228)
