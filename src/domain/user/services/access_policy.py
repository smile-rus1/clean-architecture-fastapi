from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import UserID


class UserAccessPolicy:
    def __init__(self, user: User):
        self.user = user

    def check_self(self, user_id: int) -> bool:
        current_id = UserID(user_id)

        if self.user.id == current_id:
            return True
        return False
