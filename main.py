import json

import requests
from setting import login_url, today_url, show_answer_url, answer_url, account, pw

headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'authorization': '',
    'content-type': 'application/json;charset=UTF-8',
}


def auto_answer():
    login_data = {"account": account, "password": pw}
    user = requests.post(login_url, headers=headers, data=json.dumps(login_data)).json()
    if user['code'] == 0:
        headers['authorization'] = user['data']['user']['token']
        today = requests.get(today_url, headers=headers).json()
        if today['code'] == 0:
            answer_id = today['data']['answerRecords'][0]['id']
            print('今日试题：：%s' % today['data']['answerRecords'][0])
            answer = requests.get(show_answer_url % answer_id).json()
            if answer['success']:
                correct_answer = answer['data']['respData']
                print('正确答案：%s' % correct_answer)
                answer_content = {'idSubjectQuestion': answer_id, 'answer': correct_answer}
                print(requests.post(answer_url, headers=headers, data=json.dumps(answer_content)).json())


if __name__ == '__main__':
    auto_answer()