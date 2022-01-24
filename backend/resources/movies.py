from fastapi import APIRouter, HTTPException, Depends, status
router = APIRouter(prefix='/movies', tags=["movies"])
