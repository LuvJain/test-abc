from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional


def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).order_by(models.Note.updated_at.desc()).offset(skip).limit(limit).all()


def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = get_note(db, note_id)
    if db_note is None:
        return None

    update_data = note.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if db_note is None:
        return False

    db.delete(db_note)
    db.commit()
    return True