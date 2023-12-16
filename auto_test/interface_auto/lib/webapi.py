

import requests

class APIMgr:
    def __init__(self):
        self.session = requests.Session()

    def printResponse(self, response):
        print('\n\n------HTTP response * begin------')
        print(response.status_code)
        for key, value in response.headers.items():
            print(f'{key} : {value}')

        print('')

        # print(reponse.text)
        print(response.content.decode('utf-8'))
        print('------HTTP response * end------\n\n')

    def login(self, url="http://127.0.0.1/api/mgr/signin", username='byhy', password='88888888'):
        response = self.session.post(url,
                                 data={
                                     'username': username,
                                     'password': password
                                 })

        self.printResponse(response)
        return response

    def customer_list(self, url="http://127.0.0.1/api/mgr/customers", action='list_customer', pagesize=10, pagenum=1, keywords=''):
        response = self.session.get(url,
                                params={
                                    'action': 'list_customer',
                                    'pagesize': 10,
                                    'pagenum': 1,
                                    'keywords': '',
                                })

        self.printResponse(response)
        return response


if __name__ == '__main__':
    apimgr = APIMgr()
    apimgr.login()
    apimgr.customer_list()
