import requests, sys
import ssl
import base64 
import json
from aip import AipFace

#得到acess_token验证码
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=LwciGoB63nAAYnB8PHi4kSoU&client_secret=aAtGzvxaUP83aOR1bOhy1pVfiD93sGNx'
d = {'Content-Type':'application/json','charset':'UTF-8'}
r = requests.post(url,data=d)
requests_json = r.json()                          #requests 内置的josn解析器 转化为dict
access_token = requests_json['access_token']



#将图片解析成base格式
def get_photo_base(photo_url):
    with open(photo_url,"rb") as f:
        base64_data = base64.b64encode(f.read())
        base = str(base64_data,'utf-8')
        return base



#上传对比
dict = {}
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
base1 = get_photo_base(r'C:\Users\Administrator\Desktop\百度人脸识别api\4.jpg')  #上传图片

params = "{\"image\":\""+base1+"\",\"image_type\":\"BASE64\",\"face_field\":\"faceshape,facetype,age,beauty,gender\",\"max_face_num\":\"10\"}" #传入参数

request_url = request_url + "?access_token=" + access_token
res = requests.post(url=request_url, data=params)
result = res.json()

#得到参数

dict['face_num'] =  result['result']['face_num']       #人脸数目
dict['face_token'] =   result['result']['face_list'][0]['face_token']      #人脸图片的唯一标识
dict['face_location'] =  result['result']['face_list'][0]['location']      #人脸在图片中的位置
dict['age'] =  result['result']['face_list'][0]['age']                     #年龄
dict['beauty'] = result['result']['face_list'][0]['beauty']                #美丽分
dict['face_shape'] =   result['result']['face_list'][0]['face_shape']['type']     #square: 正方形 triangle:三角形 oval: 椭圆 heart: 心形 round: 圆形
dict['gender'] =  result['result']['face_list'][0]['gender']['type'] #性别

print(dict)

#入库


#联系opencv 




