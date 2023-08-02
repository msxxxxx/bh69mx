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

    # def from_attributes(self, obj: Any):
    #     for k, v in obj.__dict__:
    #         if hasattr(self, k):
    #             setattr(self, k, v)

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

#WORK!!! send to db
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
with Products.session() as session:
    # SQLAlCHEMY CORE QUERY TO FETCH SPECIFIC COLUMNS
    query = select(Products.title, Products.description, Products.price, Products.count)
    # FETCH ALL THE RECORDS IN THE RESPONSE
    result = session.execute(query).fetchall()
    print(result)
    #
    # with open('product_dump.csv', 'w', encoding='utf-8') as file:  # type: TextIOWrapper
    #     ProductParser.dump(objs=result, file=file, delimiter=',')
            # pr1 = Products(**i.model_dump(), category_id=1)
            # session.add(pr1)
            # session.commit()
            # print(pr1.id)

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




