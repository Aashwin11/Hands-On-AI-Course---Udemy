# Self referencing Model

from typing import List, Optional
from pydantic import BaseModel

class comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['comment']]=None

comment.model_rebuild() #Required after self referencing model

comment1=comment(
    id=1,
    content="First coment",
    replies=[
        comment(id=2,content="Reply to 1, from 1st user"),
        comment(id=3,content="Reply to 1 still, reploy from 2nd user"), 
    ]
)
