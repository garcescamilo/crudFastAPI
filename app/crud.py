from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

# Crear un nuevo item
async def create_item(db: AsyncSession, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    await db.commit()  # Hacer commit de manera asíncrona
    await db.refresh(db_item)  # Obtener la última versión del item
    return db_item

# Obtener un item por su ID
async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(models.Item).filter(models.Item.id == item_id))
    return result.scalar_one_or_none()

# Obtener todos los items
async def get_items(db: AsyncSession):
    result = await db.execute(select(models.Item))  # No hay limitador, obtiene todos los items
    return result.scalars().all()

# Eliminar un item
async def delete_item(db: AsyncSession, item_id: int):
    item = await get_item(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()  # Hacer commit de manera asíncrona
    return item
