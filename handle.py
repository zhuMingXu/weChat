import hashlib
import web
from wechatpy import parse_message
from wechatpy.replies import create_reply
from wechatpy.replies import ImageReply
from autoReply.reply import AutoReply
from wechatpy.events import SubscribeEvent
from wechatpy.messages import TextMessage
#autoReply obj
autoReply = AutoReply()

replyText = {"subscribeText":"欢迎关注高校er++,这里是所有高校er的聚集地~~",\
             "defaultText":"高校er听不懂你在说什么~~"}

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello,world"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "mingxuzhu"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e

    def POST(self):
        try:
            xmlData = web.data()
            msg = parse_message(xmlData)
            print("receive msg:",msg)

            if isinstance(msg,SubscribeEvent):
               return autoReply.subscribeReply(msg,content=replyText['subscribeText'])
            elif isinstance(msg,TextMessage):
               text = msg.content#receive content
               if '@' in text:
                   keyWord = text.split('@')[0]
                   if keyWord == '新年歌词' or keyWord == '新年歌':
                       return autoReply.keywordsReply(msg)
                   else:
                       return autoReply.defaultReply(msg,content=replyText['defaultText'])
                
               return autoReply.defaultReply(msg,content=replyText['defaultText']) 
            else:
               return autoReply.defaultReply(msg,content=replyText['defaultText']) 
            

        except Exception as e:
            return e


