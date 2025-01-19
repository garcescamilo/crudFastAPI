from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, models, schemas, database

app = FastAPI()

# Ruta para crear un nuevo item
@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_item(db=db, item=item)

# Ruta para obtener todos los items
@app.get("/items/", response_model=list[schemas.Item])
async def read_items(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_items(db=db)

# Ruta para obtener un item por ID
@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: AsyncSession = Depends(database.get_db)):
    db_item = await crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Ruta para eliminar un item por ID
@app.delete("/items/{item_id}", response_model=schemas.Item)
async def delete_item(item_id: int, db: AsyncSession = Depends(database.get_db)):
    db_item = await crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
