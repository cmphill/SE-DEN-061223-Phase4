#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import db, Production

# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():


# 8.✅ Create a query to delete all existing records from Production    
    Production.query.delete()

    productions = []
# 9.✅ Create some seeds for production and commit them to the database. 
    p1 = Production(title='Hamlet', genre='drama', director='Bill Shakespeare', description='The tragedy of Hamlet, Prince of Denmark', budget="100000.00", image="https://upload.wikimedia.org/wikipedia/commons/6/6a/Edwin_Booth_Hamlet_1870.jpg", ongoing=True)
    productions.append(p1)
    p2 = Production(title='Cats', genre='Musical', director='Andrew Lloyed Webber', description='Cats and dogs sing', budget="200000.00", image="https://i.guim.co.uk/img/media/affb4861ad7c0ce1c8fb5b32bac895c90711b994/0_88_2992_1796/master/2992.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=3fde967aa96b217ca5a7b9f6e7c449a8", ongoing=True)
    productions.append(p2)
    p3 = Production(title='carmen', genre='Opera', director='Georges Bizet', description='Don Jose, carmen is mean', budget="200000.00", image="https://i.ytimg.com/vi/Lw1_GXU_rAQ/maxresdefault.jpg", ongoing=False)
    productions.append(p3)
    p4 = Production(title='Hamilton', genre='Musical', director='Lin-Manuel Miranda', description='Rapping production', budget="400000.00", image="https://m.media-amazon.com/images/M/MV5BNjViNWRjYWEtZTI0NC00N2E3LTk0NGQtMjY4NTM3OGNkZjY0XkEyXkFqcGdeQXVyMjUxMTY3ODM@._V1_FMjpg_UX1000_.jpg", ongoing=False)
    productions.append(p4)

    db.session.add_all(productions)
    db.session.commit()
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    