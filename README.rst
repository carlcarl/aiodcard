aiodcard
==============

.. image:: https://badge.fury.io/py/aiodcard.svg
    :target: http://badge.fury.io/py/aiodcard
.. image:: https://travis-ci.org/carlcarl/aiodcard.svg?branch=master
    :target: https://travis-ci.org/carlcarl/aiodcard
.. image:: https://coveralls.io/repos/carlcarl/aiodcard/badge.svg?branch=master&service=github :target: https://coveralls.io/github/carlcarl/aiodcard?branch=master

Dcard crawler using asyncio(coroutine)

Feature
-------
| Get article list and content using coroutine


Dependencies
------------
* Python 3.3 and :mod:`asyncio` or Python 3.4+
* aiohttp


Installation
------------
::

	python setup.py install

or 

::

    pip install aiodcard


Example
-------


.. code:: python

    import asyncio

    import aiohttp
    import aiodcard

    @asyncio.coroutine
    def get_funny_articles():
        session = aiohttp.ClientSession()
        forum_name = 'funny'
        page_index = 1
        result = yield from aiodcard.get_articles_of_page(session, forum_name, page_index)
        print(result)

    def main():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(get_funny_articles())

    if __name__ == '__main__':
        main()

  

Authors and License
-------------------
The ``aiodcard`` package is written by Chien-Wei Huang. It’s MIT licensed and freely available.

Feel free to improve this package and send a pull request to GitHub.

