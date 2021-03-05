import requests
s=requests.Session()
headers={'cookie':'stuinfo=stuid=27011E8244D423A5&stuxm=AD3C218B1A157BE6&stubj=7285B8596DEF819F961F13D942957AE819DBB0DE49999A22'}
r=s.post("https://fyns.eduw.cn/stu/dk9.aspx",headers=headers)
data={'Button2':' 当前情况和上次一样，系统直接帮我打卡' , '__VIEWSTATEGENERATOR': 'BEBF4070' , '__VIEWSTATE': '/wEPDwUKLTk3MjYyNTU4NGRkbQwAF57GOqyjzXoXKqZTAftYIH3j/SOdUxlgAK6g7Oc='}
k=s.post('https://fyns.eduw.cn/stu/dk9.aspx',data=data,headers=headers)
h=k.text
data={'text':'健康打卡结果','desp':h}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
requests.post('https://sc.ftqq.com/SCU163529Tf148061edc6ebaccc0e26977924b5daa6041b8c4ceb01.send',headers=headers,data=data)
