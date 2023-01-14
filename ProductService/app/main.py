from fastapi import FastAPI, HTTPException
# from ProductService.app.Product import Product # for IDE Pycharm
from app.Product import Product

productsList: list[Product] = [
    Product("102301", "Macbook 14inch M1", "Apple", "2000$"),
    Product("102302", "Macbook Air 13inch M2", "Apple", "1300$"),
    Product("102303", "HP Zenbook 2018", "HP", "1200$"),
    Product("102304", "HP Spectre X360 16", "HP", "2300$"),
    Product("102305", "Microsoft Surface Laptop 5 ", "Microsoft", "1500$")
]

app = FastAPI()

@app.get("/v1/products")
async def getProductsList():
    return productsList

@app.get("/v1/products/{idProduct}")
async def getProductById(idProduct: str):
    choosenProduct = [item for item in productsList if item.IdProduct == idProduct]
    if len(choosenProduct) > 0:
        return choosenProduct[0]
    raise HTTPException(status_code=404, detail="Product is not founded!")



