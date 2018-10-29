from user_module import User, UserDetails
from connect import  session

if __name__ == '__main__':
    row = session.query(User).get(1)
    print(row.name, row )