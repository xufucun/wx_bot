import itchat
import requests

TU_LING_URL = 'http://www.tuling123.com/openapi/api'
TU_LING_KEY = 'ad5fe83373d34331b07902baf4de9f2f'

# 微信 用户名 加密


# 请求数据
def request_msg(uid,  msg):

    data = {
        'key': TU_LING_KEY,
        'info': msg,
        'userid': uid
    }

    try:
        result = requests.post(TU_LING_URL, data=data).json()
        result_code = result.get('code')
        result_text = result.get('text')
        print(result_code)
        print(result_text)
        return result_text
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def register_text(msg):
    print(msg.fromUserName, msg.content)
    return request_msg(msg.fromUserName, msg.content)


@itchat.msg_register(itchat.content.MAP)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.CARD)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.NOTE)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.SHARING)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.PICTURE)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.RECORDING)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.VOICE)
def register_text(msg):
    print(msg.type)
    return ('我正在学习语音消息')


@itchat.msg_register(itchat.content.VIDEO)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.FRIENDS)
def register_text(msg):
    print(msg.type)


@itchat.msg_register(itchat.content.SYSTEM)
def register_text(msg):
    print(msg.type)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True, hotReload=True)
    itchat.run()
