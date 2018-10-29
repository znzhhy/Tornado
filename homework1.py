import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8080, help='run port', type=int)

class TemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('in_out.html')  # 返回页面

class User_aHandler(tornado.web.RequestHandler):
    def get(self, name, age):
        self.write('name: %s <br> age: %s' % (name, age))

class User_bHandler(tornado.web.RequestHandler):
    def get(self, name, age):
        self.write('name: %s <br> age: %s' % (name, age))

class InoutHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_arguments('name')
        print(name)

    def post(self, *args, **kwargs):
        name = self.get_argument('name', 'no')
        pwd = self.get_argument('password', 'no')
        self.write('姓名是： %s， 密码是： %s' % (name, pwd))

        print(self.get_query_argument('next', 'no'))
        print(self.get_query_argument('name', 'no'))
        print(self.get_body_argument('next', 'no'))
        print(self.get_body_argument('name', 'no'))

application = tornado.web.Application(
    handlers=[
        (r"/tem", TemHandler),
        (r"/get", InoutHandler),
        (r"/user/(.+)/([0-9]+)", User_aHandler),  # 位置传参
        (r"/stu/(?P<age>[0-9]+)/(?P<name>.+)", User_bHandler), # 关键字传参
    ],
    template_path="templates",  # 配置html文件路径i
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()












