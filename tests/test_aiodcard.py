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
def test_get_articles_of_page_success():
    session = aiohttp.ClientSession()
    forum_name = 'funny'
    page_index = 1
    result = yield from aiodcard.get_articles_of_page(session, forum_name, page_index)
    assert result != []


@pytest.mark.asyncio
def test_get_articles_of_page_fail():
    session = aiohttp.ClientSession()
    forum_name = 'funny'
    page_index = -1
    result = yield from aiodcard.get_articles_of_page(session, forum_name, page_index)
    assert result == []


@pytest.mark.asyncio
def test_get_article_successs():
    session = aiohttp.ClientSession()
    article_id = '388072'
    result = yield from aiodcard.get_article(session, article_id)
    assert result != {}


@pytest.mark.asyncio
def test_get_article_fail():
    session = aiohttp.ClientSession()
    article_id = '1'
    result = yield from aiodcard.get_article(session, article_id)
    assert result == {}
