from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    create_engine,
    FLOAT,
    select,
    update,
    delete
)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr, Any
from lesson11_pydanticschema import ProductParser, ProductModel
from io import TextIOWrapper


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)
    engine = create_engine(url='postgresql://myuser:postgres@127.0.0.1:5432/projectdb')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


# class Statuses(Base):
#     name = Column(VARCHAR(10), nullable=False, unique=True)
#
# class Users(Base):
#     name = Column(VARCHAR(24), nullable=False)
#     email = Column(VARCHAR(24), nullable=False, unique=True)
#
# class Orders(Base):
#     user_id = Column(INT, ForeignKey(column='users.id', ondelete='RESTRICT'), nullable=False)
#     status_id = Column(INT, ForeignKey(column='statuses.id', ondelete='RESTRICT'), nullable=False)

class Category(Base):
    name = Column(VARCHAR(24), nullable=False, unique=True)
    products = relationship(argument='Products', back_populates='category')


class Products(Base):
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    price = Column(FLOAT, nullable=False)
    count = Column(INT, nullable=False)
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)
    category = relationship(argument='Category', back_populates='products')


# insert category items to db
with Base.session() as session:
    category1 = Category(name='Fruit')
    category2 = Category(name='Vegetables')
    session.add_all((category1, category2))
    session.commit()
    session.refresh(category1)
    session.refresh(category2)


#send to db
with open('product.csv', 'r', encoding='utf-8') as file:  # type: TextIOWrapper
    schema = ProductParser.parse(file=file, delimiter=',')
    print(schema)
    for obj in schema:
        with Products.session() as session:
            pr1 = Products(**obj.model_dump(), category_id=1)
            session.add(pr1)
            session.commit()


# get from db
with Products.session() as session:
    products = session.scalars(select(Products)).fetchall()
    data = []
    for product in products:
        y = ProductModel.model_validate(product.__dict__)
        data.append(y)
    with open('product_dump.csv', 'w', encoding='utf-8') as file2:  # type: TextIOWrapper
        ProductParser.dump(objs=data, file=file2, delimiter=',')


# class OrderItems(Base):
#     order_id = Column(INT, ForeignKey(column='orders.id', ondelete='RESTRICT'), nullable=False)
#     product_id = Column(INT, ForeignKey(column='products.id', ondelete='RESTRICT'), nullable=False)




