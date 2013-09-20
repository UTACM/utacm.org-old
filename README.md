## Contributing

Contributions are more than welcome. Feel free to fork the [repo and submit pull
requests](https://help.github.com/articles/using-pull-requests).

## Building Site Locally

Here are the steps to building the site locally:

1. clone this repo

        git clone https://github.com/UTACM/utacm.org.git
        cd utacm.org

2. install `virtualenvwrapper`

        sudo pip install -g virtualenvwrapper

    Add the requisite hooks to your `.bashrc`.

3. create a virtualenv for this project

        mkvirtualenv utacm
        workon utacm

4. install the required Python modules

        pip install -r requirements.txt

5. start development server

        make devserver

    You can now visit the site at [http://localhost:8000](http://localhost:8000).

6. to stop the development server

        ./develop_server.sh stop

If you have any questions check the [documentation][doc] or open up an issue.

[doc]: http://docs.getpelican.com/en/3.2/index.html
