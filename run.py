
#-*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import geetest
import json



#定义处理类型
class IndexHandler(tornado.web.RequestHandler):
    #添加一个处理get请求方式的方法
    def get(self):
        #向响应中，添加数据
        challenge = self.get_argument("challenge")
        gt = self.get_argument("gt")
        referer = self.get_argument("referer")
        ans = geetest.crack(gt, challenge, referer)
        self.write(json.dumps(ans))


if __name__ == '__main__':
    #创建一个应用对象
    app = tornado.web.Application([(r'/',IndexHandler)])
    #绑定一个监听端口
    app.listen(8899)
    #启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()

