import time
import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run port', type=int)

class HeadHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('set_header')
        self.set_header('aaa', '111')
        self.set_header('bbb', '222')
        self.set_header('bbb', '333')

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('add_header')
        self.add_header('ccc', '444')
        self.add_header('ccc', '444')
        self.clear_header('ccc')

class SendHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('send_header')
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        # self.write('status_code: %s ' % status_code)
        self.write('你的页面走丢了~')
        # self.render()

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('send_header')
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        self.write('你的页面走丢了~')

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print (' ---set_default_headers---: 设置好默认的响应投头')

    def initialize(self):
        print('---initialize--: 初始化')

    def prepare(self):
        self.write('---prepare---: 准备工作')

    def get(self):
        self.write('---get--: 处理get请求')

    def post(self):
        self.write('---post--: 处理post请求')

    def write_error(self, status_code, **kwargs):
        print('---write--error: 处理错误')

    def on_finish(self):
        print('---on_finish--: 结束，释放资源')


application = tornado.web.Application(
    handlers=[
        (r"/main", HeadHandler),
        (r"/add", AddHandler),
        (r"/send", SendHandler),
        (r"/index", IndexHandler),
        (r"/.*", NotFoundHandler),  # 测试时候不写（只能写在最后一行）

        ],
    template_path="templates",  # 配置html文件路径i
    debug=True, # 调试模式
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
