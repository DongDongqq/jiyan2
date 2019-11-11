# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 15:15
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : test.py
# @Software: PyCharm


import execjs
import json
import time
import requests
import random
from pprint import pprint
from geetest import crack


# def get_captcha():
#     url = 'https://www.tianyancha.com/verify/geetest.xhtml'
#     payload = {
#         'uuid': int(time.time() * 1000)
#     }
#     referer = 'https://www.tianyancha.com/vipintro/?jsid=SEM-360-PZ-SY-081001'
#     headers = {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json; charset=UTF-8',
#         'Referer': referer,
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
#         'X-Requested-With': 'XMLHttpRequest'
#     }
#     result = requests.post(url, data=json.dumps(payload), headers=headers).json()
#     if result['state'] == 'ok':
#         return result['data']['gt'], result['data']['challenge'], referer
#     else:
#         return None


def main():
    # while True:
    #     data = get_captcha()
    #     if data:
    #         break
    #     time.sleep(random.random())
    # result = crack(data[0], data[1], data[2])
    # print(result)
    referer = 'http://218.26.1.108/index.jspx'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://218.26.1.108',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    url = "http://218.26.1.108/registerValidate.jspx?t={}".format(int(time.time() * 1000))
    sess = requests.session()
    res = sess.get(url=url, headers=headers).json()
    print(res)
    result_tonado = 'http://127.0.0.1:8899/?challenge=%s&gt=%s&referer=%s' % (res["challenge"],res["gt"],referer)
    tona_res = requests.get(url=result_tonado)
    result = tona_res.json()
    # result = crack(gt=res["gt"],challenge=res["challenge"],referer=referer)
    # print(result)
    url = "http://218.26.1.108/validateSecond.jspx"
    data = {
        'searchText': "旅游公司",
        'geetest_challenge': result["challenge"],
        'geetest_validate': result["data"]["validate"],
        # 'geetest_validate':	validate,
        'geetest_seccode': '{}|jordan'.format(result["data"]["validate"])
    }
    res = sess.post(url=url, data=data, headers=headers).json()
    print(res['obj'])
    # res_url = 'http://218.26.1.108/' + res['obj'] + '&searchType=1&entName=旅游公司'
    # respone = sess.get(url=res_url, headers=headers)
    # print(respone.text)


if __name__ == '__main__':
    main()
