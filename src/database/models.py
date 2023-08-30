import enum
from datetime import date

from sqlalchemy import Boolean, Column, DateTime,ForeignKey, Integer, Numeric, String, Table, Text, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import aggregated
from sqlalchemy import Enum

Base = declarative_base()


class Role(enum.Enum):
    user = 'User'
    moder = 'Moderator'
    admin = 'Administrator'


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[date] = mapped_column('created_at', DateTime, default=func.now())
    updated_at: Mapped[date] = mapped_column('updated_at', DateTime, default=func.now(), onupdate=func.now())
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    role: Mapped[Enum] = mapped_column('role', Enum(Role), default=Role.user)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] =  mapped_column(Boolean, default=True)



# Create Black list of access token
class BlacklistToken(Base):
    __tablename__ = 'blacklist_tokens'

    id = Column(Integer, primary_key=True)
    token = Column(String(500), unique=True, nullable=False)
    blacklisted_on = Column(DateTime, default=func.now())