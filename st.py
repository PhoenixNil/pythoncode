import requests
import json
import sqlite3
from prettytable import PrettyTable

requests.packages.urllib3.disable_warnings()


conn = sqlite3.connect('train.sqlite')
cur = conn.cursor()

chinese_startname = input('请输入起始车站名 :')
startcity = cur.execute(
    'SELECT name , abbreviation FROM stations WHERE name = ? ', (chinese_startname,))
startname_db = cur.fetchone()[1]

chinese_endname = input('请输入终点站名 :')
endcity = cur.execute(
    'SELECT name , abbreviation FROM stations WHERE name = ? ', (chinese_endname,))
endname_db = cur.fetchone()[1]


try:
    date = input("请输出日期：年-月-日 :")
    from_station = startname_db
    to_station = endname_db
except:
    date, from_station, to_station = '--', '--', '--'
    # 将城市名转换为城市代码

    # api url 构造
real_url = (
    'https://kyfw.12306.cn/otn/leftTicket/queryX?'
    'leftTicketDTO.train_date={}&'
    'leftTicketDTO.from_station={}&'
    'leftTicketDTO.to_station={}&'
    'purpose_codes=ADULT'
).format(date, from_station, to_station)
# print(real_url)
# c生成api
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-HK;q=0.6",
    "Cookie": "JSESSIONID=BE8E7B453D211BA1248F1D0CACB3CCD0; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerportal=3067347210.17695.0000; fp_ver=4.5.1; RAIL_EXPIRATION=1506451275438; RAIL_DEVICEID=ZXDJzqqcGx0vdtBVUgSdmxmWN-Gt5OV--sCu9ELbOBZo7OWyBhH5JGp5_z7UieQswwwi-qlGjvmopQ8VGfz-6Vy3Q21nErDAyAgum_5rBiUUt0zKvRJeA_q8Rc0rpXvANlpRGa7EvS9FdDRSACU_HtgYCknVG0aw; BIGipServerotn=1977155850.24610.0000; _jc_save_fromStation=%u957F%u6C99%u5357%2CCWQ; _jc_save_toStation=%u5317%u4EAC%u5317%2CVAP; _jc_save_fromDate=2017-09-26; _jc_save_toDate=2017-09-23; _jc_save_wfdc_flag=dc",
    "Host": "kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest",
    "Cache-Control": "no-cache",
}

r = requests.get(real_url, verify=False, headers=headers)
hg = r.json()
# print((hg['data']['result']))


def query_train_info(url):
    pt = PrettyTable()

    r = requests.get(url, verify=False, headers=headers)
    # 获取返回的json数据里的data字段的result结果
    raw_trains = r.json()['data']['result']

    for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[2]
        # 出发站
        from_station_code = data_list[4]
        # # 终点站
        to_station_code = data_list[7]
        # 出发时间
        start_time = data_list[8]
        # 到达时间
        arrive_time = data_list[9]
        # 总耗时
        time_fucked_up = data_list[10]
        # 一等座
        first_class_seat = data_list[31] or '--'
        # 二等座
        second_class_seat = data_list[30]or '--'
        # 软卧
        soft_sleep = data_list[23]or '--'
        # 硬卧
        hard_sleep = data_list[28]or '--'
        # 硬座
        hard_seat = data_list[29]or '--'
        # 无座
        no_seat = data_list[26]or '--'

        # 打印查询结果
        info = ['车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n 一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(
                train_no, chinese_startname, chinese_endname, start_time, arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat)]

        pt.add_row(info)

    return pt
# except:
    # return ' 输出信息有误，请重新输入'


train_query = query_train_info(real_url)

print(train_query)
