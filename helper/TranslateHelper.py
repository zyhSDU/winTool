import hashlib
import http
import http.client
import json
import random
import urllib
import urllib.parse


def baidu_translate(app_id, secret_key, translate_text, flag=0):
    """
    :param translate_text: 待翻译的句子，len(q)<2000
    :param flag: 1:原句子翻译成英文；0:原句子翻译成中文
    :return: 返回翻译结果。
    For example:
    q=我今天好开心啊！
    result = {'from': 'zh', 'to': 'en', 'trans_result': [{'src': '我今天好开心啊！', 'dst': "I'm so happy today!"}]}
    """

    http_client = None
    my_url = '/api/trans/vip/translate'  # 通用翻译API HTTP地址
    from_lang = 'auto'  # 原文语种

    if flag:
        to_lang = 'en'  # 译文语种
    else:
        to_lang = 'zh'  # 译文语种

    salt = random.randint(3276, 65536)

    sign = app_id + translate_text + str(salt) + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    my_url = my_url + '?appid=' + app_id + '&q=' + urllib.parse.quote(translate_text) + '&from=' + from_lang + \
            '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign

    # 建立会话，返回结果
    try:
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
        http_client.request('GET', my_url)
        # response是HTTPResponse对象
        response = http_client.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        # return result
        return result['trans_result'][0]['dst']

    except Exception as e:
        print(e)
    finally:
        if http_client:
            http_client.close()


if __name__ == '__main__':
    # 手动录入翻译内容，q存放
    # q = raw_input("please input the word you want to translate:")
    q = "介绍一下整本书，比如是传主的人生，或者作者写这本书的特色。可参看目录、序言或简介等资料。"
    '''
    flag=1 输入的句子翻译成英文
    flag=0 输入的句子翻译成中文
    '''
    result = baidu_translate(
        app_id="20221023001410022",
        secret_key="zsXssn8xsnvdBBD0gZF7",
        translate_text=q,
        flag=1,
    )  # 百度翻译
    print("原句:" + q)
    print(result)
