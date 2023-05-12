from fastapi import HTTPException
from typing import List
from sqlmodel import Session, select, delete
from ..models import StudyCategory as StudyCategoryTable
from ..schemas import StudyCategory, StudyCategoryInDB


async def get_all_study_categories(session: Session) -> List[StudyCategoryInDB]:
    study_category_statement = select(StudyCategoryTable)
    study_categories = session.exec(study_category_statement).all()

    return [StudyCategoryInDB(**stc.__dict__) for stc in study_categories]


async def create_study_category(
    study_category_data: StudyCategory, session: Session
) -> StudyCategoryInDB:
    new_study_category = StudyCategoryTable(**study_category_data.dict())
    session.add(new_study_category)
    session.commit()
    session.refresh(new_study_category)

    return StudyCategoryInDB(**new_study_category.__dict__)


async def update_study_category(
    study_category_id: int, study_category_data: StudyCategory, session: Session
) -> StudyCategoryInDB:
    study_category_statement = select(StudyCategoryTable).where(
        StudyCategoryTable.id == study_category_id
    )
    study_category = session.exec(study_category_statement).first()

    if not study_category:
        raise HTTPException(status_code=404, detail="Study category not found")

    for key, value in study_category_data.dict().items():
        setattr(study_category, key, value)

    session.add(study_category)
    session.commit()
    session.refresh(study_category)

    return StudyCategoryInDB(**study_category.__dict__)


async def delete_study_category(study_category_id: int, session: Session):
    study_category_statement = select(StudyCategoryTable).where(
        StudyCategoryTable.id == study_category_id
    )
    study_category = session.exec(study_category_statement).first()

    if not study_category:
        return None

    session.delete(study_category)
    session.commit()

    return study_category_id
