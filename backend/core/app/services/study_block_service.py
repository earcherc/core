from fastapi import HTTPException
from typing import List
from sqlmodel import Session, select
from ..models import StudyBlock as StudyBlockTable
from ..schemas import StudyBlockCreate, StudyBlockUpdate, StudyBlockInDB
from sqlmodel import Session, select
from app.models import StudyBlock, UserProfile


async def get_user_study_blocks_func(
    user_id: int, session: Session
) -> List[StudyBlockInDB]:
    statement = select(StudyBlock).where(StudyBlock.user_id == user_id)
    results = session.exec(statement).all()

    return [StudyBlockInDB(**sb.__dict__) for sb in results]


async def create_study_block_func(
    study_block_data: StudyBlockCreate, session: Session
) -> StudyBlockInDB:
    new_study_block = StudyBlockTable(**study_block_data.dict())
    session.add(new_study_block)
    session.commit()
    session.refresh(new_study_block)

    return StudyBlockInDB(**new_study_block.__dict__)


async def update_study_block_func(
    study_block_id: int, study_block_data: StudyBlockUpdate, session: Session
) -> StudyBlockInDB:
    study_block_statement = select(StudyBlockTable).where(
        StudyBlockTable.id == study_block_id
    )
    study_block = session.exec(study_block_statement).first()

    if not study_block:
        raise HTTPException(status_code=404, detail="Study block not found")

    for key, value in study_block_data.dict().items():
        setattr(study_block, key, value)

    session.add(study_block)
    session.commit()
    session.refresh(study_block)

    return StudyBlockInDB(**study_block.__dict__)


async def delete_study_block_func(study_block_id: int, session: Session):
    study_block_statement = select(StudyBlockTable).where(
        StudyBlockTable.id == study_block_id
    )
    study_block = session.exec(study_block_statement).first()

    if not study_block:
        raise HTTPException(status_code=404, detail="Study block not found")

    session.delete(study_block)
    session.commit()

    return study_block_id
