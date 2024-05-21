# BrainBox API

The BrainBox API, built on Django Rest Framework, serves as the backend for the BrainBox project, a note-taking web application. It forms the foundation of the BrainBox platform, empowering users to organize and manage their notes efficiently.

## Agile Methodology

I've adopted Agile methodology for project planning, utilizing GitHub Projects as the primary tool. Within the [project](https://github.com/users/elindalenback/projects/7), I've organized work into user stories. Each user story includes a title, description, acceptance criteria, and tags to prioritize features as "must-have", "should-have", and "could-have". The workflow progresses from "To Do" to "In Progress" while actively working on user stories and finally to "Done" upon completion.

### Comments

**User Story #1:**
As a user, I can comment on posts or content so that I can share my thoughts and engage with other users.

**Acceptance Criteria:**
- AC1: There should be an option to add a comment below a post or piece of content.
- AC2: Users should be able to view existing comments on a post.
- AC3: The application should allow users to edit and delete their own comments.
- AC4: Comments should display the commenter's username and timestamp.

### Followers

**User Story #2:**
As a user, I can follow other users so that I can stay updated with their activities and content.

**Acceptance Criteria:**
- AC1: There should be a 'Follow' button to follow user profiles.
- AC2: Users should be able to see content from their followed profiles.
- AC3: The application should allow users to unfollow others.

### Likes

**User Story #3:**
As a user, I can like notes or content so that I can show appreciation or agreement.

**Acceptance Criteria:**
- AC1: There should be a 'Like' button below each post or piece of content.
- AC2: The application should display the total number of likes for each post.
- AC3: Users should be able to unlike a post if they change their mind and the likes count should then remove that in the likes count.

### Notes

**User Story #4:**
As a user, I can create and edit notes so that I can jot down and manage my ideas or information.

**Acceptance Criteria:**
- AC1: There should be an option to create a new note.
- AC2: Users should be able to edit or delete their own notes.
- AC3: Notes should have a title, content, and date of creation.

### Polls

**User Story #5:**
As a user, I can create and participate in polls so that I can gather opinions or preferences.

**Acceptance Criteria:**
- AC1: There should be an option to create a new poll.
- AC2: Users should be able to vote on polls.
- AC3: The application should display poll results in real-time.

### Profiles

**User Story #6:**
As a user, I can view and edit my profile so that I can manage my personal information and settings.

**Acceptance Criteria:**
- AC1: There should be a 'Profile' section accessible from the main menu.
- AC2: Users should be able to edit their profile details and upload a profile picture.
- AC3: The application should display user profiles with relevant information.
- AC4: Users should be able to view other users' profiles.

### Tags

**User Story #7:**
As a user, I can tag posts or content so that I can easily search and categorize related content.

**Acceptance Criteria:**
- AC1: There should be an option to add tags when creating or editing a note.
- AC2: Users should be able to search for tag-related notes.
- AC3: The application should allow users to add multiple tags to a single note or content.

### Reports

**User Story #8:**
As a user, I can report notes or content to administrators, so that inappropriate or spam content can be managed effectively.

**Acceptance Criteria:**
- AC1: Users should have the option to report a note by selecting a reason from a predefined list (e.g., spam, inappropriate content, other) when viewing a note.
- AC2: The application should display a form for users to provide additional description or context when reporting a note.
- AC3: Upon reporting a note, the system should capture the reporting user's information and timestamp the report creation.
- AC4: Administrators should be able to view a list of reported notes, along with the reasons and descriptions provided by users.
- AC5: Administrators should have the ability to take appropriate actions (e.g., delete, hide) based on the reported notes and reasons provided.
- AC6: Users should receive feedback upon reporting a note, confirming that their report has been submitted successfully.

### Notebooks

**User Story #9:**
As a user, I can create and organize notebooks, so that I can manage my notes efficiently.

**Acceptance Criteria:**
- AC1: Users should have the ability to create a new notebook by providing a name for the notebook.
- AC2: Upon creation, each notebook should be associated with the user who created it.
- AC3: The application should allow users to upload a custom image for the notebook's folder, which will serve as its visual representation.
- AC4: If a custom image is not provided, the application should display a default image for the notebook's folder.
- AC5: Users should be able to view a list of their notebooks, along with their associated names and folder images, in the user interface.
- AC6: Users should have the ability to delete or edit their notebooks, including updating the name and folder image.
- AC7: The application should enforce data integrity by ensuring that each notebook has a unique name for each user.

## Features

1. **User Commenting**
   - Enable users to comment on posts or content.
   - Implement functionalities to add, view, edit, and delete comments.
   - Display commenter's username and timestamp for each comment.

2. **User Following**
   - Allow users to follow other users.
   - Enable users to view content from followed profiles.
   - Implement functionalities for users to unfollow others.

3. **Content Liking**
   - Enable users to like notes or content.
   - Show the total number of likes for each post.
   - Allow users to unlike a post and update the likes count accordingly.

4. **Note Management**
   - Enable users to create and edit notes.
   - Implement functionalities to add, edit, and delete notes.
   - Include fields for note title, content, and date of creation.

5. **Poll Creation and Participation**
   - Allow users to create and participate in polls.
   - Provide options to create new polls and vote on existing ones.
   - Display poll results in real-time.

6. **User Profile Management**
   - User Registration and Authentication: Allows users to create accounts, log in and log out to access personalized features.
   - Implement functionalities for users to edit profile details and upload profile pictures.

7. **Content Tagging**
   - Allow users to tag notes or content for categorization and searchability.
   - Implement options to add tags when creating or editing a note.
   - Enable users to search for tag-related notes.

8. **Content Reporting**
   - Allow users to report notes or content to administrators.
   - Provide predefined reasons for reporting (e.g., spam, inappropriate content).
   - Capture reporting user's information and timestamp the report creation.
   - Enable administrators to view reported notes and take appropriate actions.


### Future Features

9. **Notebook Creation and Organization (Future Feature)**
   - Introduce a feature for users to create and organize notebooks.
   - Enable users to create new notebooks, associate them with their accounts, and upload custom images for visual representation.
   - Provide functionalities to view, delete, and edit notebooks, ensuring data integrity.


## Database Design

The application utilizes a relational database structured around Django models. The relationships between these models are depicted in the Entity-Relationship Diagram (ERD):

![ERD](docs/readme_images/brainbox-erd.png)

- **Profile**: Represents user profiles containing additional information like display name, avatar, occupation, bio, and an image. Each profile is linked to a corresponding user account through a one-to-one relationship.

- **Notebook**: Stores information about notebooks created by users, including the notebook name and a folder image. Each notebook is associated with a user account through a foreign key relationship.

- **Note**: Represents user-generated notes with fields for title, content, creation date, and last update date. It includes a foreign key to the User model for ownership and a many-to-many relationship with the Tag model for categorization. Additionally, notes can optionally be linked to a notebook through a foreign key relationship.

- **Comment**: Manages comments on notes, linking back to the User who made the comment and the note being commented on.

- **Like**: Tracks user interactions such as liking notes. It's linked to both the User who liked the note and the note being liked.

- **Follower**: Manages user interactions for following other users. It establishes a relationship between the user who is following (owner) and the user who is being followed (followed). This model enables users to track relationships and stay updated on content from other users they follow.

- **Report**: Handles the reporting of content, whether it be notes. It's associated with the User who reported the note and the note being reported.

- **Tag**: Used for categorizing notes, featuring a simple model with just a name for each tag. It establishes a many-to-many relationship with the Note model.

## Testing

All endpoints underwent manual testing during the development phase by accessing the URLs directly. The API was rigorously evaluated through various request types (GET, POST, PUT, DELETE) both during development and in the production environment, as initiated from the Front End Application.

### Python Linter (PEP 8)

Only the files containing custom Python code were subjected to testing:

- In settings.py, one instance of the 'E501 line too long' error were identified. In this specific cases, it was deemed acceptable not to break the line.
- For all other files, the result was *"All clear, no errors found".*

### Testing using Postman

### Profiles
| Element                    | Action     | Expected Result                                                    | Pass/Fail |
|----------------------------|------------|--------------------------------------------------------------------|-----------|
| /profiles/                 | GET        | Data displayed as a list of profiles                               | Pass      |
| /profiles/<int:pk>/        | DELETE     | The deleted profile is removed from the list of data               | Pass      |
| /profiles/<int:pk>/        | PUT        | Successfully update/change the profiles information                | Pass      |
| /profiles/<int:pk>/        | GET        | Displays a specific profile's data                                 | Pass      |
| dj-rest-auth/registration/ | POST       | Register a new user                                                | Pass      |
| dj-rest-auth/              | GET        | Log in as a registered user                                        | Pass      |
| dj-rest-auth/logout/       | GET        | Log out as a registered user                                       | Pass      |

### Likes
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /likes/               | GET        | Data displayed as a list of likes                                  | Pass      |
| /likes/<int:pk>/      | DELETE     | The deleted like is removed from the list of data                  | Pass      |
| /likes/               | POST       | Create a new like and adds the like to the list of likes           | Pass      |
| /likes/<int:pk>/      | GET        | Displays a specific like's data                                    | Pass      |

### Comments
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /comments/            | GET        | Data displayed as a list of comments                               | Pass      |
| /comments/<int:pk>/   | DELETE     | The deleted comment is removed from the list of data               | Pass      |
| /comments/            | POST       | Successfully create a new comment, the comment is added to the list of data  | Pass      |
| /comments/<int:pk>/   | PUT        | Successfully update/change the comment's details                   | Pass      |
| /comments/<int:pk>/   | GET        | Displays a specific comment's data                                 | Pass      |

### Posts
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /posts/               | GET        | Data displayed as a list of posts                                  | Pass      |
| /posts/               | POST       | Successfully create a new post, the post is added to the list of data  | Pass      |
| /posts/<int:pk>/      | DELETE     | The deleted post is removed from the list of data                  | Pass      |
| /posts/<int:pk>/      | PUT        | Successfully update/change the post's details                      | Pass      |
| /posts/<int:pk>/      | GET        | Displays a specific post's data                                    | Pass      |

### Followers
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /followers/           | GET        | Data displayed as a list of followers                              | Pass      |
| /followers/           | POST       | Successfully create a new follower, the follower is added to the list of data | Pass      |
| /followers/<int:pk>/  | GET        | Displays a specific follower's data                                | Pass      |
| /followers/<int:pk>/  | DELETE     | The deleted follower is removed from the list of data              | Pass      |

### Polls

#### Questions
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /questions/           | GET        | Data displayed as a list of questions                              | Pass      |
| /questions/           | POST       | Successfully create a new question, the question is added to the list of data | Pass      |
| /questions/<int:pk>/  | DELETE     | The deleted question is removed from the list of data              | Pass      |
| /questions/<int:pk>/  | PUT        | Successfully update/change the question's details                  | Pass      |
| /questions/<int:pk>/  | GET        | Displays a specific question's data                                | Pass      |

#### Choices
| Element                            | Action     | Expected Result                                                              | Pass/Fail |
|------------------------------------|------------|------------------------------------------------------------------------------|-----------|
| /questions/<int:question_id>/choices/ | GET      | Data displayed as a list of choices for the specified question               | Pass      |
| /questions/<int:question_id>/choices/ | POST     | Successfully create a new choice for the specified question, added to the list of choices | Pass      |
| /questions/<int:question_id>/choices/<int:pk>/ | DELETE | The deleted choice for the specified question is removed from the list of choices | Pass      |
| /questions/<int:question_id>/choices/<int:pk>/ | PUT    | Successfully update/change the choice's details for the specified question | Pass      |
| /questions/<int:question_id>/choices/<int:pk>/ | GET    | Displays a specific choice's data for the specified question               | Pass      |

### Tags
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /tags/                | GET        | Data displayed as a list of tags                                   | Pass      |
| /tags/                | POST       | Successfully create a new tag, the tag is added to the list of data | Pass      |
| /tags/<int:pk>        | DELETE     | The deleted tag is removed from the list of data                   | Pass      |
| /tags/<int:pk>        | GET        | Displays a specific tag's data                                     | Pass      |

### Reports
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| /reports/             | GET        | Data displayed as a list of reports                                | Pass      |
| /reports/             | POST       | Successfully create a new report, the report is added to the list of data | Pass      |
| /reports/<int:pk>/    | DELETE     | The deleted report is removed from the list of data                | Pass      |
| /reports/<int:pk>/    | PUT        | Successfully update/change the report's details                    | Pass      |
| /reports/<int:pk>/    | GET        | Displays a specific report's data                                  | Pass      |

## Technologies used

The project is developed in Python.

### Frameworks

- Django and Django REST Framework for creating the web API.

### Libraries and Packages

- Gunicorn for handling web requests.
- dj-database-url for configuring database management.
- django-cors-headers for managing server headers required for Cross-Origin Resource Sharing (CORS).
- django-filter for allowing users to filter querysets dynamically.
- Pillow for image processing.
- psycopg2 as an adapter used for database connectivity.
- PyJWT for encoding and decoding JSON Web Tokens (JWT).
- Django Allauth and Dj-Rest-Auth for handling user authentication, registration, and account management.
- cloudinary for managing media assets.

### Database

- ElephantSQL as the PostgreSQL database used in production.

### Hosting

- Heroku for hosting and deploying the application.

### Other Technologies

- Git for version control.
- GitHub for hosting the code.
- Gitpod as the IDE used to develop the website.
- Lucidchart for creating the ERD.

The [requirements.txt](requirements.txt) file specifies the full list of packages and their versions of these packages.

## Deployment

This site has been deployed to Heroku, using ElephantSQL database and Cloudinary, following these steps:

1. **Installing Django and Supporting Libraries**

    - Install Django, Django REST Framework, and Gunicorn: `pip install Django djangorestframework gunicorn`
    - Install supporting database libraries: `pip install dj-database-url psycopg2`
    - Install Cloudinary libraries: `pip install django-cloudinary-storage`
    - Install Pillow: `pip install Pillow`
    - Create requirements.txt: `pip freeze > requirements.txt`
    - Create Django project: `django-admin startproject projectname`
    - Create first app: `python manage.py startapp appname`
    - Add app to installed apps in settings.py file
    - Migrate changes: `python manage.py migrate`
    - Run the server to test if the app is installed: `python manage.py runserver`

2. **Create the Heroku App**
   
    - Log into Heroku and go to the Dashboard
    - Click “New" and then “Create new app”
    - Choose an app name and select the region closest to you. Then, click “Create app” to confirm.

3. **Create an External Database with ElephantSQL**

    - Log into ElephantSQL
    - Click "Create New Instance"
    - Set up a plan by giving a Name and selecting a Plan
    - Click "Select Region" and choose a Data center
    - Click "Review", check all details and click "Create Instance"
    - Return to the Dashboard and click on the database instance name
    - Copy the database URL

4. **Create an env.py File to Avoid Exposing Sensitive Information**

    - In the project workspace, create a file called env.py. Check that the file name is included in the .gitignore file
    - Add `import os` to env.py file and set environment variable DATABASE_URL to the URL copied from ElephantSQL `os.environ["DATABASE_URL"]="<copiedURL>"`
    - Add a SECRET_KEY environment variable `os.environ["SECRET_KEY"]="mysecretkey"`
    - Add CLIENT_ORIGIN and CLIENT_ORIGIN_DEV environment variables as needed.
    
5. **Update settings.py**

    - Add the following code below the path import in `settings.py` to connect the Django project to env.py:
        ```python
        import os
        if os.path.exists("env.py"):
            import env
        ```
    - Remove the secret key provided by Django in settings.py and refer to variable in env.py instead (`SECRET_KEY = os.environ.get('SECRET_KEY')`)
    - Create a new variable called DEV at the top of settings.py to keep using the sqlite database in the development environment and turn Debug on, but off in production, and use the ElephantSQL database:
        ```python
        development = os.environ.get('DEV', False)
        ```
    - To connect to the new database for production and keep sqlite for development, replace the provided DATABASE variable with:
        ```python
        if development:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        ```

6. **Heroku Config Vars**

    - Go back to Heroku dashboard and open the Settings tab
    - Add config vars:
        - DATABASE_URL -> value of the database url
        - SECRET_KEY -> value of the secret key string
        - DISABLE_COLLECTSTATIC -> 1
        - ALLOWED_HOSTS -> value of the deployed Heroku app url
        - Add CLIENT_ORIGIN and CLIENT_ORIGIN_DEV as needed.

7. **Set Up Cloudinary for Static and Media Files Storage**

    - In the Cloudinary dashboard, copy the API Environment variable
    - In `env.py` file, add new variable `os.environ["CLOUDINARY_URL"] = "<copied_variable>"`, without "CLOUDINARY_URL="
    - Add the same variable value as new Heroku config var named CLOUDINARY_URL
    - In `settings.py`, in the INSTALLED_APPS list, above `django.contrib.staticfiles`, add `cloudinary_storage`, and below add `cloudinary`
    - Connect Cloudinary to the Django app in settings.py:
        ```python
        CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        MEDIA_URL = '/media/'
        DEFAULT_SITE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
    - Add Heroku Hostname to ALLOWED_HOSTS:
        ```python
        if development:
            ALLOWED_HOSTS = [os.environ.get('LOCALHOST')]
        else:
            ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]
        ```

8. **Add JWT to the Project**

    - Install `dj-rest-auth` and `dj-rest-auth[with_social]`: `pip install dj-rest-auth dj-rest-auth[with_social]`
    - Add to installed apps in settings.py:
        ```python
        'rest_framework.authtoken',
        'dj_rest_auth',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth.registration',
        ```
    - Install `djangorestframework-simplejwt`: `pip install djangorestframework-simplejwt`
    - Add authentication method to settings.py:
        ```python
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [(
                'rest_framework.authentication.SessionAuthentication'
                if 'DEV' in os.environ
                else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
            )],
        }
        ```
        ```python
        REST_USE_JWT = True
        JWT_AUTH_SECURE = True
        JWT_AUTH_COOKIE = 'my-app-auth'
        JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
        JWT_AUTH_SAMESITE = None
        ```

9. **Create Procfile**

10. **Heroku Deployment**

    - Click Deploy tab in Heroku
    - In the 'Deployment method' section select 'Github' and click 'Connect to Github'
    - In the 'search' field enter the repository name
    - Connect to link the heroku app with the Github repository
    - Click "Deploy Branch" or enable "Automatic Deploys"

## Credits

- The project structure, including project setup and the implementation of the notes, profiles, likes, comments, and followers apps, is based on Code Institute's Django REST Framework project [drf-api](https://github.com/Code-Institute-Solutions/drf-api).
- Deployment steps were adapted from Code Institute's resources.
- The Reports functionality was inspired by Tiago's implementation in his [Connect](https://github.com/TiagoMA90/connect) project. You can find the Reports app for the backend [here](https://github.com/TiagoMA90/drf-api/tree/main/reports).
- The Tags functionality was inspired by Javier's implementation in his [hoodsap](https://github.com/fsjavier/hoodsap-api) project. You can find the Tags app for the backend [here](https://github.com/fsjavier/hoodsap-api/tree/main/tags).
- Special thanks to the tutor support team for their valuable insights and patience.
- Acknowledgments to fellow student Anton Eriksson for collaborative work and troubleshooting efforts. Thank you!
