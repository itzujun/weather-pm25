# _*_ coding:utf-8 _*_

"""
PM2.5 爬虫天气,并保存在数据库中
21108.12.31
"""

__author__ = "liuzujun"

import time

import requests
from bs4 import BeautifulSoup
from app.model import CityWeather
from app.config import db


def init_db():
    db.create_all()


def drop_db():
    db.drop_all()

url = "http://www.pm25.in/rank"

if __name__ == "__main__":
    init_db()
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        lis = soup.select("table.table-striped tbody tr")
        record_d = []
        count = 1
        for a in lis:
            record_dic = {}
            tds = a.find_all("td")
            record_dic["城市"] = tds[1].text
            record_dic["AQI"] = tds[2].text
            record_dic["PM2.5:"] = tds[6].text
            record_dic["空气质量"] = tds[3].text
            record_d.append(record_dic)
            query = CityWeather.query.filter_by(city=tds[1].text, time=time.strftime("%Y%m%d")).first()
            if query is not None:
                query.AQI = tds[2].text
                query.quality = tds[3].text
                query.pm = tds[6].text
                query.time = time.strftime("%Y%m%d")
                query.city = tds[1].text
                db.session.commit()
            else:
                weather = CityWeather(time=time.strftime("%Y%m%d"), city=tds[1].text,
                                      AQI=tds[2].text, quality=tds[3].text, pm=tds[6].text)
                db.session.add(weather)
                db.session.commit()
            db.session.close()
    except Exception as e:
        print("error: ", e)
