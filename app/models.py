from sqlalchemy import Column, Integer, String
from app import db
from app import admin
from flask_admin.contrib.sqla import ModelView


class Brand(db.Model):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    en = Column(String(50), unique=True)
    zh = Column(String(50), unique=True)

    def __repr__(self):
        return '{} - {}'.format(self.en, self.zh)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    brandCN = Column(String(50))
    productCN = Column(String(50))
    skuName = Column(String(50))


admin.add_view(ModelView(Brand, db.session))
admin.add_view(ModelView(Product, db.session))

