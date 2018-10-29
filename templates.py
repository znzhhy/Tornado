import time
import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run port', type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.render('in_out.html')   # 路由跳转

    def post(self, *args, **kwargs):
        name = self.get_argument('name', 'no')
        self.render('in_out2.html',
                    username=name
                    )


application = tornado.web.Application(
    handlers=[
        (r"/main", IndexHandler),

    ],
    template_path="templates",  # 配置html文件路径i
    debug=True, # 调试模式
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



