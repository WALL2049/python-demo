#coding=gbk
import requests
import beautifultable

def get_ncov_info(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None




country = input('请输入要查询的国家：')
url = f'https://lab.isaaclin.cn//nCoV/api/area?latest=1&province={country}'
data = get_ncov_info(url)
if not data['results']:
    print('没有爬取到数据！')
else:
    currentConfirmedCount = data['results'][0]['currentConfirmedCount']
    confirmedCount = data['results'][0]['confirmedCount']
    curedCount = data['results'][0]['curedCount']
    deadCount = data['results'][0]['deadCount']
    table = beautifultable.BeautifulTable()
    table.column_headers = ['现存确诊人数', '总计确诊人数', '治愈人数', '死亡人数']
    table.append_row(currentConfirmedCount, confirmedCount, curedCount, deadCount)
    print(table)




