import json
import requests
import os
import notify
"""
任务名称
name: lunastory签到
定时规则
cron: 10 8 * * *
"""
def signIn(cookie):
    url = "https://h5.youzan.com/wscump/checkin/checkinV2.json"
    params = {
      'checkinId': "3620022",
      'app_id': "wx8bb8f3ca1a378b9c",
      'kdt_id': "127790902"
    }
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 12; M2102K1AC Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 MMWEBID/7906 MicroMessenger/8.0.50.2701(0x2800325A) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
      'Cookie': cookie
    }
    response = requests.get(url, params=params, headers=headers).json()
    print(response)
    QLAPI.notify('lunastory签到', response)

def main():
    cookie = os.getenv("lunastory_cookie")
    signIn(cookie)

if __name__ == '__main__':
    main()