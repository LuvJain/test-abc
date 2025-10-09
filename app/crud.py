from sqlalchemy.orm import Session
from . import models, schemas
from .security import get_password_hash
from typing import List, Optional


# Note Operations

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


# User Operations

def get_user(db: Session, user_id: int):
    """Get a user by ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    """Get a user by username."""
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of users with pagination."""
    return db.query(models.User).order_by(models.User.created_at.desc()).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user."""
    # Check if user with this email or username already exists
    db_user_email = get_user_by_email(db, email=user.email)
    if db_user_email:
        return None

    db_user_username = get_user_by_username(db, username=user.username)
    if db_user_username:
        return None

    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create the user object
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        full_name=user.full_name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    """Update a user's information."""
    db_user = get_user(db, user_id)
    if db_user is None:
        return None

    update_data = user.dict(exclude_unset=True)

    # Handle password separately to hash it
    if "password" in update_data:
        hashed_password = get_password_hash(update_data["password"])
        update_data["hashed_password"] = hashed_password
        del update_data["password"]

    # Check email uniqueness if being updated
    if "email" in update_data and update_data["email"] != db_user.email:
        existing_user = get_user_by_email(db, update_data["email"])
        if existing_user:
            return None

    # Check username uniqueness if being updated
    if "username" in update_data and update_data["username"] != db_user.username:
        existing_user = get_user_by_username(db, update_data["username"])
        if existing_user:
            return None

    # Apply updates
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    """Delete a user."""
    db_user = get_user(db, user_id)
    if db_user is None:
        return False

    db.delete(db_user)
    db.commit()
    return True