import requests
import re
import time

act = '20377308'
pwd = 'Zzsygz3-21'
form_data = {
    'sfzs':0,
    'bzxyy':2,
    'bzxyy_other':"",
    'brsfzc':1,
    'tw':"",
    'sfcxzz':"",
    'zdjg':"",
    'zdjg_other':"",
    'sfgl': "",
    'gldd': "",
    'gldd_other': "",
    'glyy': "",
    'glyy_other': "",
    'gl_start': "",
    'gl_end': "",
    'sfmqjc': "",
    'sfzc_14': 1,
    'sfqw_14': 0,
    'sfqw_14_remark': "",
    'sfzgfx': 0,
    'sfzgfx_remark': "",
    'sfjc_14': 0,
    'sfjc_14_remark': "",
    'sfjcqz_14': 0,
    'sfjcqz_14_remark': "",
    'sfgtjz_14': 0,
    'sfgtjz_14_remark': "",
    'szsqqz': 0,
    'sfyqk':"" ,
    'szdd': 1,
    'area': "%E5%B1%B1%E4%B8%9C%E7%9C%81%20%E6%9E%A3%E5%BA%84%E5%B8%82%20%E8%96%9B%E5%9F%8E%E5%8C%BA",
    'city': "%E6%9E%A3%E5%BA%84%E5%B8%82",
    'province': "%E5%B1%B1%E4%B8%9C%E7%9C%81",
    'address': "%E5%B1%B1%E4%B8%9C%E7%9C%81%E6%9E%A3%E5%BA%84%E5%B8%82%E8%96%9B%E5%9F%8E%E5%8C%BA%E4%B8%B4%E5%9F%8E%E8%A1%97%E9%81%93%E9%BB%84%E6%B2%B3%E4%B8%AD%E8%B7%AF121%E5%8F%B7%E6%96%B0%E5%AE%89%E5%B0%8F%E5%8C%BA%28%E7%A6%8F%E6%B3%89%E5%B7%B7%29",
    'geo_api_info': "%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22cEa%22%3A%22jsonp_375383_%22%2C%22position%22%3A%7B%22Q%22%3A34.80252%2C%22R%22%3A117.27283999999997%2C%22lng%22%3A117.27284%2C%22lat%22%3A34.80252%7D%2C%22message%22%3A%22Get%20ipLocation%20success.Get%20address%20success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220632%22%2C%22adcode%22%3A%22370403%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E9%BB%84%E6%B2%B3%E4%B8%AD%E8%B7%AF%22%2C%22streetNumber%22%3A%22121%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E5%B1%B1%E4%B8%9C%E7%9C%81%22%2C%22city%22%3A%22%E6%9E%A3%E5%BA%84%E5%B8%82%22%2C%22district%22%3A%22%E8%96%9B%E5%9F%8E%E5%8C%BA%22%2C%22township%22%3A%22%E4%B8%B4%E5%9F%8E%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%B1%B1%E4%B8%9C%E7%9C%81%E6%9E%A3%E5%BA%84%E5%B8%82%E8%96%9B%E5%9F%8E%E5%8C%BA%E4%B8%B4%E5%9F%8E%E8%A1%97%E9%81%93%E9%BB%84%E6%B2%B3%E4%B8%AD%E8%B7%AF121%E5%8F%B7%E6%96%B0%E5%AE%89%E5%B0%8F%E5%8C%BA%28%E7%A6%8F%E6%B3%89%E5%B7%B7%29%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D",
    'gwdz': "",
    'is_move': 0,
    'move_reason': "",
    'move_remark': "",
    'realname': "%E6%9C%B1%E7%9D%A6%E6%99%A8",
    'number': 20377308,
    'uid': 406490,
    'created': 1627729606,
    'date': 20210731,
    'created_uid': 31890,
    'id': 4133304,
    'gwszdd': "",
}
url = 'https://app.buaa.edu.cn/site/buaaStudentNcov/index'

def login(act,pwd):
    global url
    print("Login...ing")
    post_data = {"username":act,"password":pwd}
    Res = requests.post(url,data=post_data)
    print(f"text = {Res.text}")
    return Res

def fill(res):
    s = requests.session()
    day = time.strftime("%Y%m%d",time.localtime())
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/ncov/wap/default/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': res.headers['set-cookie']
    }
    data = re.sub(r'date=\d{8}', 'data=' + day, form_data)
    r = s.post('https://app.buaa.edu.cn/ncov/wap/default/save', data=data, headers=headers)
    return r

def main_handler(event, context):
    result = fill(login(act, pwd))
    return("DONE")


main_handler()