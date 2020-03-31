import requests,time,pymysql,warnings
from bs4 import BeautifulSoup

#数据入库
def mysql_insert(data):
    global conn
    try:
        with conn.cursor() as cursor:
            res = cursor.execute("insert into zp_position(name,pid,level,hide,state,update_time,create_time,delete_time) values(%s, %s, %s, %s, %s, %s, %s, %s)", data)
            conn.commit()
            print(data[0],'---------',u'入库成功')
    except Exception as e:
        print(u'入库错误', e)
        conn.rollback()

#爬取逻辑
def get():
    global url,headers
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    dls = BeautifulSoup(res.text, 'lxml').select('.job-menu')[0].select('dl')
    now = time.time()

    #半自动
    
    #第一层职位起始id(主键id从1自增)
    i = 1
    #第二层职位起始id(第一层职位个数+1)
    j = 20
    
    #按顺序入库
    
    #解析入库第一层职位
    for dl in dls:
        position1 = dl.select('.menu-article')[0].text.strip()
        mysql_insert((position1, 0, 1, 0, 1, now, now, 0))

    #解析入库第二层职位
    for dl in dls:
        dls2 = dl.select('.menu-sub ul')[0].select('li')
        for dl2 in dls2:
            position2 = dl2.select('h4')[0].text.strip()
            mysql_insert((position2, i, 2, 0, 1, now, now, 0))
        i = i + 1
            
    #解析入库第三层职位
    for dl in dls:
        dls2 = dl.select('.menu-sub ul')[0].select('li')
        for dl2 in dls2:
            dls3 = dl2.select('.text')[0].select('a')
            for dl3 in dls3:
                position3 = dl3.text.strip()
                mysql_insert((position3, j, 3, 0, 1, now, now, 0))
            j = j + 1

if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    #BOSS直聘网地址
    url = 'https://www.zhipin.com'

    #数据库配置
    host="127.0.0.1"
    user="root"
    password="root"
    database="boss"
    charset="utf8"

    #连接mysql数据库
    conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)

    #浏览器headers配置
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

    #开始爬取
    get()
