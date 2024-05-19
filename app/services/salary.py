from app.schemas.users import UserSchema

def get_salary_by(user: UserSchema):
    return user.salary
