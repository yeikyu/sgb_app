# run.py
from app import create_app, db
#from app.models import User

app = create_app()

@app.cli.command('initdb')
def init_db():
    db.create_all()
    print('Database initialized.')

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
    .
>>>>>>> c7ad1f39ed03a94cf86e48dd1f93301a38c096a8
