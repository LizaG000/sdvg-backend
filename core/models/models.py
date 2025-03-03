"""
from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, BigInteger, NUMERIC, DATETIME, TEXT
from datetime import datetime

metadata_obj = MetaData()

#связующая табличка
achievement_profile_table = Table(
    "achievement_profile",
    metadata_obj,
    Column("profile_id", Integer, primary_key=True, nullable=False),
    Column("achievement_id", Integer, primary_key=True, nullable=False)
)

lst_table = Table(
    "lst",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String),
    Column("date_created", DATETIME, default=datetime.now()),
    Column("date_modified", DATETIME, default=datetime.now()),
    Column("del", String, default=False)
)

# МЕГА ВАЖНЫЙ ВОПРОС
# Этой таблицы нет??
achievement_table = Table(
    "achievement",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String, nullable=False)
)

lst_value_table = Table(
    "lst_value",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("lst_id", Integer, nullable=False),
    Column("name", String, nullable=False),
    Column("date_created", DATETIME, default=datetime.now()),
    Column("date_modified", DATETIME, default=datetime.now()),
    Column("del", Boolean, nullable=False, default=False)
)


profile_table = Table(
    "profile",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("phone", BigInteger, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False), 
    Column("email", String, nullable=False),
    Column("date_created", DATETIME, default=datetime.now()),
    Column("date_modified", DATETIME, default=datetime.now()),
    Column("del", Boolean, nullable=False, default=False),
    Column("balance", NUMERIC, nullable=False, default=0) # что за тип numeric
)

task_table = Table(
    "task",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("profile_id", Integer),
    Column("title", String),
    Column("text", TEXT, nullable=False),
    Column("till_dt", DATETIME, nullable=False),
    Column("completed_dt", DATETIME),
    Column("date_created", DATETIME, default=datetime.now()),
    Column("date_modified", DATETIME, default=datetime.now())
)

transaction_table = Table(
    "transaction",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("value", NUMERIC, default=0, nullable=False),
    Column("date_created", DATETIME, default=datetime.now()),
    Column("date_modified", DATETIME, default=datetime.now())
)

"""