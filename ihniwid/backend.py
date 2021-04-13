import sys
import urllib.parse
from typing import Optional

import requests
from bs4 import BeautifulSoup
from stackapi import StackAPI


def is_question_link(tag) -> bool:
    return tag.name == 'a' and tag.has_attr('class') and 'question-hyperlink' in tag['class']


def question_url_to_id(url: str) -> Optional[int]:
    parsed = urllib.parse.urlparse(url)
    if parsed.hostname and parsed.hostname != 'stackoverflow.com':
        return None
    parts: list[str] = parsed.path.split('/')
    if len(parts) < 3:
        return None
    if parts[0] != '' or parts[1] != 'questions':
        return None
    return int(parts[2])


def question_ids(soup):
    for tag in soup.find_all(is_question_link):
        question_url = tag['href']
        id = question_url_to_id(question_url)
        if id:
            yield id


def answers(site, soup):
    for chunk in chunks(question_ids(soup), size=100):
        yield from site.fetch('questions/{ids}/answers', ids=chunk, filter='withbody')['items']


def extract_code_blocks(answer):
    soup = BeautifulSoup(answer['body'], 'html.parser')
    for tag in soup.find_all('pre'):
        yield str(tag.code.string)


def foo(term: str):
    params = {'q': term}
    response = requests.get(f'https://stackoverflow.com/search', params=params)
    if 'nocaptcha' in response.url:
        print('Oh noes! Please solve this captcha:', response.url, file=sys.stderr)
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    for answer in answers(StackAPI('stackoverflow'), soup):
        for code_block in extract_code_blocks(answer):
            print('====')
            print(code_block)


def chunks(it, size: int):
    """Group iterator items into chunks of given size.

    This is like https://doc.rust-lang.org/std/primitive.slice.html#method.chunks,
    or the grouper example from itertools.
    """

    l = []
    for item in it:
        l.append(item)
        if len(l) == size:
            yield l
            l = []
    if l:
        # The last chunk may be shorter than the other ones.
        yield l


foo('undefined is not a function')
