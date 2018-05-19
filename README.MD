# Micro blog

This website follows along to the [Miguel Grinberg's blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to create a micro blogging website.

* To view the site click this [link](https://flask-microblog-98865.herokuapp.com) to the heroku version of the website
* I also have a version running on my on a digital ocean droplet [here](206.189.150.252)

## Components of the website

* Microsoft Translator (API)
* Elasticsearch (API) - to host this site for free i have removed the search component from deployment.
* SQLAlchemy used as an ORM to switch between databases:
  * Heroku Postrgress on the heroku deployment
  * SQLlite when deployed to my personal server
* Flask with a Blueprint architecture

## Running the Program on local machine

* set FLASK_APP=microblog.py (export = set for linux)
* set MS_TRANSLATOR_KEY=<paste-your-key-here>
    * see https://portal.azure.com to get a MS translator API.
* flask run

### Translations

> (venv) $ flask translate update

edit the messages.po files in each language repository to include the translations for these new tests

To publish the new translations, they need to be compiled:

> (venv) $ flask translate compile

## debugging

> set FLASK_DEBUG=True

## to do

* flask admin for admin pannel

## flask vs django vs ruby
* +ve doesnt lock you into to how you access dbs
* -ve less out of the box in flask
* -ve django more popular -> more docs

## docker image
* docker build -t microblog:latest .
  * need to re build container each time a change is made before running.
* docker images
* docker run --name microblog -d -p 8000:5000 --rm microblog:latest
  * -d = run container in background
  * -p host computer:inside container
  * -rm delete container once terminated

To Set up the DB (dont forget to choose a password)
> docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog \
    -e MYSQL_PASSWORD=<database-password> \
    mysql/mysql-server:5.7

Then once db running then re build docker image
> docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    microblog:latest


docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog -e MYSQL_PASSWORD=<password> mysql/mysql-server:5.7

Note removed e mail stuff:
docker run --name microblog -d -p 8000:5000 --rm --link mysql:dbserver -e DATABASE_URL=mysql+pymysql://microblog:<password>@dbserver/microblog microblog:latest
