from fastapi import APIRouter, HTTPException, Depends, status
router = APIRouter(prefix='/common_actors', tags=["common_actors"])