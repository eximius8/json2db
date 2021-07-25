"""Преобразование данных json в базу sql."""
from dbsetup import Goods, ShopsGoods
import json
from jsonschema import validate, exceptions


def json_to_db(filepath: str) -> None:
    """Функция преобразующая json данные из файла в базу sql."""
    with open('goods.schema.json', 'r') as fschema:
        schema = json.loads(fschema.read())

    with open(filepath, 'r') as fdata:
        try:
            data = json.loads(fdata.read())
        except json.decoder.JSONDecodeError:
            raise Exception("json файл содержит синтаксическую ошибку.")

    try:
        validate(instance=data, schema=schema)
    except exceptions.ValidationError:
        raise Exception("Неверный формат файла json. Отсутсвуют обязательные поля.")

    good = Goods.get_or_none(id=data['id'])
    if good:
        good.name = data['name']
        good.package_height = data['package_params']['height']
        good.package_width = data['package_params']['width']
        good.save()
    else:
        good = Goods.create(
                    id=data['id'],
                    name=data['name'],
                    package_height=data['package_params']['height'],
                    package_width=data['package_params']['width'])
    dquery = ShopsGoods.delete().where(ShopsGoods.id_good == good.id)
    dquery.execute()
    for shop in data['location_and_quantity']:
        ShopsGoods.create(
            location=shop['location'],
            amount=shop['amount'],
            id_good=good.id
        )


json_to_db('sample.json')
