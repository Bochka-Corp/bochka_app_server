from sqlalchemy.orm import Session

from bochka.orm.database import database


def get_sync_session() -> Session:
    with database.get_session() as session:
        try:
            yield session
        except Exception as exc:
            session.rollback()
            raise exc
