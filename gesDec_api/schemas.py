from pydantic import BaseModel

class FeedbackBase(BaseModel):
    feedback: str
    # class Config:
    #     orm_mode=True

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackRead(FeedbackBase):
    id: int