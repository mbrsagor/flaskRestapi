# Flask Rest API

> Flask restful API project.

###### Instructions
- Python3.8
- Flask
- postgresql

Open your bash or terminal or ZSH then follow the instruction for ru the project in your local development server or somewhere else.
Here, the following setup for Mac I think linux should be same.

```
git clone https://github.com/mbrsagor/flaskRestapi.git
cd flaskRestapi
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

##### Migrate sqlite.db

```pip install Flask-SQLAchemy ```

```python
from models import db
db.create_all()
```
##### Set environment variables in terminal
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
