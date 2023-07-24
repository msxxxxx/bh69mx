from pydantic import (
    BaseModel,
    Field,
    field_validator
)
from pydantic.types import Decimal, PositiveInt
from typing import List

products = [
    {'title': 'banan', 'descr': 'fruit', 'price': '3.34', 'count': '10'},
    {'title': 'orange', 'descr': 'fruit', 'price': '4.33', 'count': '4'},
    {'title': 'orange', 'descr': 'fruit', 'price': '4.33', 'count': '6'}
]
class Product(BaseModel):
    title: str
    descr: str
    price: Decimal = Field(max_digits=8, decimal_places=2)
    count: PositiveInt

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if len(value) > 128:
            raise ValueError("Not much 128 symbols")
        return value

    @field_validator("descr")
    @classmethod
    def validate_descr(cls, value):
        if len(value) > 4096:
            raise ValueError("Not much 4096 symbols")
        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: Decimal = Field(max_digits=8, decimal_places=2)):
        return value

    @field_validator("count")
    @classmethod
    def validate_count(cls, value: PositiveInt):
        return value

class Products(BaseModel):
    products: List[Product]

m = Products(products=products)
print(m.model_dump())
