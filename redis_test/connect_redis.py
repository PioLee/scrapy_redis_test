import redis


def connect_redis():
    conn = redis.Redis(host="127.0.0.1", port=6379)
    # set类型 按照这个格式来存数据的
    for i in range(1, 101):
        conn.lpush('tests:start_urls',
                   'https://item.taobao.com/item.htm?spm=a217f.8051907.312171.33.2df233088ZDEBU&id=561043847738')
    # print(conn.smembers('test:start_urls'))  # 存储数据类型
    print("存储完毕")
    conn.close()


connect_redis()
