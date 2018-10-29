import time
import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run port', type=int)

class HeadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('in_out.html')
#
# class LandHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument('name', 'no')
        password = self.get_argument('password', 'no')
        self.render('in_out2.html', username= name)

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('send_header')
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        self.redirect('/tem')

class TemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('error_404.html')

application = tornado.web.Application(
    handlers=[
        (r"/main", HeadHandler),
        (r"/tem", TemHandler),
        (r"/.*", NotFoundHandler),  # 测试时候不写（只能写在最后一行）

        ],
    template_path="templates",  # 配置html文件路径i
    debug=True,
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
