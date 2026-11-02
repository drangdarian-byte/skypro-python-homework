"""Independent CREATE / UPDATE / DELETE tests for Skypro's teacher table."""

from uuid import uuid4

from sqlalchemy import text


def new_teacher():
    unique_id = uuid4().int % 1_000_000_000 + 1_000_000_000
    email = f"skypro-test-{uuid4().hex}@example.invalid"
    return unique_id, email


def insert_teacher(db, teacher_id, email):
    db.execute(
        text(
            "INSERT INTO teacher (teacher_id, email, group_id) "
            "VALUES (:teacher_id, :email, :group_id)"
        ),
        {"teacher_id": teacher_id, "email": email, "group_id": 10},
    )


def test_insert_teacher(db):
    teacher_id, email = new_teacher()
    insert_teacher(db, teacher_id, email)

    result = db.execute(
        text(
            "SELECT email FROM teacher "
            "WHERE teacher_id = :teacher_id AND email = :email"
        ),
        {"teacher_id": teacher_id, "email": email},
    ).scalar_one()

    assert result == email


def test_update_teacher(db):
    teacher_id, email = new_teacher()
    insert_teacher(db, teacher_id, email)
    new_email = f"updated-{uuid4().hex}@example.invalid"

    updated = db.execute(
        text(
            "UPDATE teacher SET email = :new_email "
            "WHERE teacher_id = :teacher_id AND email = :email"
        ),
        {"new_email": new_email, "teacher_id": teacher_id, "email": email},
    )
    result = db.execute(
        text("SELECT email FROM teacher WHERE teacher_id = :teacher_id"),
        {"teacher_id": teacher_id},
    ).scalar_one()

    assert updated.rowcount == 1
    assert result == new_email


def test_delete_teacher(db):
    teacher_id, email = new_teacher()
    insert_teacher(db, teacher_id, email)

    deleted = db.execute(
        text(
            "DELETE FROM teacher "
            "WHERE teacher_id = :teacher_id AND email = :email"
        ),
        {"teacher_id": teacher_id, "email": email},
    )
    found = db.execute(
        text("SELECT email FROM teacher WHERE teacher_id = :teacher_id"),
        {"teacher_id": teacher_id},
    ).first()

    assert deleted.rowcount == 1
    assert found is None
