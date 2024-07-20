# main file from where execution of whole Employee Management file begins

# importing create_app class to initalise the app and db
from App import create_app

app=create_app()

if __name__=='__main__': 
    app.run(debug=True) # runcommand
