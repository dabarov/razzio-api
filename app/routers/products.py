from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["items"],
)


@router.get("/")
async def read_products():
    return {"details": "all products"}


@router.get("/{product_id}")
async def read_product(product_id: str):
    return {"details": "single product"}
