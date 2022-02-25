from fastapi import APIRouter
from gesDec_api.repositories import ModelRepository

router=APIRouter(
    tags=['Model']
)

path='D:/programming/api/gesture_detection-api/model-api/model-files'

@router.get("/model")
def _get_model():
    return ModelRepository.get_model()

@router.get("/group1-shard1of1.bin")
def _get_shar1of1():
    return ModelRepository._get_shar1of1()

# @router.get("/group1-shard2of3.bin")
# def _get_shard2of3():
#     return ModelRepository._get_shar2of3()

# @router.get("/group1-shard3of3.bin")
# def _get_shard3of3():
#     return ModelRepository._get_shar3of3()