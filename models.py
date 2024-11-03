from typing import Annotated
from decimal import Decimal
from datetime import datetime

from sqlalchemy import Numeric, ForeignKey, String, Text, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


intpk = Annotated[int, mapped_column(primary_key=True)]
name = Annotated[str, mapped_column(String(length=100))]
currency = Annotated[Decimal, mapped_column(Numeric(10, 2))]
amount = Annotated[int, mapped_column(CheckConstraint('amount >= 0'))]
email = Annotated[str, mapped_column(String(length=254))]
description = Annotated[str, mapped_column(Text)]


class Base(DeclarativeBase):
    pass


class Genre(Base):

    __tablename__ = "genre"

    genre_id: Mapped[intpk]

    name_genre: Mapped[name]

    books: Mapped[list['Book']] = relationship(back_populates='genre')


class Author(Base):

    __tablename__ = "author"

    author_id: Mapped[intpk]

    name_author: Mapped[name]

    books: Mapped[list['Book']] = relationship(back_populates='author')


class Book(Base):

    __tablename__ = "book"

    book_id: Mapped[intpk]

    title: Mapped[name]

    author_id: Mapped[int] = mapped_column(ForeignKey('author.author_id'))
    author: Mapped[Author] = relationship(back_populates='books')

    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.genre_id'))
    genre: Mapped[Genre] = relationship(back_populates='books')

    price: Mapped[currency]

    amount: Mapped[amount]

    buy_books: Mapped[list['BuyBook']] = relationship(back_populates='book')


class City(Base):

    __tablename__ = 'city'

    city_id: Mapped[intpk]

    name_city: Mapped[name]

    days_delivery: Mapped[int] = mapped_column(CheckConstraint('days_delivery >= 0'))

    clients: Mapped[list['Client']] = relationship(back_populates='city')


class Client(Base):

    __tablename__ = 'client'

    client_id: Mapped[intpk]

    name_client: Mapped[name]

    city_id: Mapped[int] = mapped_column(ForeignKey('city.city_id'))
    city: Mapped[City] = relationship(back_populates='clients')

    email: Mapped[email]

    buys: Mapped[list['Buy']] = relationship(back_populates='client')


class Buy(Base):

    __tablename__ = 'buy'

    buy_id: Mapped[intpk]

    buy_description: Mapped[description]

    client_id: Mapped[int] = mapped_column(ForeignKey('client.client_id'))
    client: Mapped[Client] = relationship(back_populates='buys')

    buy_books: Mapped[list['BuyBook']] = relationship(back_populates='buy')

    buy_steps: Mapped[list['BuyStep']] = relationship(back_populates='buy')


class Step(Base):

    __tablename__ = 'step'

    step_id: Mapped[intpk]

    name_step: Mapped[name]

    buy_steps: Mapped[list['BuyStep']] = relationship(back_populates='step')


class BuyStep(Base):

    __tablename__ = 'buy_step'

    buy_step_id: Mapped[intpk]

    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.buy_id'))
    buy: Mapped[Buy] = relationship(back_populates='buy_steps')

    step_id: Mapped[int] = mapped_column(ForeignKey('step.step_id'))
    step: Mapped[Step] = relationship(back_populates='buy_steps')

    buy_step_beg: Mapped[datetime]

    buy_step_end: Mapped[datetime]


class BuyBook(Base):

    __tablename__ = 'buy_book'

    buy_book_id: Mapped[intpk]

    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.buy_id'))
    buy: Mapped[Buy] = relationship(back_populates='buy_books')

    book_id: Mapped[int] = mapped_column(ForeignKey('book.book_id'))
    book: Mapped[Book] = relationship(back_populates='buy_books')

    amount: Mapped[amount]




