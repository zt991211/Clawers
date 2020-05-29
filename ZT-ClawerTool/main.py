import requests
import bs4
import json
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) A'
                  'ppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
}


def GT_clawer():
    station_name = {}
    name_station = {}
    f = open('station.txt', encoding='utf-8')
    lines = f.readlines()
    f.close()
    for i in lines:
        temps = i.split(' ')
        station_name[temps[0]] = temps[1][:-1]
        name_station[temps[1][:-1]] = temps[0]
    while True:
        #print('车票查询业务开始。。。。。。')
        info1 = input('请输入出发站和终点站(格式为:广汉|成都),中间无空格: ')
        fromName = info1.strip().split('|')[0]
        toName = info1.strip().split('|')[1]
        startDate = input('请输入查询日期,不早于当前日期(格式为:2020-05-29): ')
        if fromName not in station_name:
            print('当前系统无此出发站')
            continue
        if toName not in station_name:
            print('当前系统无此终点站')
            continue
        url = 'https://i.meituan.com/uts/train/train/querytripnew?fromPC=1' \
              '&train_source=meituanpc@wap&uuid=a2bab8b38b364d7f8d7a.1590661315.1.0.0' \
              '&from_station_telecode={}&to_station_telecode={}&yupiaoThreshold=0&start_date={}' \
              '&isStudentBuying=false'.format(station_name[fromName], station_name[toName], startDate)

        response = requests.get(url, headers=headers).json()
        for train in response['data']['trains']:
            print('车次号:'+train['full_train_code'] + '     出发时间:' + train['start_time'] + '     到达时间:' + train[
                'arrive_time'] + '     耗时:' +
                  train['run_time'] + '     出发站:' + train['from_station_name'] + '     终点站:' + train['to_station_name'])
            seats_info = ''
            for seats in train['seats']:
                seats_info += str(seats['seat_type_name'])+'--'
                seats_info += str(seats['seat_min_price'])+'元--'
                seats_info += str(seats['seat_yupiao'])
                seats_info += '张      '
            print('票价信息:   ' + seats_info+'\n')
        print('所有车票信息打印完毕')
        print('如果想要继续查询, 请按y键, 否则按n键')
        order = input()
        if order == 'y':
            continue
        if order == 'n':
            print('你已经退出查询服务。。。。。。')
            break


def main_meau():
    print('|*----指令列表----*|')
    print('获取指令列表----h')
    print('查询火车票----g')
    print('退出系统----q')


print('Welcome to ZT-ClawerTools!')
print('开发者: SCU-ZT')
print('完成时间: 2020-05-29')
print('功能: 爬取美团火车票信息')
print('目的: 疫情在家太无聊，写个小爬虫'+'\n')
main_meau()
while True:
    print('请输入指令, 按h可以获得指令列表: ')
    command = input()
    if command == 'h':
        main_meau()
    if command == 'q':
        break
    if command == 'g':
        GT_clawer()
print('Bye--Bye')
