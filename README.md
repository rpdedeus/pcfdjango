# pcfdjango

This purpose of this project is to act as a template for Django applications deployed to Cloud Foundry environments.

## Running locally

1. Clone project and navigate to root directory where the project was cloned.

```none
mkdir /Users/$(whoami)/Dev/
cd /Users/$(whoami)/Dev/
git clone https://github.com/rpdedeus/pcfdjango.git
cd pcfdjango
```

2. Create and activate virtualenv for local development

```none
pip install virtualenv
virtualenv ~/.envs/pcfdjango
source ~/.envs/pcfdjango/bin/activate
```

3. Install project dependencies

```none
pip install -r requirements.txt
```

3. Apply database migrations

```none
python manage.py migrate --settings=settings.local
```

4. Run project

```none
python manage.py runserver --settings=settings.local
```

5. Validate project is working

```none
http://localhost:8000/
```

### Apply DJANGO_SETTINGS_MODULE environment variable (Optional)
It is possible to avoid having to pass the settings flag to the manage.py script by using an environment variable. See details [here](https://docs.djangoproject.com/en/2.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)

##  Pre-Deployment

1. [Create cloud foundry account](https://login.run.pivotal.io/login)
2. [Download cf cli](https://console.run.pivotal.io/tools) and follow instructions on the page.


## Deployment

1. Login to cf cli

```
cf login -a https://api.run.pivotal.io
```

2. From the project's root directory, issue the command to push the applications

```
cf push
```

## Maintenance / management

### Run Tasks
[Docs](https://docs.cloudfoundry.org/devguide/using-tasks.html)

```
cf run-task pcfdjango "python --version"
```

## Troubleshooting

* Tail logs

```
cf logs pcfdjango
```

* Validate app status

View all apps in the current org/space

```
cf apps
```

or  

View specific app in the current org/space

```
cf apps pcfdjango
```

* ssh into container

```
cf ssh pcfdjango
```

## Misc

### Generate a new SECRET_KEY

Each deployment environment should have a different key.

```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
