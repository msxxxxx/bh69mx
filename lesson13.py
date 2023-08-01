from datetime import datetime
from sqlalchemy import Column, INT, VARCHAR, ForeignKey, TIMESTAMP, TEXT, create_engine, CheckConstraint, FLOAT
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr
from lesson11_pydanticschema import ProductParser, ProductDetail, Parser
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

with Category.session() as session:
    # создаем объект Person для добавления в бд
    s1 = Category(name='fruit')
    session.add(s1)     # добавляем в бд
    session.commit()     # сохраняем изменения
    print(s1.id)   # можно получить установленный id

with Products.session() as session:
    # создаем объект Person для добавления в бд
    pr1 = Products(title='banan', description='fruit', price=3.34, count=10, category_id=1)
    session.add(pr1)     # добавляем в бд
    session.commit()     # сохраняем изменения
    print(pr1.id)   # можно получить установленный id

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




