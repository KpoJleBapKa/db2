from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
class Client(Base):
    __tablename__ = 'client'
    ID = Column(Integer, primary_key=True)
    Address = Column(String(255))
    FullName = Column(String(255))
    Email = Column(String(255))
    PhoneNumber = Column(String(255))

class Computer(Base):
    __tablename__ = 'computer'
    ID = Column(Integer, primary_key=True)
    SSD = Column(String(255))
    PSU = Column(String(255))
    GPU = Column(String(255))
    CPU = Column(String(255))
    RAM = Column(String(255))
    HDD = Column(String(255))
    Motherboard = Column(String(255))

class Orders(Base):
    __tablename__ = 'orders'
    ID = Column(Integer, primary_key=True)
    ClientID = Column(Integer, ForeignKey('client.ID'))
    Client = relationship("Client")
    ClientAddress = Column(String(255))
    ClientFullName = Column(String(255))
    ClientEmail = Column(String(255))
    ClientPhoneNumber = Column(String(255))

class Warehouse(Base):
    __tablename__ = 'warehouse'
    ComputerID = Column(Integer, ForeignKey('computer.ID'), primary_key=True)
    Computer = relationship("Computer")

class Catalog(Base):
    __tablename__ = 'catalog'
    ComputerID = Column(Integer, primary_key=True)

engine = create_engine('mysql+pymysql://root:root@localhost/kroll')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Отримання даних з усіх таблиць
clients = session.query(Client).all()
computers = session.query(Computer).all()
orders = session.query(Orders).all()
warehouse = session.query(Warehouse).all()

# Функція для відображення даних
def display_clients():
    clients = session.query(Client).all()
    print("Clients:")
    for client in clients:
        print(f"ID: {client.ID}, FullName: {client.FullName}, Email: {client.Email}, PhoneNumber: {client.PhoneNumber}")

def display_computers():
    computers = session.query(Computer).all()
    print("Computers:")
    for computer in computers:
        print(f"ID: {computer.ID}, SSD: {computer.SSD}, PSU: {computer.PSU}, GPU: {computer.GPU}, CPU: {computer.CPU}, RAM: {computer.RAM}, HDD: {computer.HDD}, Motherboard: {computer.Motherboard}")

def display_orders():
    orders = session.query(Orders).all()
    print("Orders:")
    for order in orders:
        print(f"ID: {order.ID}, ClientID: {order.ClientID}, ClientAddress: {order.ClientAddress}, ClientFullName: {order.ClientFullName}, ClientEmail: {order.ClientEmail}, ClientPhoneNumber: {order.ClientPhoneNumber}")

def display_warehouse():
    warehouses = session.query(Warehouse).all()
    print("Warehouse:")
    for warehouse in warehouses:
        print(f"ComputerID: {warehouse.ComputerID}")

def display_catalog():
    catalogs = session.query(Catalog).all()
    print("Catalog:")
    for catalog in catalogs:
        print(f"ComputerID: {catalog.ComputerID}")


def display_menu():
    while True:
        print("\nМеню:")
        print("1. Catalog")
        print("2. Clients")
        print("3. Computers")
        print("4. Orders")
        print("5. Warehouse")
        print("0. Вихід")

        choice = input("Виберіть таблицю (або 0 для виходу): ")
        if choice == '1':
            display_catalog()
        elif choice == '2':
            display_clients()
        elif choice == '3':
            display_computers()
        elif choice == '4':
            display_orders()
        elif choice == '5':
            display_warehouse()
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

display_menu()