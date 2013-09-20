## Contributing

Contributions are more than welcome. Feel free to fork the [repo and submit pull
requests][pr].

To add a blog post or edit one of the pages, please check the `content/` folder.
All files are written in [Markdown][md] format.

#### Adding A Blog Post

Create a [Markdown][md] file in the `content/` folder. Any filename is
acceptable, but please use `YYYYMMDD_title.md`.

Within the text file, fill in some basic metadata:

    Title: LAN Party!
    Date: 2013-09-20
    Category: social
    Tags: lan, party
    Slug: fall-lan-party
    Author: Kim Phung Tran
    Summary: Start the new year with a LAN Party!

    Welcome back from your (hopefully) great summer! And ...

Afterwards submit a [pull request][pr] and someone will comment or merge it in
to the website shortly.

#### Adding A Static Page

Do the same thing as a blog post except create the file in `content/pages/`
folder.

At the moment you need to modify `themes/utacm/utacm/templates/base.html` to
manually add the page link to the navigation bar.

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
[md]: https://daringfireball.net/projects/markdown/basics
[pr]: https://help.github.com/articles/using-pull-requests
