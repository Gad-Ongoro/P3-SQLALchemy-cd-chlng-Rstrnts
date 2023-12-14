from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

restaurant_customer = Table(
    'restaurant_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    price = Column(Integer())

    reviews = relationship("Review", backref=("visited_rest"))
    customers = relationship('Customer', secondary=restaurant_customer, back_populates='restaurants')

    # def reviews(self):
    #     pass

    # def customers(self):
    #     pass

    def __repr__(self):
        return(
            f"Restaurant: {self.name}(${self.price})"
        )
    pass

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    reviews = relationship("Review", backref=('rest_customer'))
    restaurants = relationship('Restaurant', secondary=restaurant_customer, back_populates='customers')

    # def reviews(self):
    #     pass

    # def restaurants(self):
    #     pass

    def __repr__(self):
        return(
            f"Name: {self.first_name} {self.last_name}"
        )
        pass
    pass

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    comment = Column(String(255))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    # def customer(self):
    #     return(self.instances)
    #     pass

    # def restaurant(self):
    #     pass

    def __repr__(self):
        return(
            # f"Rating:{self.rating}"
            f"{self.rest_customer.first_name} ({self.visited_rest.name}): {self.comment} {self.rating}"
        )
        pass
    pass

engine = create_engine('sqlite:///restaurants.db')
# engine = create_engine('mysql+mysqlconnector://root:😂😂😂😂😂@localhost:3306/moringa_school_practice', echo = True)
Base.metadata.create_all(engine)