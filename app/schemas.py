from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    symbol: str = Field(..., example="AAPL")
    price: float = Field(..., example=145.32)
    quantity: int = Field(..., example=10)
    order_type: str = Field(..., example="buy")

class OrderResponse(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: int
    order_type: str

    class Config:
        orm_mode = True
