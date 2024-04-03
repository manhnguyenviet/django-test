### Installation:

```python
# clone the repo
git clone git@github.com:manhnguyenviet/django-test.git
cd django_test

# init the virtual environment
pyenv virtualenv 3.10.8 django_test
pyenv local django_test

# install dependencies
pip install -r requirements.txt

# cd to tutorial
cd tutorial

# migrate
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run the tests
python manage.py test quickstart.tests
python manage.py test quickstart.tests.BlogTestCase

```