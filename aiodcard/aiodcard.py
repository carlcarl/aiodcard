# /usr/bin/env python3

import logging
import sys
import re
import os
import asyncio

logging.basicConfig(
    stream=sys.stderr, level=logging.INFO,
    format='[%(levelname)s](%(funcName)s/%(lineno)d) %(message)s',
)
logger = logging.getLogger(__name__)


def get_direct_image_url(image_url):
    """
    Used to trasform image html url to image url.
    Support: imgur
    """
    imgur_id = re.findall('http[s]?://imgur.com/((?:[a-zA-Z]|[0-9])+)', image_url)
    if imgur_id:
        image_url = 'http://i.imgur.com/{0}.png'.format(imgur_id[0])
    return image_url


def find_image_urls(article_json):
    # https://stackoverflow.com/questions/169625/regex-to-check-if-valid-url-that-ends-in-jpg-png-or-gif
    # https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    image_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.(?:jpg|gif|png)|http://imgur.com/(?:[a-zA-Z]|[0-9])+', article_json['version'][0]['content'])
    return image_urls


@asyncio.coroutine
def download_image(session, image_url, image_folder, image_name):
    logger.info('download@%s', image_url)
    result = {
        'func_name': 'download_image',
        'image_url': image_url,
        'image_folder': image_folder,
        'image_name': image_name,
        'result': 0,
    }
    response = yield from session.request('get', image_url)
    if response.status != 200:
        logger.error('Download image failed: %s', image_url)
        result['result'] = -1
        return result
    image_path = os.path.join(image_folder, image_name)
    image = yield from response.read()
    with open(image_path, 'wb') as f:
        f.write(image)
    yield from response.release()
    return result


@asyncio.coroutine
def get_articles_of_page(session, forum_name, page_index):
    url = 'https://www.dcard.tw/api/forum/{0}/{1}/'.format(forum_name, page_index)
    response = yield from session.request('get', url)
    if response.status != 200:
        logger.error('Get article list failed: %s', url)
        yield from response.release()
        session.close()
        return []
    articles_json = yield from response.json()
    yield from response.release()
    session.close()
    return articles_json


@asyncio.coroutine
def get_article(session, article_id):
    url = 'https://www.dcard.tw/api/post/all/{0}'.format(article_id)
    response = yield from session.request('get', url)
    if response.status != 200:
        logger.error('Get article content failed: %s', url)
        yield from response.release()
        session.close()
        return {}
    article_json = yield from response.json()
    yield from response.release()
    return article_json
