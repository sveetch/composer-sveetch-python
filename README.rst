.. _Python: https://www.python.org/
.. _Project composer: https://github.com/sveetch/project-composer
.. _virtualenv: https://virtualenv.pypa.io/
.. _pip: https://pip.pypa.io/


=======================
Composer Sveetch Python
=======================

A basic Python project sample with `Project composer`_ from its tutorial documentation
on a basic sample usage.


Dependencies
************

* `Python`_>=3.8;
* `Project composer`_>=0.5.0;
* `virtualenv`_;
* `pip`_;


Install
*******

Just use the makefile action: ::

    make install

If you don't have Makefile available on your system or you want to use something else
than virtualenv or pip, you should easily be able to install it yourself. This is just
about to setup a virtual Python environment for the project and then install the
composer package in it.

Usage
*****

Use the Python interpreter from your virtual environment to execute the ``hello.py``
script: ::

    source .venv/bin/activate
    python hello.py
