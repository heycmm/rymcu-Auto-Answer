import os

headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) '
                  'Version/11.0 Mobile/15A372 Safari/604.1',
    'authorization': '',
    'content-type': 'application/json;charset=UTF-8',
}
# 登录 post
login_url = os.environ['login_url']
# 每日一题 get
today_url = os.environ['today_url']
# 查询答案 get
show_answer_url = os.environ['show_answer_url']
# 答题 post
answer_url = os.environ['answer_url']
account = os.environ['account']
pw = os.environ['pw']
