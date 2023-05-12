from ..models import StudyBlock as StudyBlockTable
from sqlmodel import Session, select, delete
from typing import Optional
from ..schemas import StudyBlockCreate, StudyBlockUpdate, StudyBlockInDB


async def create_study_block(study_block_data: StudyBlockCreate, session: Session):
    new_study_block = StudyBlockTable(**study_block_data.dict())

    session.add(new_study_block)

    session.commit()

    session.refresh(new_study_block)

    return new_study_block.id


def get_study_block(study_block_id: int, session: Session) -> Optional[StudyBlockInDB]:
    statement = select(StudyBlockTable).where(StudyBlockTable.id == study_block_id)
    study_block = session.exec(statement).first()
    if study_block:
        return StudyBlockInDB(**study_block.__dict__)


async def update_study_block(
    study_block_id: int, study_block_data: StudyBlockUpdate, session: Session
):
    study_block_statement = select(StudyBlockTable).where(
        StudyBlockTable.id == study_block_id
    )
    study_block = session.exec(study_block_statement).first()

    if not study_block:
        return None

    for var, value in vars(study_block_data).items():
        setattr(study_block, var, value if value else getattr(study_block, var))

    session.add(study_block)

    session.commit()

    session.refresh(study_block)

    return StudyBlockInDB(**study_block.__dict__)


async def delete_study_block(study_block_id: int, session: Session):
    study_block_statement = select(StudyBlockTable).where(
        StudyBlockTable.id == study_block_id
    )
    study_block = session.exec(study_block_statement).first()

    if not study_block:
        return None

    session.delete(study_block)
    session.commit()

    return study_block_id
