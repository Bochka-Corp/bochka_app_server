import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from bochka.orm.models.baseclass import metadata

target_metadata = metadata


def get_url():
    """
    Retrieves the URL from the environment variables or config files.
    """
    environment = os.getenv('ENVIRONMENT', 'local')
    if environment == 'production':
        return os.getenv('DATABASE_URL_PROD')
    return os.getenv('DATABASE_URL_LOCAL')


# other settings ...

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=get_url()
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# execute run_migrations_online or run_migrations_offline
run_migrations_online()
