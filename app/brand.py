# """
#     爬取丝芙兰网站的所有品牌名称
# """
# import re
#
# import requests
# import os
# from bs4 import BeautifulSoup
# from sqlalchemy import create_engine
# import json
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine('mysql+pymysql://root:san611027@localhost/sfl?charset=utf8mb4')
#
# db = declarative_base()
# Dbsession = sessionmaker(bind=engine)
# session = Dbsession()
#
#
#
#
# class Brand(db):
#     __tablename__ = 'brand'
#     id = Column(Integer, primary_key=True)
#     en = Column(String(50), unique=True)
#     zh = Column(String(50), unique=True)
#
#     def __repr__(self):
#         return '{} - {}'.format(self.en, self.zh)
#
#
# class Product(db):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True)
#     brandCN = Column(String(50))
#     productCN = Column(String(50))
#     skuName = Column(String(50))
#
#
# def get_brand():
#     base_url = "https://www.sephora.cn/brand/"
#     r = requests.get(base_url).text
#     soup = BeautifulSoup(r, 'lxml')
#     result = soup.select('.NameZone')
#     result = map(lambda item: item.select('p'), result)
#     result = map(lambda it: map(lambda ite: ite.string, it), result)
#     result = list(result)
#     result = [list(n) for n in result]
#     json_str = json.dumps(result, ensure_ascii=False)
#     with open('./static/brand.json', 'w') as f:
#         f.write(json_str)
#
#
# def get_pro(brands):
#     all_link = {}
#     for brand in brands:
#         url = "https://www.sephora.cn/search/?k={}".format(brand[1])
#         link = []
#         r = requests.get(url).text
#         soup = BeautifulSoup(r, 'lxml')
#         links = soup.select('.p_productCN')
#         for l in links:
#             link.append(l.a.get('href'))
#         all_link[brand[1]] = link
#     json_str = json.dumps(all_link, ensure_ascii=False)
#     with open('./static/link.json', 'w') as f:
#         f.write(json_str)
#
#
# # with open('./static/brand.json') as f:
# #     brand = json.load(f)
# #     get_pro(brand)
#
# def get_number():
#     res = {}
#     with open('./static/link.json', 'r') as f:
#         links = json.load(f)
#         for k, v in links.items():
#             result = map(lambda item: re.findall(r'\d+', item), v)
#             result = list(result)
#             res[k] = result
#     return res
#
#
# def get_detail():
#     links = get_number()
#
#     for value in links.values():
#         for v in value:
#             url = "https://api.sephora.cn/v1/product/sku/optionalSkuSpec?productId={" \
#                   "}&skuId=&channel=PC&isPromotion=false".format(v[0])
#             r = requests.get(url).json()
#             brandCN = r.get('results').get('brandCN')
#             skuName = r.get('results').get('skuName')
#             productCN = r.get('results').get('productCN')
#             p = Product(brandCN=brandCN, skuName=skuName, productCN=productCN)
#             session.add(p)
#             session.commit()
#
#
# # get_detail()
