import tornado.ioloop   # I/O事件循环
import tornado.web  # web服务
import tornado.httpserver   # 单线程的http服务
import tornado.options

from tornado.options import define, options

define('port', default=8000, help='run port', type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('in_out.html')  # 返回页面

# class TemplatesHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        user = self.get_argument('name', 'no')
        self.render('username_homework.html',
        username=user)

application = tornado.web.Application(
    handlers=[
        (r"/main", MainHandler),
        # (r"/tem",  TemplatesHandler),
    ],
    template_path="templates",  # 配置html文件路径
    debug=True, # 调试模式
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_sever = tornado.httpserver.HTTPServer(application)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



