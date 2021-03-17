# Contribute Instructions

[Back](./)

## First, Fork This Repo by clicking here [![GitHub](https://img.shields.io/github/forks/Christopher-MakeSchool/django-on-docker.svg?style=flat-square)](https://github.com/Christopher-MakeSchool/django-on-docker/fork).

## Second, Clone your version for local dovelopment

```zsh
$ git clone https://github.com/YourUserName/django-on-docker.git
```

## Third, Create a new branch starting with your username

```zsh
$ git checkout -b ChrisBarnes2000
or
$ gco -b ChrisBarnes2000
```

## Fourth, Configure Your Local Environment

1. Rename `.env-sample` to `.env.dev` & `.env-db-sample` to `.env-db`.
2. Update the variables in these files (ask team lead for new values).
3. Run Locally, by Building the images to run the containers

```zsh
$ docker-compose up -d --build
```

Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Stop The Local Server

```zsh
$ docker-compose down
```

## Fifth, Make Modificaitons on your new branch

#### Remember to Document your Changes.

### Command Short Cuts used below

| Description             | Short Cut | Regular             |
| ----------------------- | --------- | ------------------- |
| Add all changes         | ga .      | git add .           |
| checkout branch         | gco       | git checkout        |
| checkout master branch  | gcm       | git checkout master |
| merge changes to master | gm        | git merge Branch    |
| push to origin          | gp        | git push            |

## Local Branch Development

1. Create/Switch to branch and work on it there..

    ```zsh
    $ gco <Branch-Name>
    ```

2. Edit Stuff and Test locally

3. add, commit, & Push to that branch

    Use tags when committing ```ga .;gcmsg "[function] description"```

    - [Add]: File or Function XYZ
    - [Fix]: Typo or Function or explaination, etc
    - [Pull]: From Whom or What Branch For What Reason
    - [Refactor]: File or Function XYZ For Reason LMNOP
    - [Remove]: File or Function XYZ For Reason LMNOP
    - [Update]: File or Function XYZ For Reason LMNOP

    ```zsh
    $ git push origin <Branch-Name>
    ```

4. Switch to master

    ```zsh
    $ gcm
    or 
    $ git checkout master
    ```

5. Merge with master

    ```sh
    $ gm <Branch-Name>
    or
    $ git merge <Branch-Name>
    ```

6. Push

    ```sh
    $ gp
    or
    $ git push
    ```

Repeat branching and update your team and progress tracker
