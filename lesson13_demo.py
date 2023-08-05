from datetime import datetime
from sqlalchemy import Column, INT, VARCHAR, ForeignKey, TIMESTAMP, TEXT, create_engine, CheckConstraint, FLOAT, select
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr, Any
from lesson11_pydanticschema import ProductParser, ProductModel, Parser
from io import TextIOWrapper
from collections import namedtuple

class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)
    engine = create_engine(url='postgresql://myuser:postgres@127.0.0.1:5432/projectdb')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    def from_attributes(self, obj: Any):
        for k, v in obj.__dict__:
            if hasattr(self, k):
                setattr(self, k, v)

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
    # __table_args__ = (
    #     CheckConstraint('char_length(name) >= 4'),
    # )
    name = Column(VARCHAR(24), nullable=False, unique=True)
    products = relationship(argument='Products', back_populates='category')

class Products(Base):
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    price = Column(FLOAT, nullable=False)
    count = Column(INT, nullable=False)
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)
    category = relationship(argument='Category', back_populates='products')

# with Category.session() as session:
#     s1 = Category(name='fruit')
#     session.add(s1)
#     session.commit()
#     print(s1.id)
#
# with Products.session() as session:
#     pr1 = Products(title='banan', description='fruit', price=3.34, count=10, category_id=1)
#     session.add(pr1)
#     session.commit()
#     print(pr1.id)

#send to db
# with open('product.csv', 'r', encoding='utf-8') as file:  # type: TextIOWrapper
#     schema = ProductParser.parse(file=file, delimiter=',')
#     for i in schema:
#         print(i)
#         with Products.session() as session:
#             pr1 = Products(**i.model_dump(), category_id=1)
#             session.add(pr1)
#             session.commit()
#             print(pr1.id)

# with open('product.csv', 'r', encoding='utf-8') as file:  # type: TextIOWrapper
#     schema = ProductParser.parse(file=file, delimiter=',')
#     for i in schema:
#         print(i)

# get from db
with Products.session() as session:
    # ob = select(Products.id, Products.title, Products.description)
    #
    # objs = session.execute(ob).all()
    # for obj in objs:
    #     print(objs)
    #     # > <__main__.CompanyOrm object at 0x0123456789ab>
    #     co_model = ProductModel.model_validate(obj)
    #     print(co_model)

    people = session.scalars(select(Products)).fetchall()
    x = []
    for i in people:
        # print(i.__dict__)

        # print(ProductModel.model_validate(i.__dict__, from_attributes=True).model_dump())
        x1 = ProductModel.model_validate(i.__dict__, from_attributes=True)
        x.append(x1)
        # print(type(x))
    print(x)

        # # x1 = ProductModel.model_validate(i.__dict__, from_attributes=True).model_dump_json()
        # x1 = ProductModel.model_validate(i.__dict__, from_attributes=True)
        # # x = x.append(x1)
    with open('product_dump.csv', 'w', encoding='utf-8') as file2:  # type: TextIOWrapper
        ProductParser.dump(objs=x, file=file2, delimiter=',')


    # for u in session.query(User).all():
    #     print u.__dict__


    #     session.commit()


# class OrderItems(Base):
#     order_id = Column(INT, ForeignKey(column='orders.id', ondelete='RESTRICT'), nullable=False)
#     product_id = Column(INT, ForeignKey(column='products.id', ondelete='RESTRICT'), nullable=False)

# class Post(Base):
#     title = Column(VARCHAR(128), nullable=False)
#     descr = Column(TEXT, nullable=False)
#     date_created = Column(TIMESTAMP, default=datetime.utcnow())
#     date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
#     category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)
#     category = relationship(argument='Category', back_populates='posts')

    # @property
    # def date(self):
    #     return self.date_created.isoformat()


# print(Base.metadata.create_all(bind=Base.engine))
# print(Base.metadata.drop_all(bind=Base.engine))




