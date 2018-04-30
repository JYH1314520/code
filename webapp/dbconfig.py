from django.conf import settings
import sqlalchemy
from sqlalchemy.engine.url import URL
__all__ = ['metadata']
def create_engine():
    url = URL(drivername=settings.DATABASE_ENGINE,
              database=settings.DATABASE_NAME,
              username=settings.DATABASE_USER,
              password=settings.DATABASE_PASSWORD,
              host=settings.DATABASE_HOST,
              port=settings.DATABASE_PORT or None,
              query = getattr(settings, 'DATABASE_OPTIONS', {})
              )
    options = getattr(settings, 'SQLALCHEMY_OPTIONS', {})
    engine = sqlalchemy.create_engine(url, **options)
    return engine
metadata = sqlalchemy.MetaData(create_engine())
