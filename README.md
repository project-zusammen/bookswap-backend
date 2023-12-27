# bookswap-backend

Hi, this is the repo for bookswap Rest API using Python Flask

make sure that you're accepted the invitation to become contributor of this repo.

### To contribute:

1. Clone the repository
2. Checkout to a feature branch, add and commit your changes
3. Push your feature branch
4. Create a PR to the master branch

### To run this server:

1. Create and activate Python Virtual environment
2. Install all dependencies using
   ```bash
   pip install -r requirements.txt
   ```
3. Rename the .template.env file into .env, add the required config
4. Make sure you have created a database on Postgres and edit the database URI on the .env file.
5. On the root path run this

```bash
flask shell
```

6. In the flask shell run

```bash
from root_path.app.models import *
db.create_all()
exit()
```

7. Run the application with

```bash
flask run
```
