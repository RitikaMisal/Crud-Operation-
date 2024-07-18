from sqlalchemy import String, Boolean, Integer, Column, text
from database import Base

class Product(Base):
        __tablename__ = 'products'

        id = Column(Integer, primary_key=True, nullable=False)
        title = Column(String, nullable=False)
        description = Column(String, nullable=False)
        at_sales = Column(Boolean)  
        inventory = Column(Integer, server_default=text('0'), nullable=False)


