# -*- coding: utf-8 -*-
from alidayu import AlibabaAliqinFcSmsNumSendRequest
import json

# 其中appkey和secret是必须的参数
# url可选，默认为沙箱的URL，正式应用请传入 https://eco.taobao.com/router/rest
# partner_id为可选，其值为下载的TOP SDK中的top/api/base.py里的SYSTEM_GENERATE_VERSION

appkey = ''
secret = ''
url = 'https://eco.taobao.com/router/rest'
partner_id = '' #可选
#短信内容参数
params = {
    'a' : '1',
    'b' : '2'
}

req = AlibabaAliqinFcSmsNumSendRequest(appkey, secret, url, partner_id)
req.extend = "123456"
req.sms_type = "normal"
req.sms_free_sign_name = "注册验证"
req.sms_param = json.dumps(params,ensure_ascii=False)
req.rec_num = "13000000000"
req.sms_template_code = "SMS_5410290"
try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)