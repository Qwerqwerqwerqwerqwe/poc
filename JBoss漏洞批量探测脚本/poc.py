# -*- coding: utf-8 -*-
import argparse
import sys
import requests
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """

     ██╗██████╗  ██████╗ ███████╗███████╗
     ██║██╔══██╗██╔═══██╗██╔════╝██╔════╝
     ██║██████╔╝██║   ██║███████╗███████╗
██   ██║██╔══██╗██║   ██║╚════██║╚════██║
╚█████╔╝██████╔╝╚██████╔╝███████║███████║
 ╚════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                         
            tag:  this is a JBoss  poc                                       
            @version: 1.0.0   @author: bob           
"""
    print(test)


def poc(target):
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",

    }

    vuls = ['/jmx-console', '/web-console', '/invoker/JMXInvokerServlet', '/admin-console','/jbossmq-httpil/HTTPServerILServlet', '/invoker/readonly']
    for test in vuls:
        test = test.strip()
        url = target+test
        try:
            response = requests.get(url, headers=headers, verify=False, timeout=5)
            if response.status_code == 200:
                if "admin" in url:
                    print(f"[+]{target}admin-console vulnerability may exist!")
                    with open("admin-concle.txt","a+",encoding="utf-8") as f:
                        f.write(target+"\n")
                elif "JMXInvokerServlet" in url:
                    print(f"[+]{target}JBoss JMXInvokerServlet(CVE-2015-7501) vulnerability may exist!")
                    with open("JBoss JMXInvokerServlet(CVE-2015-7501.txt","a+",encoding="utf-8") as f:
                        f.write(target+"\n")
                elif "jbossmq" in url:
                    print(f"[+]{target}JBOSSMQ JMS(CVE-2017-7504) vulnerability may exist!")
                    with open("aJBOSSMQ JMS(CVE-2017-7504).txt","a+",encoding="utf-8") as f:
                        f.write(target+ "\n")
                else:
                    pass
            else:
                pass

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

        mp = Pool(20)  # 创建一个拥有20个线程的线程池
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()
