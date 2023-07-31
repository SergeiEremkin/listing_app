from sqlalchemy.ext.asyncio import AsyncSession

# from src.mappers.category_mapper import to_db_category
#from src.repositories.postgres.category import add_category
# from src.repositories.postgres.pg_tables.category import Category

from src.entities.web import category


# async def create_category_service(session: AsyncSession, category_validation: category.CreateCategory) -> Category:
#     db_category = await to_db_category(category_validation)
#     await add_category(session, db_category)
#     return db_category
