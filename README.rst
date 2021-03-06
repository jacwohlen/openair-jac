===============================
OpenAir 2018 Registration
===============================

Dedicated app to JAC Wohlen to run the registration for the OpenAir Event 2018

Its everything other than lovely... and hardcoded. I might invest some time later to
make it generic and usable for other purposes.

Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export OPENAIR_SECRET='something-really-secret'

Run the following commands to bootstrap your environment ::

    git clone https://github.com/kraeki/openair
    cd openair
    pip install -r requirements/dev.txt
    npm install
    npm start  # run the webpack dev server and flask server using concurrently

You will see a pretty welcome screen.

In general, before running shell commands, set the ``FLASK_APP`` and
``FLASK_DEBUG`` environment variables ::

    export FLASK_APP=autoapp.py
    export FLASK_DEBUG=1

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    npm start



Deployment
----------

To deploy::

    export FLASK_DEBUG=0
    npm run build   # build assets with webpack
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.

Deployment via Docker
---------------------

.. code-block:: bash

    docker-compose -f docker/docker-compose.yml build -d
    docker-compose -f docker/docker-compose.yml up -d

    # Setup Database (fresh)
    docker-compose -f docker/docker-compose.yml flask db upgrade

    # Otherwise load initial script from e.g. backup.sql
    copy sql script to docker/db/create.sql

    # Backup
    docker exec -it docker_web-db_1 pg_dump --username postgres --no-password > "backup_$(date +"%s").sql"

Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.


Asset Management
----------------

Files placed inside the ``assets`` directory and its subdirectories
(excluding ``js`` and ``css``) will be copied by webpack's
``file-loader`` into the ``static/build`` directory, with hashes of
their contents appended to their names.  For instance, if you have the
file ``assets/img/favicon.ico``, this will get copied into something
like
``static/build/img/favicon.fec40b1d14528bf9179da3b6b78079ad.ico``.
You can then put this line into your header::

    <link rel="shortcut icon" href="{{asset_url_for('img/favicon.ico') }}">

to refer to it inside your HTML page.  If all of your static files are
managed this way, then their filenames will change whenever their
contents do, and you can ask Flask to tell web browsers that they
should cache all your assets forever by including the following line
in your ``settings.py``::

    SEND_FILE_MAX_AGE_DEFAULT = 31556926  # one year
