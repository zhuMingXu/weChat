from wechatpy.client import WeChatClient
from wechatpy.session.redisstorage import RedisStorage
from redis import Redis


app_id = "wx32f4c041fd82d8cb" 
secret = "8fc8a6d2cbb63538ec8366e1bbda88e4"



redis_client = Redis.from_url('redis://127.0.0.1:6379/0')
session_interface = RedisStorage(
    redis_client,
    prefix="wechatpy"
)

client = WeChatClient(
    app_id,
    secret,
    session=session_interface
)

print client.access_token


res = client.media.upload("image", open("blue.jpg"))
print(type(res)) 
print(res)
