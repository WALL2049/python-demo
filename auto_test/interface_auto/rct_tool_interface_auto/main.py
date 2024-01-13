# coding=utf-8
import json
import time
import datetime
import threading

from Ume import Ume
from Business import Bussiness_Type

path = 'config.json'
f = open(path, 'r', encoding='utf-8')
m = json.load(f)

UME_ip = m.get('UME_ip')
GNB_IP = m.get('GNB_IP')
UE_CORE_IP_  UDSIP = m.get('UE_CORE_IP_UDSIP')

neId = m.get('neId')
subnetworkId = m.get('subnetworkId')
'''
body = {
    "menuId": "ranume-sta-ne-trace",
    "traceName": "NE20221122203819",
    "comments": "",
    "scheduleInfo": {
        "strategy": "timing",
        "start": (datetime.datetime.now()-datetime.timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        "end": (datetime.datetime.now() - datetime.timedelta(hours=7)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "timing": [ ]
    },
    "dataViewMode": "2",
    "resInfos": [
        {
            "managedElementType": "ITBBU",
            "mimType": "ITRAN-PNF",
            "mimVersion": "V5.55.10.20P31R19-1",
            "neInfos": [
                {
                    "id": "43df84a7-77bc-4d13-868a-f9455e90f1f7",
                    "neName": "RT_J3_NSAMU_鲍宇辉_10276605",
                    "neId": "15762",
                    "subnetwork": "340999",
                    "ipAddress": "10.230.157.62"
                }
            ]
        }
    ],
    "services": [
        {
            "serviceType": "5gnr",
            "extend": [ ],
            "eventFilters": [
                {
                    "taskTypeName": "IperfData",
                    "events": [
                        {
                            "eventName": "CELL_PDCP_THROUGHPUT",
                            "eventId": [
                                "43800"
                            ],
                            "properties": [ ],
                            "moId": "43800"
                        }
                    ],
                    "filters": [
                        {
                            "filter": "aProtocolTypeFilter",
                            "value": "0",
                            "moId": "aProtocolTypeFilter"
                        },
                        {
                            "filter": "bIperfDirectionFilter",
                            "value": "1",
                            "moId": "bIperfDirectionFilter"
                        },
                        {
                            "filter": "udpBufferSizeFilter",
                            "value": "1360",
                            "moId": "udpBufferSizeFilter"
                        },
                        {
                            "filter": "udpFlowBandWidthFilter",
                            "value": "100",
                            "moId": "udpFlowBandWidthFilter"
                        },
                        {
                            "filter": "iperfDurationFilter",
                            "value": "9999",
                            "moId": "iperfDurationFilter"
                        },
                        {
                            "filter": "portNoFilter",
                            "value": "12345",
                            "moId": "portNoFilter"
                        },
                        {
                            "filter": "tcpWindowSizeFilter",
                            "value": "512",
                            "moId": "tcpWindowSizeFilter"
                        },
                        {
                            "filter": "iperUeIpFilter",
                            "value": str(UE_CORE_IP_UDSIP),
                            "moId": "iperUeIpFilter"
                        },
                        {
                            "filter": "dlIperfNumPerUeFilter",
                            "value": "1",
                            "moId": "dlIperfNumPerUeFilter"
                        }
                    ]
                }
            ]
        }
    ]
}
'''
def getbody(ne_message):
    traceName = neId + 'UDP'
    mimVersion = ne_message.get('version')
    id = ne_message.get('id')
    neName = ne_message.get('name')
    subnetwork = subnetworkId
    ipAddress = ne_message.get('ipAddress')
    ue_core_ip_str = json.dumps(UE_CORE_IP_UDSIP)
    body = {
        "menuId": "ranume-sta-ne-trace",
        "traceName": traceName,
        "comments": "",
        "scheduleInfo": {
            "strategy": "timing",
            "start": (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            "end": (datetime.datetime.now() - datetime.timedelta(hours=7)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "timing": []
        },
        "dataViewMode": "2",
        "resInfos": [
            {
                "managedElementType": "ITBBU",
                "mimType": "ITRAN-PNF",
                "mimVersion": mimVersion,
                "neInfos": [
                    {
                        "id": id,
                        "neName": neName,
                        "neId": neId,
                        "subnetwork": subnetwork,
                        "ipAddress": ipAddress
                    }
                ]
            }
        ],
        "services": [
            {
                "serviceType": "5gnr",
                "extend": [],
                "eventFilters": [
                    {
                        "taskTypeName": "IperfData",
                        "events": [
                            {
                                "eventName": "CELL_PDCP_THROUGHPUT",
                                "eventId": [
                                    "43800"
                                ],
                                "properties": [],
                                "moId": "43800"
                            }
                        ],
                        "filters": [
                            {
                                "filter": "aProtocolTypeFilter",
                                "value": "0",
                                "moId": "aProtocolTypeFilter"
                            },
                            {
                                "filter": "bIperfDirectionFilter",
                                "value": "1",
                                "moId": "bIperfDirectionFilter"
                            },
                            {
                                "filter": "udpBufferSizeFilter",
                                "value": "1360",
                                "moId": "udpBufferSizeFilter"
                            },
                            {
                                "filter": "udpFlowBandWidthFilter",
                                "value": "100",
                                "moId": "udpFlowBandWidthFilter"
                            },
                            {
                                "filter": "iperfDurationFilter",
                                "value": "9999",
                                "moId": "iperfDurationFilter"
                            },
                            {
                                "filter": "portNoFilter",
                                "value": "12345",
                                "moId": "portNoFilter"
                            },
                            {
                                "filter": "tcpWindowSizeFilter",
                                "value": "512",
                                "moId": "tcpWindowSizeFilter"
                            },
                            {
                                "filter": "iperUeIpFilter",
                                "value": ue_core_ip_str,
                                "moId": "iperUeIpFilter"
                            },
                            {
                                "filter": "dlIperfNumPerUeFilter",
                                "value": "1",
                                "moId": "dlIperfNumPerUeFilter"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    #print(body)
    return body

def rct_udp(gnbip, ue, port):
    Bussiness_Type(gnbip, ue, port).start_udp_rct()

def pdn_udp(gnbip, ue, port):
    Bussiness_Type(gnbip, ue, port).start_udp_pdn()

def rct_tcp(gnbip, ue, port):
    Bussiness_Type(gnbip, ue, port).start_tcp_rct()

def pdn_tcp(gnbip, ue, port):
    Bussiness_Type(gnbip, ue, port).start_tcp_pdn()

def threading_udp():
    t1 = threading.Thread(target=rct_udp, args=(GNB_IP, UE_CORE_IP_UDSIP[0], '12345'))
    t2 = threading.Thread(target=rct_udp, args=(GNB_IP, UE_CORE_IP_UDSIP[1], '15345'))
    t3 = threading.Thread(target=rct_udp, args=(GNB_IP, UE_CORE_IP_UDSIP[2], '18345'))
    t4 = threading.Thread(target=pdn_udp, args=(GNB_IP, UE_CORE_IP_UDSIP[3], '21345'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

def threading_tcp():
    t1 = threading.Thread(target=rct_tcp, args=(GNB_IP, UE_CORE_IP_UDSIP[0], '10218'))
    t2 = threading.Thread(target=rct_tcp, args=(GNB_IP, UE_CORE_IP_UDSIP[1], '10219'))
    t3 = threading.Thread(target=rct_tcp, args=(GNB_IP, UE_CORE_IP_UDSIP[2], '10216'))
    t4 = threading.Thread(target=pdn_tcp, args=(GNB_IP, UE_CORE_IP_UDSIP[3], '10217'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == '__main__':
    ume = Ume(UME_ip)
    ume.login()
    ne_message = json.loads(ume.query_gnb_alias(neId))
    body = getbody(ne_message)
    subscriptionId,taskId = ume.create_ranume_sta_ne_trace(body)
    #time.sleep(20)
    print("请输入灌包方式：")
    Input = input()
    if Input == 'UDP' or 'udp':
        threading_udp()
    elif Input == 'TCP' or 'tcp':
        threading_tcp()
    time.sleep(300)
    ume.delete_ranume_sta_ne_trace(subscriptionId)
    ume.logout()
    #input('Press Enter to exit...')