from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    ForeignKeyField,
    FloatField,
    IntegerField
)

db = SqliteDatabase('warehouse.db')

class Goods(Model):

    name = CharField()
    package_height = FloatField()
    package_width = FloatField()

    class Meta:
        database = db
        table_name = 'goods'


class ShopsGoods(Model):

    location = CharField()
    amount = IntegerField()
    id_good = ForeignKeyField(Goods, column_name='id_good', backref='shops_goods')

    class Meta:
        database = db
        table_name = 'shops_goods'

db.connect()
db.create_tables([Goods, ShopsGoods])