from sqlalchemy import Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.types import Date


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    full_name: Mapped[String] = mapped_column(String(200), nullable=False)
    email: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[String] = mapped_column(String(200), nullable=False)

    salary = relationship('Salary', uselist=False, cascade='all, delete')

    def __repr__(self):
        return f'User(id={self.id}, email={self.email})'


class Salary(Base):
    __tablename__ = 'salary'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('users.id'))
    amount: Mapped[Integer] = mapped_column(Integer,  nullable=False)
    date_increase: Mapped[Date] = mapped_column(Date, nullable=False)

    def __repr__(self):
        return f'Salary (id={self.id}, user_id={self.user_id})'
