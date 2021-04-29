from bs4 import BeautifulSoup
from stackapi import StackAPI

from .code_suggestion import CodeSuggestion
from .question import Question
from .utils import chunks

__all__ = ("Answer",)


class Answer:
    def __init__(self, raw):
        self.raw = raw

    def link(self) -> str:
        return "https://stackoverflow.com/a/" + str(self.raw["answer_id"])

    def question_id(self) -> int:
        return self.raw["question_id"]

    def code_suggestions(self, questions: dict[int, Question]):
        soup = BeautifulSoup(self.raw["body"], "html.parser")
        for tag in soup.find_all("pre"):
            if not tag.code:
                continue
            raw_code = str(tag.code.string)
            question_text = questions[self.question_id()].text
            yield CodeSuggestion(
                question_text=question_text,
                answer_link=self.link(),
                raw_code=raw_code,
            )

    @staticmethod
    def fetch_answers(question_ids):
        """Fetch the answers to the given question IDs.

        We use the official API for this.
        """
        api = StackAPI("stackoverflow")
        # We can submit up to 100 questions at a time.
        for chunk in chunks(question_ids, size=100):
            raw_answers = api.fetch(
                "questions/{ids}/answers", ids=chunk, filter="withbody"
            )["items"]
            for raw_answer in raw_answers:
                yield Answer(raw_answer)
