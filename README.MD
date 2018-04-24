## Running the Program

* set FLASK_APP=microblog.py (export = set for linux)
* set MS_TRANSLATOR_KEY=<paste-your-key-here>
    * see https://portal.azure.com
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