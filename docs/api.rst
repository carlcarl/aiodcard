
====================
 Core API Reference
====================


Crawl
=====

.. function:: get_articles_of_page(session, forum_name, page_index)

    Get articles of a page on the specific forum 

    :param aiohttp.client.ClientSession session: HTTP(s) connect session

    :param string forum_name: forum name(ex: funny)

    :param int page_index: the page of the forum

    :returns: a list of article json response
    :rtype: list


.. function:: get_article(session, article_id)

    Get the article json according to the ``article_id``

    :param aiohttp.client.ClientSession session: HTTP(s) connect session

    :param int article_id: article ID

    :returns: article json response
    :rtype: dict


Image
=====

.. function:: find_image_urls(article_json)

    Get image urls in the ``artciel_json`` response

    :param dict article_json: article json response

    :returns: a list of image urls
    :rtype: list


.. function:: get_direct_image_url(image_url) 

    Transfer image html url to the direct image url,
    ex: ``https://imgur.com/aaaaa`` to ``https://i.imgur.com/aaaaa.png``

    :param string image_url: the image url

    :returns: the direct image url
    :rtype: string


.. function:: def download_image(session, image_url, image_folder, image_name)

    Download image to the ``image_folder`` with the ``image_name``

    Example of returns:

    ::

        {
            'func_name': 'download_image',
            'result': 0 # 0 success, -1 error,
            'image_url': 'http://xxx.png',
            'image_folder': '/tmp',
            'image_name': 'yyy.png',
        }

    :param aiohttp.client.ClientSession session: HTTP(s) connect session

    :param string image_url: the image url you want download

    :param string image_folder: the folder you want to put your image, should be absolute path 

    :param string image_name: the name of the image you want

    :returns: a dict include result, function name and arguments of download_image
    :rtype: dict
