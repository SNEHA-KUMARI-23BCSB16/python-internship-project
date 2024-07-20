
# importing os class from python library
import os 

# setting up the absolute path 
base_dir=os.path.abspath(os.path.dirname(__file__)) 



# configuring the base directory path
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(base_dir, 'employees.db')
    sQLALCHEMY_TRACK_MODIFICATIONS= False