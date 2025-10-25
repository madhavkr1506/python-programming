from sqlalchemy import create_engine, Insert, Select, Update, Integer, String, Text, select, insert, text
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

BASE = declarative_base()

class VoiceAssistance(BASE):
    __tablename__ = "voice_assistance"
    __table_args__ = {"schema" : "genome"}

    speaker_id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    speaker_name : Mapped[str] = mapped_column(String(50))
    speaker_mfcc : Mapped[str] = mapped_column(Text)

class PrepareQuery:
    def __init__(self):
        self.show_grants = None
        self.select = None
        self.insert = None
    
    def prepare_select(self):
        try:
            query = select(VoiceAssistance)
            self.select = query
        except Exception as e:
            raise Exception(f"failed to prepare select query\nproblem: {e}")
    
    def prepare_insert(self):
        try:
            pass
        except Exception as e:
            raise Exception(f"failed to prepare insert query\nproblem: {e}")
    
    def show_grants_query(self):
        try:
            query = text("show grants for local@localhost;")
            self.show_grants = query
        except Exception as e:
            raise Exception(f"failed to prepare show grants query\nproblem: {e}")
    