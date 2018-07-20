#coding:utf8
from qiniu import Auth,put_file,etag,urlsafe_base64_encode,put_data
import qiniu.config

#需要填写的acess key 和secret key
acess_key='nrL2RMP5dkv0Z4hHtWyo5-RBBDGyfRrcHqqWppi2'
secret_key='Ztz8olT8r_952F0e55jxA381rwUTg6uHPxn_j02n'

def storage(file_data):
    '''上传图片到七牛,file_data是文件的二进制数据'''
    #构建鉴权对象
    q=Auth(acess_key,secret_key)

    #要上传的空间
    bucket_name='ihome'

    #生成上传token,可以指定过期时间
    token=q.upload_token(bucket_name,None,3600)

    ret,info=put_data(token,None,file_data)
    # print(info)
    # print(ret)

    if info.status_code==200:
        #表示上传的成功,返回文件名
        # print(ret.get('key'))
        return ret.get('key')

    else:
        #表示上传失败
        raise Exception("上传的失败")

if __name__=='__main__':
    with open('fruit.jpg','rb') as f:
        file_data=f.read()
        storage(file_data)


