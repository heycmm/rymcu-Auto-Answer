import json

import requests
from setting import headers, login_url, today_url, show_answer_url, answer_url, account, pw
from requests.adapters import HTTPAdapter

r = requests.Session()
# 超时重试3次
r.mount('http://', HTTPAdapter(max_retries=3))
r.mount('https://', HTTPAdapter(max_retries=3))


def auto_answer():
    login_data = {"account": account, "password": pw}
    user = r.post(login_url, headers=headers, data=json.dumps(login_data)).json()
    if user['code'] == 0:
        headers['authorization'] = user['data']['token']
        today = r.get(today_url, headers=headers).json()
        if today['code'] == 0:
            answer_id = today['data']['answerRecords'][0]['id']
            print('今日试题：：%s' % today['data']['answerRecords'][0])
            answer = r.get(show_answer_url % answer_id).json()
            if answer['success']:
                correct_answer = answer['data']['respData']
                print('正确答案：%s' % correct_answer)
                answer_content = {'idSubjectQuestion': answer_id, 'answer': correct_answer}
                print(r.post(answer_url, headers=headers, data=json.dumps(answer_content)).json())


if __name__ == '__main__':
    auto_answer()
