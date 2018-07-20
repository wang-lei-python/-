#coding:utf8

from CCPRestSDK import REST
import ConfigParser

# 主账号
accountSid = '8aaf07086488623101648ede1f900639'

# 主账号token
accountToken = 'aaaf4505909e499d98e4b6c9e6fed653'

# 应用id
appId = '8aaf07086488623101648ede1fef0640'

# 请求地址http://
serverIP = 'app.cloopen.com';

# 请求端口
serverPort = '8883';

# REST版本号
softVersion = '2013-12-26';


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
# @param $tempId 模板Id

class CCP(object):
    '''发送短信的工具类,单例模式'''
    def __new__(cls):
        if not hasattr(cls,'instance'):
            #判断CCP中有没有类属性instance
            #如果没有,创建这个类的对象,并保存到类的属性instance中
            obj=super(CCP, cls).__new__(cls)
            #初始化REST,SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls.instance=obj

        #如果有则直接返回
        return cls.instance

    def send_template_sms(self,to,datas,temp_id):

        try:
            #调用云通讯的工具REST发送短信
            #sendTemplatSMS(to:手机号,datas:数据内容,模板id)
            result = self.rest.sendTemplateSMS(to, datas, temp_id)
            print(result)
        except Exception as e:
            raise e
        status_code=result.get('statusCode')
        if status_code=='000000':
            #表示发送成功
            return 0
        else:
            #发送失败
            return -1

if __name__=="__main__":
    ccp=CCP()
    ccp.send_template_sms('13294178370',['1234',5],1)







