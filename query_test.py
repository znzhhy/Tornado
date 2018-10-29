from connect import session
from user_module import User

rs = session.query(User).filter(User.name=='nancheng')
print(rs, type(rs))


















