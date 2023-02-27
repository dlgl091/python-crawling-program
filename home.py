import requests
import aiohttp
import asyncio
import time
import settings as set
import pandas as pd
import asyncio_ver as asy
import requests_ver as req
import selenium_ver as sel
import os
import sys


while True:
    print("\n<<< 사이트 크롤링 시스템 >>>")
    print("-"*40)
    print("0. asyncio")
    print("1. requests")
    print("2. selenium")
    print("3. 크롤링 시스템 종료")
    print("-"*40)
    choi = input("수집 라이브러리를 선택해주세요 : ")

    if choi == "0":
        while True:
            try:
                os.system('cls')
                url, date_list = set.return_dateList()
                loop = asyncio.get_event_loop()
                start = time.time()
                result = loop.run_until_complete(asy.main(url+'{0}', date_list))
                end = time.time()
                result_csv = set.to_csv(date_list, result); print(result_csv)
                print(f"elapsed time = {end - start}s")
                os.system("pause")
                break
            except Exception as e:
                print(e, "오류")
                os.system("pause")
                os.system('cls')
                break
            finally:
                loop.close()
    elif choi == "1":
        while True:
            try:
            
                os.system('cls')
                url, date_list = set.return_dateList()
                start = time.time()
                result = req.get_request(url, date_list)
                end = time.time()
                result_csv = set.to_csv(date_list, result); print(result_csv)
                print(f"elapsed time = {end - start}s")
                os.system("pause")
                break
            except Exception as e:
                print(e, "오류")
                os.system("pause")
                os.system('cls')
                break
    elif choi == "2":
        while True:
            try:
                os.system('cls')
                url, date_list = set.return_dateList()
                start = time.time()
                result = sel.get_selenium(url, date_list)
                end = time.time()
                result_csv = set.to_csv(date_list, result); print(result_csv)
                print(f"elapsed time = {end - start}s")
                os.system("pause")
                break
            except Exception as e:
                print(e, "오류")
                os.system("pause")
                os.system('cls')
                break
    elif choi == "3":
            print("시스템을 종료합니다.")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
    else:
        print("잘못 선택했습니다. ")
        os.system("pause")
