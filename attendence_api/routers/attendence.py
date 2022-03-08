from fastapi import APIRouter
from attendence_api.predict import predict
from attendence_api.ExcelFile import register_attendance

router=APIRouter(
    tags=['Attendence']
)

@router.post("/attendence")
def _post_image(image):
    try:
        predicted_name = predict(image)
        register_attendance(predicted_name)
        return "success"
    except:
         return "failed"
   


