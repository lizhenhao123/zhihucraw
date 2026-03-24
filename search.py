# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import math
import traceback
cookies = {
    'SESSIONID': 'x8uNmNdvqVIRB6EYvf8UexyGucafoGNSUzkFn45Fhbi',
    'JOID': 'W18VAEsjlm5W4amhIykhcxCl6349b8AbIoDS9mxJ4QEeqtjiE_G7lTTmoKUjEgKzzgRv3RyW0VFVWuQzvq-wTgw=',
    'osd': 'UVodBkMpk2ZQ6aOkKy8peRWt7XY3asgdKorX_mpB6wQWrNDoFvm9nT7jqKMrGAe7yAxl2BSQ2VtQUuI7tKq4SAQ=',
    'q_c1': '615920fb27514813b8748cc11a70866f|1727078600000|1727078600000',
    '_zap': '5008dd52-48fe-4345-8882-ee30b2599c57',
    'd_c0': 'AACS8UZX2xmPTr7F6noy2NP2-BTrex21P-4=|1736996449',
    '_xsrf': 'ktw3D0lBdl3aWQ77MVqOed7RqQTYe7ut',
    'z_c0': '2|1:0|10:1760948275|4:z_c0|92:Mi4xZnM4aUdnQUFBQUFBQUpMeFJsZmJHU1lBQUFCZ0FsVk5ud25mYVFBRml0eXd1blRibThXTm9QeDdOQ3ZtbS1HNWhn|cb5e47cbee77e265ffa6fbf32f35ef3dec2bff9c4208654d2823f79039da0894',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1760951503',
    'SESSIONID': 'BQvwhuPLcyhKHxM7QYxb94pDWdEYpKh3tm3ImVxMror',
    'JOID': 'VlASA0xy8PL5qbSKNXZP5bPt-F0hPK6DicLN1X4ShZW15s_LDczRCZWmt4I1740uuEQf7uTOULYvuonQPGYsuWY=',
    'osd': 'Ul8cBEl2__z-rLCFO3FK4bzj_1glM6CEjMbC23kXgZq74crPAsLWDJGpuYUw64Igv0Eb4erJVbIgtI7VOGkivmM=',
    '__zse_ck': '004_ubue2iVhDWhBd3DSgLBmbO8E4ICLCXtKSFQercQO6oDnyQFawUbuiY1oOPT6MBywLbCfzlCV80HtuN7AxNxSLm3a/OKAFDhuaUwLt52OGKWDQXh=HWNzrtYZpGgATvc0-JkU2er2kKFQiW3T1gRILBhet7CKYijdo0z54Nu+SVZfNxzyKHPiCfd7ObZZM+OcHMjhtMEfntwmQbJ21qXQ9pb6yW0/USUM8WJf8E5jSZ1KShJa8CsAB8HbIbHVn4tv/',
    'edu_user_uuid': 'edu-v1|bf61a055-241d-415f-b5c0-14918d9e6a2d',
    'BEC': '244e292b1eefcef20c9b81b1d9777823',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.zhihu.com/search?q=%E9%AB%98%E8%80%83&type=topic',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    # 'cookie': 'SESSIONID=x8uNmNdvqVIRB6EYvf8UexyGucafoGNSUzkFn45Fhbi; JOID=W18VAEsjlm5W4amhIykhcxCl6349b8AbIoDS9mxJ4QEeqtjiE_G7lTTmoKUjEgKzzgRv3RyW0VFVWuQzvq-wTgw=; osd=UVodBkMpk2ZQ6aOkKy8peRWt7XY3asgdKorX_mpB6wQWrNDoFvm9nT7jqKMrGAe7yAxl2BSQ2VtQUuI7tKq4SAQ=; q_c1=615920fb27514813b8748cc11a70866f|1727078600000|1727078600000; _zap=5008dd52-48fe-4345-8882-ee30b2599c57; d_c0=AACS8UZX2xmPTr7F6noy2NP2-BTrex21P-4=|1736996449; _xsrf=ktw3D0lBdl3aWQ77MVqOed7RqQTYe7ut; z_c0=2|1:0|10:1760948275|4:z_c0|92:Mi4xZnM4aUdnQUFBQUFBQUpMeFJsZmJHU1lBQUFCZ0FsVk5ud25mYVFBRml0eXd1blRibThXTm9QeDdOQ3ZtbS1HNWhn|cb5e47cbee77e265ffa6fbf32f35ef3dec2bff9c4208654d2823f79039da0894; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1760951503; SESSIONID=BQvwhuPLcyhKHxM7QYxb94pDWdEYpKh3tm3ImVxMror; JOID=VlASA0xy8PL5qbSKNXZP5bPt-F0hPK6DicLN1X4ShZW15s_LDczRCZWmt4I1740uuEQf7uTOULYvuonQPGYsuWY=; osd=Ul8cBEl2__z-rLCFO3FK4bzj_1glM6CEjMbC23kXgZq74crPAsLWDJGpuYUw64Igv0Eb4erJVbIgtI7VOGkivmM=; __zse_ck=004_ubue2iVhDWhBd3DSgLBmbO8E4ICLCXtKSFQercQO6oDnyQFawUbuiY1oOPT6MBywLbCfzlCV80HtuN7AxNxSLm3a/OKAFDhuaUwLt52OGKWDQXh=HWNzrtYZpGgATvc0-JkU2er2kKFQiW3T1gRILBhet7CKYijdo0z54Nu+SVZfNxzyKHPiCfd7ObZZM+OcHMjhtMEfntwmQbJ21qXQ9pb6yW0/USUM8WJf8E5jSZ1KShJa8CsAB8HbIbHVn4tv/; edu_user_uuid=edu-v1|bf61a055-241d-415f-b5c0-14918d9e6a2d; BEC=244e292b1eefcef20c9b81b1d9777823',
}

#response = requests.get('https://www.zhihu.com/topic/19567664/hot', cookies=cookies, headers=headers)


def getComments(total,id):
    if total == 0:
        return
    totalpage = math.ceil(total/20)
    print('共多少页评论：'+str(totalpage))
    for index in range(2):
        print('评论第多少页：'+str(index))
        offset = index*20
        params = {
            'order_by': 'score',
            'limit': '20',
            'offset': str(offset),
        }
        time.sleep(0.5)
        response = requests.get(
            'https://www.zhihu.com/api/v4/comment_v5/answers/'+str(id)+'/root_comment',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        datalist = response.json().get('data')
        print(len(datalist))
        for citem in datalist:
            com_dict = {
                '昵称':citem.get('author').get('name'),
                '性别':citem.get('author').get('gender'),
                '回答id':id,
                '评论id':citem.get('reply_root_comment_id'),
                '内容':BeautifulSoup(citem.get('content'), 'html.parser').text,
                '发布时间':citem.get('created_time'),
                '点赞':citem.get('like_count')
            }
            comment_list.append(com_dict)
insert_list = []
comment_list = []
try:
    for i in range(100):
        print('第几页：'+str(i))
        start = i * 20
        time.sleep(0.5)
        response = requests.get(
            #时间排序 'https://www.zhihu.com/api/v5.1/topics/19553176/feeds/timeline_activity/v2?offset='+str(start)+'&limit=20&',
            # 热门排序
            'https://www.zhihu.com/api/v5.1/topics/19567664/feeds/essence/v2?offset='+str(start)+'&limit=20&',
            cookies=cookies,
            headers=headers,
        )
        datalist = response.json().get('data')
        print(len(datalist))
        for item in datalist:
            citem = item.get('target')
            print(citem.get('content'))
            content = ''
            if citem.get('content'):
                content = BeautifulSoup(citem.get('content'), 'html.parser').text
            if citem['type'] == 'zvideo':
                continue
            temp_dict = {
                '昵称':citem.get('author').get('name'),
                '性别': citem.get('author').get('gender'),
                '回答id':citem.get('id'),
                '内容':content,
                '发布时间':citem.get('updated_time'),
                '点赞':citem.get('voteup_count'),
                '收藏':citem.get('favlists_count'),
                '评论数':citem.get('comment_count'),
                'url':citem.get('url'),
            }
            insert_list.append(temp_dict)
            getComments(citem.get('comment_count'), citem.get('id'))
except:
    traceback.print_exc()
df = pd.DataFrame(insert_list)
df.to_excel('data.xlsx', index=False, engine='xlsxwriter')
df = pd.DataFrame(comment_list)
df.to_excel('comment.xlsx', index=False, engine='xlsxwriter')