# Contribute Instructions
[Back](./)

## To Get Started Learn the [Difference Between Clone and Fork](https://www.toolsqa.com/git/difference-between-git-clone-and-git-fork/)

Then clone and modify these files
```sh
$ git clone https://github.com/ChrisBarnes7404/Repo-Name.git
```

1. Rename `*.env.dev-sample*` to `*.env.development*`.
2. Update the environment variables (ask team lead for new values) in the `*docker-compose.yml*` and `*.env.dev* files`.
3. Build the images and run the containers:

Command Short Cuts used below
| Description               | Short Cut |       Regular       |
| ------------------------- | --------- | ------------------- |
| Add all changes           |  ga .     | git add .           |
| checkout branch           |  gco      | git checkout        |
| checkout master branch    |  gcm      | git checkout master |
| merge changes to master   |  gm       | git merge Branch    |
| push to origin            |  gp       | git push            |


# Development

### Run Locally
```sh
$ docker-compose up -d --build
```

Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Stop The Local Server
```sh
$ docker-compose down
```

# Branching

1. Create/Switch to branch and work on it there.. 
    ```sh
    $ gco FrontEnd
    ```

2. Edit Stuff and Test locally

3. add, commit, & Push to that branch 
    ```sh
    $ git push origin FrontEnd/Development/Fixes
    ```

4. Switch to master
    ```sh
    $ gcm
    ```
5. Merge with master
    ```sh
    $ gm FrontEnd/Development/Fixes
    ```
3. Push
    ```sh
    $ gp
    ```

Repeat branching and update your team and progress tracker


<!-- # Production

Uses gunicorn + nginx.

1. Rename `*.env.prod-sample*` to `*.env.production*` and `*.env.prod.db-sample*` to `*.env.prod.db*`. Update the environment variables (again ask team lead).
2. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

### Stop The Server
```sh
$ docker-compose down
``` -->

## Other Docker [Commands](Docs/Docker-comands.md)
