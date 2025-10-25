from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.port = "3306"
        self.username = "local"
        self.password = "Madhavkr1@"
        self.password = quote_plus(self.password)
        self.db = "genome"

        self.engine = None
        self.session = None

    def build_engine(self):
        try:
            connection_url = f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}"
            print(f"connection url: {connection_url}")
            engine = create_engine(
                url=connection_url
            )
            self.engine = engine

            if self.engine:
                with self.engine.connect() as conn:
                    response = conn.execute(text("select version();"))
                    if response:
                        print(f"response: {response.scalar_one()}")
        except Exception as e:
            raise Exception(f"failed to build db engine\nproblem: {e}")
        
    def create_session(self):
        try:
            if not self.engine:
                self.build_engine()

            session = sessionmaker(
                bind=self.engine,
                expire_on_commit=True,
                autoflush=True
            )
            session = session()
            self.session = session
            self.session.info["user"] = self.username
            self.session.info["database"] = self.db

            if self.session:
                print(f"session established:\n{session.info}")
        except Exception as e:
            raise Exception(f"failed to create session object for database connection\nproblem: {e}")
        