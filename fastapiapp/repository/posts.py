from fastapiapp.db.models import Post
from fastapiapp.repository.repository import CRUDBase
from fastapiapp.schemas import PostDB

crud_post = CRUDBase(Post)