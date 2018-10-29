import time
import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run port', type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello word!')   # 字符串
        self.write('<br>')
        self.write(b'<nancheng<br>>')   # 二进制
        self.flush()
        user = {
            'name' : 'nancheng',
            'age' : 18,
            'li' : [1,2,3,4]
        }
        self.write(user)    # 字典

        # li = [1,2,3,4]
        # self.write(li)
        self.finish()   # 请求结束

class TemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('in_out.html')  # 返回页面

class RecHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.redirect('/tem')   # 路由跳转

class InoutHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name', 'no')
        self.write(name)
        name1 = self.get_arguments('name')
        print(name1)

    def post(self, *args, **kwargs):
        name = self.get_argument('name', 'no')
        passwd = self.get_argument('name', 'no')
        self.write('姓名是： %s， 密码是： %s' % (name,passwd))

        print(self.get_query_argument('next', 'no'))
        print(self.get_query_argument('name', 'no'))
        print(self.get_body_argument('next', 'no'))
        print(self.get_body_argument('name', 'no'))

class ReqHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.remote_ip)  # 获取客户端ip
        print(self.request.connection)
        print(self.request)

class UserHandler(tornado.web.RequestHandler):
    def get(self, name, age):
        self.write('name: %s <br> age: %s' % (name, age))

class StudentHandler(tornado.web.RequestHandler):
    def get(self, name, age):
        self.write('name: %s <br> age: %s' % (name, age))

application = tornado.web.Application(
    handlers=[
        (r"/main", MainHandler),
        (r"/tem", TemHandler),
        (r"/rec", RecHandler),
        (r"/req", ReqHandler),
        (r"/get", InoutHandler),
        (r"/user/(.+)/([0-9]+)", UserHandler),  # 位置传参
        (r"/stu/(?P<age>[0-9]+)/(?P<name>.+)", StudentHandler), # 关键字传参
    ],
    template_path="templates",  # 配置html文件路径i
    debug=True, # 调试模式
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



