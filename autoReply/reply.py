# -*- coding: utf-8 -*-
from . import sensWordsFilter
from wechatpy.replies import create_reply
from wechatpy.replies import ImageReply




class AutoReply(object):
    

    def __init__(self):
        super(AutoReply,self).__init__()

    #reply text or pic
    def subscribeReply(self,msg,content=None,media_id=None):
        if content == None and media_id == None:
            raise Exception("no info be send!")
        elif content != None and media_id != None:
            raise Exception("content and media_id args only one != None")
        elif content != None:
            reply = create_reply(content, message=msg)
            xml = reply.render()
            return xml 
        else:
            reply = ImageReply(message=msg)
            reply.media_id = media_id
            xml = reply.render()
            return xml

    #default reply  text
    def defaultReply(self,msg,content):
        reply = create_reply(content, message=msg)
        xml = reply.render() 
        return xml


    
    def keywordsRules(self,msg):
        text = msg.content
        # only one @ 
        if len(text.split('@')) > 2:
            return -3
  
        #昵称长度检测     
        name = text.split('@')[1]
        if len(name) < 1 or len(name) > 10:
            return -1    
 
        #敏感词检测
        gfw = sensWordsFilter.DFAFilter()
        path = "/root/weChat/autoReply/gxSensWords.txt"
        gfw.parse(path)

        result = gfw.filter(name)
        if '*' in result:
            return -2

        #合法的name
        return name

    #keyword reply rules(msg,keyword)
    def keywordsReply(self,msg,content=None,media_id=None):
        ret = self.keywordsRules(msg)
        print("ret:",ret)
        if ret == -1:
            content = "新年歌词活动：\n昵称长度必须在1~10个字符之间。\n请重新输入\"新年歌词@昵称\"！"
            reply = create_reply(content, message=msg)
            xml = reply.render()
            return xml

        elif ret == -2:
            content = "新年歌词活动：\n昵称含有敏感词，请使用一个合法昵称。\n请重新输入\"新年歌词@昵称\"！"
            reply = create_reply(content, message=msg)
            xml = reply.render()
            return xml
 
        elif ret == -3:
            content = "新年歌词活动：\n昵称中不能含有@。\n请重新输入\"新年歌词@昵称\"！"
            reply = create_reply(content, message=msg)
            xml = reply.render()
            return xml
