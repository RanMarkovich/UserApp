## About the project:

This is a full stack automation project that tests both UI and API of a demo flask application for a user registration and login flows.

## About the application:

Written mostly in Python - The application contains two web-services:
    
* **user-service**: handles the frontend requests and integrates with sql database for user data registration and login.
* **user-app**: serves the html pages for registration and login, to send the user data to the user-service.

## About the CI Infrastructure:

Using the Jenkins multibranch-pipeline, whenever a new remote branch is created (git push), the jenkins server receives a git webhook to initialize a build which would then build, run and test the application.

a sample of a successful run:
![img.png](img.png)

The build status is reflected in the PR, like so:
![img_1.png](img_1.png)