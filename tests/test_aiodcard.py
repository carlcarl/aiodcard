#!/usr/bin/env python

import aiohttp
import pytest

import aiodcard


def test_get_direct_image_url_chnaged():
    image_url = 'http://imgur.com/aaaaa'
    direct_image_url = aiodcard.get_direct_image_url(image_url)
    assert direct_image_url == 'http://i.imgur.com/aaaaa.png'


def test_get_direct_image_url_unchnaged():
    image_url = 'http://test.com/test.jpg'
    direct_image_url = aiodcard.get_direct_image_url(image_url)
    assert direct_image_url == image_url


def test_find_image_urls_multiple():
    article_json = {
        'version': [
            {
                'content': 'test http://xxxx.com/aaa.jpg end, another: http://xxxx.com/bbb.jpg'
            }
        ]
    }
    image_urls = aiodcard.find_image_urls(article_json)
    assert image_urls[0] == 'http://xxxx.com/aaa.jpg' and image_urls[1] == 'http://xxxx.com/bbb.jpg'


def test_find_image_urls_multiple_mixed():
    article_json = {
        'version': [
            {
                'content': 'test http://xxxx.com/aaa.jpg end, another: http://imgur.com/aaaaa'
            }
        ]
    }
    image_urls = aiodcard.find_image_urls(article_json)
    assert image_urls[0] == 'http://xxxx.com/aaa.jpg' and image_urls[1] == 'http://imgur.com/aaaaa'


def test_find_image_urls_none():
    article_json = {
        'version': [
            {
                'content': 'test this url: http://www.google.com'
            }
        ]
    }
    image_urls = aiodcard.find_image_urls(article_json)
    assert image_urls == []


@pytest.mark.asyncio
def test_download_image():
    import os
    session = aiohttp.ClientSession()
    image_url = 'http://i.imgur.com/3Tsokox.jpg'
    image_folder = '.'
    image_name = 'test.jpg'
    result = yield from aiodcard.download_image(session, image_url, image_folder, image_name)
    assert result['result'] == 0

    statinfo = os.stat(os.path.join(image_folder, image_name))
    session.close()
    assert statinfo.st_size == 457612
    os.remove(os.path.join(image_folder, image_name))


@pytest.mark.asyncio
def test_download_image_none():
    session = aiohttp.ClientSession()
    image_url = 'http://i.imgur.com/0d4I9Pz.jp'
    image_folder = '.'
    image_name = 'test.jpg'
    result = yield from aiodcard.download_image(session, image_url, image_folder, image_name)
    session.close()
    assert result['result'] == -1


@pytest.mark.asyncio
def test_get_articles_of_page_success():
    session = aiohttp.ClientSession()
    forum_name = 'funny'
    page_index = 1
    result = yield from aiodcard.get_articles_of_page(session, forum_name, page_index)
    session.close()
    assert result != []


@pytest.mark.asyncio
def test_get_articles_of_page_fail():
    session = aiohttp.ClientSession()
    forum_name = 'funny'
    page_index = -1
    result = yield from aiodcard.get_articles_of_page(session, forum_name, page_index)
    session.close()
    assert result == []


@pytest.mark.asyncio
def test_get_article_successs():
    session = aiohttp.ClientSession()
    article_id = '388072'
    result = yield from aiodcard.get_article(session, article_id)
    session.close()
    assert result != {}


@pytest.mark.asyncio
def test_get_article_fail():
    session = aiohttp.ClientSession()
    article_id = '1'
    result = yield from aiodcard.get_article(session, article_id)
    session.close()
    assert result == {}
