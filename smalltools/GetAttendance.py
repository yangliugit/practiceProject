# -*- coding:utf-8 -*-
import requests
import json
from datetime import datetime
from urllib import urlencode
import socket


class GetAttendance(object):
    def __init__(self, username, password, month):
        self.__username = username
        self.__password = password
        self.month = month
        self._headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"}

    def get_cookies(self):
        data = {
            "authorization": "",
            "timeZone": "",
            "login_username": self.__username,
            "login_password": self.__password,
            "login_validatePwdStrength": 3,
            "random": "",
            "fontSize": 12,
            "screenWidth": 1920,
            "screenHeight": 1080
        }
        login_param = urlencode(data)
        login_url = "http://10.10.188.224:8080/seeyon/main.do?method=login"
        login_res = requests.post(login_url, login_param, headers=self._headers, allow_redirects=False)
        return login_res.cookies

    def get_attendance(self):
        data = {
            "managerMethod": "showHistoryList",
            "arguments": """[{"page":1,"size":200000},{}]"""
        }
        call_param = urlencode(data)
        attendance_url = "http://10.10.188.224:8080/seeyon/ajax.do?" \
                         "method=ajaxAction&managerName=historyManage&rnd=25731"
        attendance_res = requests.post(attendance_url, call_param, headers=self._headers, cookies=self.get_cookies())
        res_json = json.loads(attendance_res.text, encoding="utf-8")
        attendance_data = res_json["data"]
        time_record = []
        for time in attendance_data:
            time_record.append(time["sign_time"])
        return time_record

    def date_filter(self):
        time_record = self.get_attendance()
        date_list = [date[:19].encode('unicode-escape').decode('string_escape')
                     for date in time_record if date[:7] == self.month]
        date_map = {}
        date_sort = sorted(date_list)
        for date in date_sort:
            if date[:10] not in date_map.keys():
                date_map[date[:10]] = [date, date]
            else:
                date_map[date[:10]][1] = date

        return date_map

    def calc_data(self):
        all_overtime = 0
        billing_overtime = 0
        cb = 0
        dicta = self.date_filter()
        for data in sorted(dicta.items(), key=lambda x: x[0]):
            print data
        for key, value in dicta.items():
            is_week = datetime.strptime(key, "%Y-%m-%d").weekday()
            start_time = datetime.strptime(value[0], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(value[1], "%Y-%m-%d %H:%M:%S")
            nine_time = datetime.strptime(value[1][:10] + " 21:00:00", "%Y-%m-%d %H:%M:%S")
            eight_q = datetime.strptime(value[1][:10] + " 20:30:00", "%Y-%m-%d %H:%M:%S")
            if is_week > 4:
                all_overtime += (end_time - start_time).seconds
                billing_overtime += (end_time - start_time).seconds
            elif is_week <= 4 and end_time <= nine_time:
                if end_time != start_time:
                    all_overtime += (end_time - start_time).seconds - (9 * 3600)
                    if end_time >= eight_q:
                        billing_overtime += 0
                        cb += 40
                    else:
                        cb += 20
            elif is_week <= 4 and end_time > nine_time:
                if end_time != start_time:
                    cb += 40
                    all_overtime += ((end_time - start_time).seconds - (9 * 3600))
                    billing_overtime += (end_time - nine_time).seconds

        return all_overtime / 3600.0, billing_overtime / 3600.0, cb


def send_info(word):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1999))
    s.recv(1024).decode('utf-8')
    s.send(bytes(word))
    s.close()


if __name__ == '__main__':
    user = raw_input("\nPlease input your OA Username(For example: liuyang):\n")
    password = raw_input("Please input your OA Password:\n")
    user_info = [user, password]
    month = raw_input("Please input query month(For example: 2018-07):\n")
    print "\n\n*****Abnormal data have been removed from the statistical process, " \
          "The results are for reference only*****\n"

    try:
        geta = GetAttendance(user, password, month)
        calc = geta.calc_data()
        send_info(user_info)
        print "\n*****The following is statistic data *****"
        print " Work overtime hours: %s\n Billing overtime hours: %s\n Subside: %s" % calc

    except Exception as err:
        print "Exception info: %s" % str(err)
        print "Please check your input!!!"
    finally:
        raw_input("\nPress Enter to exit......")
