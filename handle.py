import hashlib
import web
from wechatpy import parse_message
from wechatpy.replies import create_reply
from wechatpy.replies import ImageReply


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
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            xmlData = web.data()
            print "handle xmlData:",xmlData
            msg = parse_message(xmlData)
            reply = ImageReply(message=msg)
            reply.media_id = u'ZJVhlh0cg72wKvGERY2828Cgm2fgBu_dHoDpRV6n_j4Vovq9vPSFz-CVR-48nCqf'
            xmlReply = reply.render()
            return xmlReply


        except Exception, Argment:
            return Argment




