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

    name = CharField(help_text='наименование товара')
    package_height = FloatField(help_text='высота упакованного товара')
    package_width = FloatField(help_text='ширина упакованного товара')

    class Meta:
        database = db
        table_name = 'goods'


class ShopsGoods(Model):

    location = CharField(help_text='адрес магазина')
    amount = IntegerField(help_text='количество этого товара в этом магазине')
    id_good = ForeignKeyField(
        Goods,
        column_name='id_good',
        backref='shops_goods',
        help_text='идентификатор товара')

    class Meta:
        database = db
        table_name = 'shops_goods'


db.connect()
db.create_tables([Goods, ShopsGoods])
