# User Instructions

## Want to use this project?

(this will make a folder for the project be in the outter folder where you want it placed)
> git clone url

> Navigate into this new folder

> ls (you see requirements.txt and not settings.py)

> touch .env

> Navigate into folder named the same as outer folder

> ls (you see settings.py and not requirements)

> touch local_settings.py

> .. (back to requirements)

> Code . Or open in editor



### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Branching

Create/Switch to branch and work on it there.. 
> (gco/git checkout) FrontEnd

Make and edit and Test locally

add, commit, & Push to that branch 

> git push origin FrontEnd/Development/Fixes

Switch to master, merge, and push 
> (gcm/git checkout master)

> (gm/git merge) FrontEnd/Development/Fixes

> (gp/git push)

Repeat branching and update your team and progress tracker


### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.


## Other Docker [Commands](Docs/Docker-comands.md)