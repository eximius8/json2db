from dbsetup import Goods, ShopsGoods
import json
from jsonschema import validate


with open('goods.schema.json', 'r') as fschema:
    schema = json.loads(fschema.read())

with open('sample.json', 'r') as fdata:
    try:
        data = json.loads(fdata.read())
    except json.decoder.JSONDecodeError:
        raise Exception("Неверный формат файла json")
    


validate(instance=data, schema=schema)

print(data['id'])