import os

headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) '
                  'Version/11.0 Mobile/15A372 Safari/604.1',
    'authorization': '',
    'content-type': 'application/json;charset=UTF-8',
}
# 登录 post
login_url = 'https://rymcu.com/api/auth/login'
# 每日一题 get
today_url = 'https://rymcu.com/api/answer/today'
# 查询答案 get
show_answer_url = 'http://1.116.175.112:8089/question/show-answer/%s'
# 答题 post
answer_url = 'https://rymcu.com/api/answer/answer'
account = os.environ['account']
pw = os.environ['pw']
