from db import db
from pony.orm import PrimaryKey, Required, Optional


class Feedback(db.Entity):
    __table__ = "feedback table"

    id = PrimaryKey(int, auto=True)
    user =Optional(str,default='anonymous')
    feedback = Required(str)