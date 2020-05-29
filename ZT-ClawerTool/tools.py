
file_path='E:\\station.txt'
f=open(file_path,'r',encoding='utf-8')
lines=f.readlines()
f.close()
all=''
for i in lines:
    all = all + i
areas = all.split('@')
length=len(areas)
station_name={}
for i in range(1,length):
    tmps = areas[i].split('|')
    station_name[tmps[1]] = tmps[2]
f1=open('E:\\ZT-ClawerTool\\station.txt','a+',encoding='utf-8')
for data in station_name:
    f1.write(data+' '+station_name[data]+'\n')
f1.close()