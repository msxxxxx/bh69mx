from datetime import datetime
from sqlalchemy import Column, INT, VARCHAR, ForeignKey, TIMESTAMP, TEXT, create_engine, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr

class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)
    engine = create_engine(url='postgresql://myuser:postgres@127.0.0.1:5432/projectdb')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

class Statuses(Base):
    name = Column(VARCHAR(10), nullable=False, unique=True)

class Users(Base):
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)

class Orders(Base):
    user_id = Column(INT, ForeignKey(column='users.id', ondelete='RESTRICT'), nullable=False)
    status_id = Column(INT, ForeignKey(column='statuses.id', ondelete='RESTRICT'), nullable=False)

class Categories(Base):
    # __table_args__ = (
    #     CheckConstraint('char_length(name) >= 4'),
    # )
    name = Column(VARCHAR(24), nullable=False, unique=True)
    # posts = relationship(argument='Post', back_populates='category')

class Products(Base):
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(INT, ForeignKey(column='categories.id', ondelete='RESTRICT'), nullable=False)

class OrderItems(Base):
    order_id = Column(INT, ForeignKey(column='orders.id', ondelete='RESTRICT'), nullable=False)
    product_id = Column(INT, ForeignKey(column='products.id', ondelete='RESTRICT'), nullable=False)

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




