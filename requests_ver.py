import requests
import settings as set
import time


def get_request(url, date_list):
    result = []
    try:
        for i in date_list:
            url_1 = url + i
            response = requests.get(url_1)
            content = response.text
            response_status = response.status_code

            if int(i[8:]) == 1 :
                print(i[5:7] + "월 시작..")

            result.append((content, response_status))

        return result
    except requests.exceptions.Timeout as errd:
        print("Timeout Error : ", errd)
    
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting : ", errc)

    except requests.exceptions.HTTPError as errb:
        print("Http Error : ", errb)

    # Any Error except upper exception
    except requests.exceptions.RequestException as erra:
        print("AnyException : ", erra)
        
        
