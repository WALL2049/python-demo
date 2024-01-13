# coding=utf-8
import requests
import urllib3
import rsa
import base64
import json
import logging
import re
import time

urllib3.disable_warnings()

UME_API_MAP = {
    'getUmePublicKey': 'api/oauth2/v1/login/publickey',
    'loginByRsa': 'api/oauth2/v1/login_rsa',
    'getAccessToken': 'api/oauth2/v1/usercred/access_token',
    'logout': 'api/oauth2/v1/logout',
    'queryEnodeb': 'api/randps/v1/ManagedElementType/ITBBU/moquery',
    'createStaneTraceTask': '/api/sta-subscriber/v1/neTrace/create',
    'deleteStaneTraceTask': '/api/sta-subscriber/v1/traceTask/ranume-sta-ne-trace/',
    'querygnbalias': '/api/res/v1/ranmes?nbiId='
}

#UME_ip = '10.230.40.199'

class Ume:
    def __init__(self,ip,port=28001,username='admin',pwd='Zenap_123!@#'):
        self.ip = ip
        self.port = port
        self.username = username
        self.pwd = pwd
        self.baseApiUrl = "https://%s:%s/" % (ip, port)
        self._login_token = "df421cd0874839755a89635e6d08eafb"
        self._header = {"Content-Type": "application/json"}
        self._cookie = ""
        self._access_token = ""

    def ip(self):
        return self.ip

    def __get_api_url(self,apiName):
        return self.baseApiUrl + UME_API_MAP[apiName]

    @staticmethod
    def _encrypt_password(password, public_key):
        rsa_public_key = rsa.PublicKey.load_pkcs1_openssl_pem(
            "-----BEGIN PUBLIC KEY-----\n" + public_key + "\n-----END PUBLIC KEY-----")
        encrypted_pwd = rsa.encrypt(password.encode(), rsa_public_key)
        return base64.b64encode(encrypted_pwd).decode()

    def update_header(self):
        public_key_result = requests.request('GET', self.__get_api_url('getUmePublicKey'), headers=self._header,
                                             verify=False)
        public_key = json.loads(public_key_result.text).get("rsaPublicKey")
        password = self._encrypt_password(self.pwd, public_key)
        cookie = 'Z-LOGIN-PUBLIC-CODE-%s=%s' % (
            self.port, public_key_result.cookies.get("Z-LOGIN-PUBLIC-CODE-%s" % self.port))
        login_body = {
            "isEncypted": "true",
            "username": self.username,
            "password": password,
            "loginToken": self._login_token
        }
        self._header = {"Content-Type": "application/json", "Cookie": cookie}
        login_result = requests.request('POST', self.__get_api_url('loginByRsa'), data=json.dumps(login_body),
                                        headers=self._header, verify=False)
        self._cookie = login_result.cookies.get("Z-AUTH-CODE-%s" % self.port)
        cookie = 'Z-AUTH-CODE-%s=%s' % (self.port, login_result.cookies.get("Z-AUTH-CODE-%s" % self.port))
        self._header.update({"username": self.username, "Cookie": cookie})
        return self._header

    def login_ume(self):
        self._header = self.update_header()
        param = {"username": self.username, "password": self.pwd, "grant_type": "PASSWORD"}
        access_token_result = requests.request('POST', self.__get_api_url('getAccessToken'), data=json.dumps(param),
                                               headers=self._header, verify=False)
        self._access_token = json.loads(access_token_result.text).get("access_token")

    def login(self):
        try:
            self.login_ume()
            return True
        except Exception:
            logging.error("can't login ume device: %s" % self.ip)
            return False

    def logout(self):
        header = {"Content-Type": "application/json", "username": self.username, "Cookie": self._cookie}
        logout_ume = self.__get_api_url('logout') + "?username={}&Z-AUTH-CODE={}".format(self.username, self._cookie)
        requests.request('GET', logout_ume, headers=header, verify=False)
        logout_by_token = self.__get_api_url('logout') + "?Z-ACCESS-TOKEN={}".format(self._access_token)
        requests.request('GET', logout_by_token, headers=header, verify=False)

    def _query_enodeb_attrs(self, subNetworkId, neId):
        body = {
            "neList": ["SubNetwork={},ManagedElement={}".format(subNetworkId, neId)],
            "mocList": ["ManagedElement"],
        }
        message = requests.request('POST', self.__get_api_url('queryEnodeb'), data=json.dumps(body),
                                   headers=self._header, verify=False).json()
        if not message.get('message') and message['result']:
            attrNames = message['result'][0]['attrNames']
            values = message['result'][0]['values'][0]
            return dict(zip(attrNames, values))
        return {'mimVersion': '', 'mimType': '', 'managedElementType': ''}

    def query_ne_version(self, paras):
        enodeb_attrs = self._query_enodeb_attrs("%(subNetwork)s" % paras, "%(meId)s" % paras)
        return enodeb_attrs.get('mimVersion', u'站点的模型标识为空')

    def create_ranume_sta_ne_trace(self,BODY):
        body = BODY
        #self._header = self.update_header()
        self._header.update({"language-option": "en-US"})
        message = requests.request('POST', self.__get_api_url('createStaneTraceTask'), data=json.dumps(body),
                                   headers=self._header, verify=False).json()
        ID = re.findall("\d+", message.get('message'))
        subscriptionId,taskId = ID[0],ID[1]
        #print(subscriptionId)
        #print(taskId)
        return subscriptionId,taskId

    #def stop_ranume_sta_ne_trace(self):

    def delete_ranume_sta_ne_trace(self,taskId):
        url = self.__get_api_url('deleteStaneTraceTask')+taskId
        self._header.update({"language-option": "zh-CN"})
        message = requests.request('DELETE', url,
                                   headers=self._header, verify=False).json()
        delete_result = message.get('message')
        return delete_result

    def query_gnb_alias(self,taskId):
        url = self.__get_api_url('querygnbalias')+taskId
        message = requests.request('GET', url,
                                   headers=self._header, verify=False)
        #print(message.text[1:-1])
        return message.text[1:-1]