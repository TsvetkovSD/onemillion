from fastapi import APIRouter, Depends, HTTPException, Query, status

router = APIRouter(prefix="/answers", tags=["answers"])

@router.get("/universal")
async def universal():
    return {"answer": 42}