from datetime import datetime, date, timedelta
from re import match, sub
import pandas as pd
import requests

class refineInput:
    def __init__(self):
        self.rdate = ''
        self.inurl = ''
        self.infname = ''
        self.inputFilter_result = False
    def user_input_date(self): # input 받는 함수
        while True: # url 인풋
            target_url = input("url을 입력하세요 : ")
            if self.set_url(target_url):
                in_url = self.inurl
                break
            else:
                continue
        while True:
            start_date = input("시작 날짜를 입력하세요(YYYYmmdd 형식) : ")
            if self.set_date(start_date):
                in_sdate = self.rdate
                break
            else:
                continue
        while True:
            end_date = input("끝 날짜를 입력하세요(YYYYmmdd 형식) : ")
            if self.set_date(end_date):
                in_ndate = self.rdate
                break
            else:
                continue
        return in_url, in_sdate, in_ndate

    def file_name_input(self):
        while True:
            file_name = input("csv 파일의 이름을 입력하세요(확장자 빼고 이름만 입력) : ")
            if file_name != '':
                in_fname = file_name
                break
            else:
                continue
        return in_fname
        
    def set_date(self, date1): # 날짜 형식 필터링 함수
        try:
            if date1 != '':
                if bool(match(r'\d{8}', date1)):
                    date1 = date(int(date1[:4]), int(date1[4:6]), int(date1[6:]))
                    date1 = datetime.strftime(date1, '%Y-%m-%d')
                    self.rdate = date1
                    self.inputFilter_result = True
                elif bool(match(r'\d{4}-\d{2}-\d{2}', date1)):
                    date1 = date.fromisoformat(date1)
                    self.rdate = date1
                    self.inputFilter_result = True
                else:
                    self.inputFilter_result = False

            else:
                print("날짜 형식을 잘못 입력하셨습니다.\n")
        except:
            print("날짜 형식을 잘못 입력하셨습니다.\n")
            self.inputFilter_result = False
        finally:
            return self.inputFilter_result

    def set_url(self, url): # 유효한 url인지 확인
        try:
            page = requests.get(url)
            html = page.text
            self.inurl = url
            self.inputFilter_result = True
        except:
            print("url을 잘못 입력하셨습니다.\n")
        finally:
            return self.inputFilter_result


    def date_range(self, start, end): # 날짜 사이 모든 날짜 리스트로 구하는 함수
        try:
            start = datetime.strptime(start, "%Y-%m-%d")
            end = datetime.strptime(end, "%Y-%m-%d")
            dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
            return dates
        except:
            print("날짜 형식을 잘못 입력하셨습니다.\n")

def return_dateList():
    ref_obj = refineInput()
    in_url, start_date, end_date = ref_obj.user_input_date()
    date_list = ref_obj.date_range(start_date, end_date)
    return in_url, date_list


# 결과 dict -> df -> csv
def to_csv(date_list, result): # op은 csv 파일의 버전 숫자를 구분. aiohttp는 0, request는 1, selenium는 2
    response_dict = {}; response_content = []; response_status = []
    response_dict['날짜'] = date_list
    for one_date in result :
        response_content.append(one_date[0])
        response_status.append(one_date[1])
    response_dict['내용'] = response_content
    response_dict['status'] = response_status

    result_df = pd.DataFrame(response_dict)

    file_name = '{0}.csv'.format(refineInput().file_name_input())
    result_df.to_csv(file_name, index=False)
    print(file_name, "생성 완료!")
    return result_df