## pydantic


## pydanticAI





## 意向




### 如何检查和检出JSON
```python

from datetime import date

from pydantic import BaseModel, ConfigDict, ValidationError


class Event(BaseModel):
    model_config = ConfigDict(strict=True)

    when: date
    where: tuple[int, int]


json_data = '{"when": "1987-01-28", "where": [51, -1]}'
print(Event.model_validate_json(json_data))  
#> when=datetime.date(1987, 1, 28) where=(51, -1)

try:
    Event.model_validate({'when': '1987-01-28', 'where': [51, -1]})  
except ValidationError as e:
    print(e)
    """
    2 validation errors for Event
    when
      Input should be a valid date [type=date_type, input_value='1987-01-28', input_type=str]
    where
      Input should be a valid tuple [type=tuple_type, input_value=[51, -1], input_type=list]
    """
    
```


### 如何处理残缺的JSON
```python

from pydantic_core import from_json

partial_json_data = '["aa", "bb", "c'  

try:
    result = from_json(partial_json_data, allow_partial=False)
except ValueError as e:
    print(e)  
    #> EOF while parsing a string at line 1 column 15

result = from_json(partial_json_data, allow_partial=True)
print(result)  
#> ['aa', 'bb']

```

```python
from pydantic_core import from_json

partial_dog_json = '{"breed": "lab", "name": "fluffy", "friends": ["buddy", "spot", "rufus"], "age'
dog_dict = from_json(partial_dog_json, allow_partial=True)
print(dog_dict)
#> {'breed': 'lab', 'name': 'fluffy', 'friends': ['buddy', 'spot', 'rufus']}
```