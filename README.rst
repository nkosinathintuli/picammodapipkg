==============
picammodapipkg
==============


.. image:: https://img.shields.io/pypi/v/picammodapipkg.svg
        :target: https://pypi.python.org/pypi/picammodapipkg

.. image:: https://img.shields.io/travis/nkosinathintuli/picammodapipkg.svg
        :target: https://travis-ci.com/nkosinathintuli/picammodapipkg

.. image:: https://readthedocs.org/projects/picammodapipkg/badge/?version=latest
        :target: https://picammodapipkg.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: MIT license
* Documentation: https://picammodapipkg.readthedocs.io.


Features
--------

This package contains an API and a demonstrator application using the API. Instructions on how to install the package can be found in the documentation link above.

API:

* Has the ability to do motion detection.
* Has the ability to capture capture a video of fixed time length.
* Has the ability to capture a video based on light intensity.
* Has the ability to capture an image and save it on system storage.

Demonstrator:

* Uses a web application to enable/disable motion detection, start/stop a video recording and enable/disable a light triggered recording all on button press.
* Contains camproject and motion_detector modules run independantly for the video recording functions and enabling motion detection respectively.
* To use the demonstrator run each module first before using the buttons oof the web application
* The URL of the web application can be found here: https://pi-cam-surveillance.anvil.app/

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
