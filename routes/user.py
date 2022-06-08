from typing import List, Generator
from fastapi import FastAPI


def get_db()-> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/',response_model=schemas.User)