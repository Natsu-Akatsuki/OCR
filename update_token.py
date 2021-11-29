import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK 参考@https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu，获取access token
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=<官网获取的A>&client_secret<官网获取的SK>'
AK = '...'
SK = '...'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + SK

response = requests.get(host)
if response:
    print(response.json()['access_token'])
    with open("token", "w") as fp:
        fp.write(response.json()['access_token'])
else:
    print("获取失败，相关原因为：" + response.json()["error_description"])
    print("please refer https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu for the problem")
