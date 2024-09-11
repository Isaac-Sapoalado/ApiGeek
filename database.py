from sqlmodel import SQLModel,create_engine


def get_engine():
  url = 'sqlite:///geek.db'
  engine = create_engine(url)

  return engine


def sync_database(engine):
  SQLModel.metadata.create_all(engine)