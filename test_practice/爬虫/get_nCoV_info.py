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




country = input('������Ҫ��ѯ�Ĺ��ң�')
url = f'https://lab.isaaclin.cn//nCoV/api/area?latest=1&province={country}'
data = get_ncov_info(url)
if not data['results']:
    print('û����ȡ�����ݣ�')
else:
    currentConfirmedCount = data['results'][0]['currentConfirmedCount']
    confirmedCount = data['results'][0]['confirmedCount']
    curedCount = data['results'][0]['curedCount']
    deadCount = data['results'][0]['deadCount']
    table = beautifultable.BeautifulTable()
    table.column_headers = ['�ִ�ȷ������', '�ܼ�ȷ������', '��������', '��������']
    table.append_row(currentConfirmedCount, confirmedCount, curedCount, deadCount)
    print(table)




