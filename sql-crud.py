from sqlalchemy import (
    create_engine, Column, Integer, String   
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

### executing the instructions from the "chinook" database ###
db = create_engine("postgresql:///chinook")
base = declarative_base()

### create a class based model for the "Programmer" table ###
class Programmer(base):
    __tablename__ = "programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of the sessionmaker class, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session but calling the session() sub-class defined above
session = Session()

### creating the database using declarative_base sub-class ###    
base.metadata.create_all(db)


### creating records on our programmer table ###
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

ben_fashan = Programmer(
    first_name = "Ben",
    last_name = "Fashan",
    gender = "M",
    nationality = "British",
    famous_for = "Being cool"
)

###  add each instance of the Programmers to the session ### 
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(ben_fashan)

# commit the session to the database
# session.commit()


###  updating a single record ### 
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Being really cool"

# # commit the session to the database
# session.commit()


### updating multiple records ### 
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

### deleting a single record - using input as user cannot see primary key ###
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
## defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer record has been deleted")
#     else:
#         print("Programmer record was not deleted")
# else:
#     print("No records found")

### deleting multiple records - using input as user cannot see primary key ###
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)

###  query the database to find all programmers ### 
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id, 
        programmer.first_name + " " + programmer.last_name, 
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
