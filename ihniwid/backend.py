import requests
from bs4 import BeautifulSoup

from .captcha import CaptchaError
from .answer import Answer
from .question import Question


__all__ = ('find_code_suggestions',)



def is_question_link(tag) -> bool:
    return (
        tag.name == 'a' and
        tag.has_attr('class') and
        'question-hyperlink' in tag['class'] and
        'js-gps-track' not in tag['class'] and
        'title' in tag.attrs
    )


def extract_questions(soup):
    for tag in soup.find_all(is_question_link):
        yield Question(
            url=tag['href'],
            text=tag['title'],
        )


def find_code_suggestions(term: str):
    # Make a query to the search page.
    params = {'q': term}
    response = requests.get(f'https://stackoverflow.com/search', params=params)
    if 'nocaptcha' in response.url:
        raise CaptchaError(response.url)

    # Parse the response.
    soup = BeautifulSoup(response.text, 'html.parser')
    questions = dict()
    for question in extract_questions(soup):
        question_id = question.id()
        if question.id is not None:
            questions[question_id] = question

    for answer in Answer.fetch_answers(questions.keys()):
        yield from answer.code_suggestions(questions)
