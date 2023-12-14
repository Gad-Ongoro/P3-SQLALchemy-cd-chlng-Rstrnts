from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, engine

Session = sessionmaker(bind=engine)
session = Session()

restaurant1 = Restaurant(id=1, name="KFC", price=30)
restaurant2 = Restaurant(id=2, name="Big_Square", price=50)
restaurant3 = Restaurant(id=3, name="Red_Kitchen", price=40)
restaurant4 = Restaurant(id=4, name="Chicken_Inn", price=20)

session.query(Restaurant).delete()
session.commit()

session.add_all([restaurant1, restaurant2, restaurant3, restaurant4])
session.commit()


customer1 = Customer(id=1, first_name="Muhammad", last_name = "Gaddafi")
customer2 = Customer(id=2, first_name="Allahdu", last_name = "Jamil")
customer3 = Customer(id=3, first_name="Sean", last_name = "Newton")
customer4 = Customer(id=4, first_name="John", last_name = "Doe")

session.query(Customer).delete()
session.commit()

session.add_all([customer1, customer2, customer3, customer4])
session.commit()


review1 = Review(id=1, rating=4, comment="Yummy", restaurant_id=1, customer_id= 1)
review2 = Review(id=2, rating=5, comment="Spicy", restaurant_id=2, customer_id= 3)
review3 = Review(id=3, rating=3, comment="Nice", restaurant_id=3, customer_id= 2)
review4 = Review(id=4, rating=2, comment="Sweet", restaurant_id=4, customer_id= 4)

session.query(Review).delete()
session.commit()

session.add_all([review1, review2, review3, review4])
session.commit()

fake = Faker()
# print(fake.name())


# READ and print()
# restaurans_query = session.query(Restaurant).all()
# for rest in restaurans_query:
#     print(rest)

# customers_query = session.query(Customer).all()
# for customer in customers_query:
#     print(customer)

review_query = session.query(Review).all()
for review in review_query:
    print(review)