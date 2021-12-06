## Running with a virtual environment

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual
  Python environment for 3.7.9
- Check you have the pyenv version you need: `pyenv versions`
- You should see 3.7.9
- If you do not have the correct version of Python, install it like this: `pyenv install 3.7.9`
- On command line do this: `~/.pyenv/versions/3.7.9/bin/python -m venv env`
- This creates a folder called env. Then do this to activate the virtual environment: `source env/bin/activate`
- Lastly do this to check that you are now on the correct Python version: `python --version`
- You might need to upgrade pip environment `pip install --upgrade pip`
- You can install the dependencies with `pip install -r requirements.txt`
- You should run `python setup_and_seed.py` to get a local database setup and seeded with lookup data
- You can then run the app with `python manage.py runserver 0.0.0.0:8000` in the root directory


## Django environment variables

- DJANGO_SETTINGS_MODULE=iwocapay.settings;PYTHONUNBUFFERED=1