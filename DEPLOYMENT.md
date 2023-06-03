# Deployment
### Table of contents

- [Deploying the site](#deploying-the-site)
    - [Heroku app setup](#heroku-app-setup)
    - [Preparation for deployment](#preparation-for-deployment)
    - [Generate a SECRET KEY](#generate-a-secret-key)
    - [Setting up AWS](#setting-up-aws)
    - [Creating AWS groups, policies and users](#creating-aws-groups-policies-and-users)
    - [Connecting Django to our S3 bucket](#connecting-django-to-our-s3-bucket)
    - [Stripe Setup](#stripe-setup)
- [To fork a repository](#to-fork-a-repository)
- [To clone a repository](#to-clone-a-repository)
  


## Deploying the site

### Heroku app setup 
- Click the New button in the top right corner of the Heroku dashboard and choose Create New App.
- Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
- The database URL you copied from elephantSQL should be pasted into the value of a new configuration variable called DATABASE URL that you create in the settings tab (the value should not have quotation marks around it)

### Preparation for deployment
- Install dj_database_url and psycopg2 as they are both needed for connecting to the external database you've just created

        pip3 install dj_database_url==0.5.0 psycopg2

- Update your requirements.txt file

        pip3 freeze > requirements.txt

- In settings.py underneath import os, add import dj_database_url

- Locate the section for DATABASES and comment out the code. Add the following code below the commented out code, and use the URL copied from elephantSQL for the value:

        DATABASES = {
        'default': dj_database_url.parse('paste elephantSQL URL here...')
    }
- In the terminal, run the show migrations command to confirm connection to the external database.

        python3 manage.py showmigrations

- If it is connected to the database, you will see a list of unchecked migrations

- Now run migrations to migrate the models to the new database:

        python3 manage.py migrate

- Create a superuser for the new database.

        python3 manage.py createsuperuser
- Input a username, email and password when prompted.

- You should now be able to go to the browser tab on the left of the page in elephantsql, click the 'table queries' button and see the user you've just created by selecting the 'auth_user table'.

- Now you can add an if/else statement for the databases in settings.py, so that so you can use the development database while in development and the external database on the live site

        if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
      }
    }

- Install gunicorn which will act as our web server and freeze this to the requirements.txt file.

        pip3 install gunicorn pip3 freeze > requirements.txt

- Create a Procfile in the root directory. This instructs Heroku to build a web dyno that serves our Django app and runs Gunicorn.

- Add the following code in the procfile

        web:  gunicorn home_furniture.wsgi:application

- Disable collectstatic by running the following command in the terminal

        heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku--your-app-name-here

- Add the Heroku app and localhost by adding the following code in the settings.py

        ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]

- Save, add, commit and push the changes to GitHub.

        heroku git:remote -a {app name here}
        git push heroku master

- The deployed site is available to see now. You won't see any static file as we have not set that up yet.

- To enable automatic deploys on Heroku, click enable automatic deploys at the bottom of the page.

### Generate a SECRET KEY

- When you start a project in Django, a secret key is immediately generated; however, we shouldn't utilize this key in our deployed version as it makes our website insecure.

- We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.

- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) is one of the sites where we can generate a secret key for our django project
- Create a new key and copy the key
- Create a new config var with the key SECRET KEY in the Heroku settings.

- Update the SECRET_KEY in the settings.py

    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
- Update the debug variable to true if in development

        DEBUG = 'DEVELOPMENT' in os.environ

- Save, add, commit and push these changes.

### Setting up AWS

- Sign up or login to your aws [amazon account](https://aws.amazon.com/) on the top right by using the manage my account button
- Then navigate to S3 to create a new bucket. This bucket will store our project files.
- Select the closest region to you.
- Selecting ACLs enabled and then bucket owner preferred are required in the object ownership section.
- Uncheck the block public access box in the block public access section
- Tick the acknowledge button to make the bucket public. Then click create bucket.

- Select the properties tab from the bucket you just created
- Find the static web hosting section and choose enable static web hosting.
- Enter index.html and error.html for the index and error documents
- Open the permissions tab and copy the ARN (amazon resource name).
- Go to the bucket policy section, select Edit, and then choose Policy Generator.
- The policy type will be S3 bucket policy, we want to allow all principles by adding * to the input and the actions will be get object.
- Click "add statement" after pasting the ARN we copied from the previous page into the ARN input.
- Click generate policy and copy the policy that displays in a new pop up.
- Paste this policy into the bucket policy editor and make the following changes: Add a /* at the end of the resource value. Click save.
-  Edit the the cross-origin resource sharing (CORS) and paste in the following text:

        [
            {
                "AllowedHeaders": [
                    "Authorization"
                ],
                "AllowedMethods": [
                    "GET"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": []
            }
        ]
- Edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

### Creating AWS groups, policies and users

- To manage access to AWS services, go to IAM by clicking the services icon in the top right corner of the page. Click User Groups from the left-hand navigation menu, and then click the Create Group button in the top-right corner. This will establish the group in which our user will be included. 

- Choose a name for your group and click the create policy button on the right. This will open a new page.

- To import managed policy, click the link in the top right corner of the page after selecting the JSON tab.

- Search for S3 and select the one called AmazonS3FullAccess, then click import.
- To make a change to the resources, we need to make resources an array and then change the value for the resources. Instead of a * which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with /* at the end. This permits all operations on our bucket and all of its resources.

- Click the next: tags button and then the next - review

- Give the policy a name and description (e.g. ajk-furniture-policy | Access to S3 bucket for seaside sewing static files.) Click the create policy button.

- To attach policy click User Groups from the left-hand navigation menu, select the group, and then select the Permissions tab.

- Select "attach policies" from the dropdown menu after clicking the add permissions button on the right.

- Select the policy you just created and then click add permissions at the bottom.

- Create a user for the group by clicking on the user link in the left hand navigation menu.

- Click the add users button on the top right and giving our user a username (e.g. ajk-furniture-staticfiles). 

- Select programmatic access and then click the next: permissions button.

- Add the user to the group you just created and then click next:tags button, next:review button and then create user button.

- As we need to insert the user access key and secret access key into the Heroku config vars, you will now need to download the CSV file. You won't be able to view the CSV again, so be sure to download it now.

### Connecting Django to our S3 bucket

- Install boto3 and django storages 

        pip3 install boto3
        pip3 install django-storages

- freeze them to the requirements.txt file

        pip3 freeze > requirements.txt

- Add storages to the installed apps in settings.py

- Add the following code in settings.py to use our bucket

        if 'USE_AWS' in os.environ:
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=9460800',
            }
            
            AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
            AWS_S3_REGION_NAME = 'enter the region you selected here'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

- We can now add these keys to our configuration variables in Heroku:

    | KEY                       | VALUE         |
    | -------------             | ------------- |
    | `AWS_ACCESS_KEY_ID`       | Paste: The access key value from the amazon csv file downloaded in the last section         |
    | `AWS_SECRET_ACCESS_KEY`   | Paste: The secret access key from the amazon csv file downloaded in the last section         |
    | `USE_AWS`                 | True         |

- Remove the DISABLE_COLLECTSTATIC variable.

- Create a file called custom_storages.py in the root directory.
- import settings and S3Botot3Storage. Create a custom class for static files and one for media files.

- Add the following code to file you created just now

        """ Custom storages for AWS file storage. """
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

- In order to override the static and media URLs in production and update the app where to put static and media assets, add the following to settings.py.

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

- Save everything, add, commit and push these changes to make a deployment to Heroku.

- Navigate to S3 and open your bucket. 
- Click the create folder button on the top right and naming the folder media. This is where we will save all out media files.

### Stripe Setup

- Log into Stripe, click developers and then API keys.
- Copy the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) 
- Log in to heroku and create 2 new variables in Heroku's config vars, publishable key is STRIPE_PUBLIC_KEY and the secret key is STRIPE_SECRET_KEY and paste values copied from stripe
- To add webhooks go to the WebHooks link in the menu on the left and select the add endpoint option.
- Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.
- add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
- Paste the following code in settings.py


        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
        STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

## To fork a repository

- Log in to [github](https://github.com/)
- Navigate to the repository for this project [andrew-kennedy](https://github.com/andyk8872/p5-ecommerce)
- Click on the fork button which can be found on the top right of the page.
- Click the button to create a copy of the original repository

## To clone a repository
The following steps can be used to run the project locally:
- Log in to [github](https://github.com/)
- Navigate to the repository for this project [andrew-kennedy](https://github.com/andyk8872/p5-ecommerce)
- Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.
- Change the current working directory to the place you want to use for the cloned repository by opening the terminal in your preferred IDE.
- In terminal type `git clone` followed by the link you copied earlier.
- All the packages listed in the requirements will need to be installed:

        pip install -r requirements.txt