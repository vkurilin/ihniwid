__all__ = ("CodeSuggestion",)


class CodeSuggestion:
    def __init__(self, *, question_text: str, answer_link: str, raw_code: str):
        self.question_text = question_text
        self.answer_link = answer_link
        self.raw_code = raw_code

    def _repr_html_(self):
        pre_style = "border: 1px solid gray; padding: 5px; margin: 5px 0"
        return (
            f'<p>{_("From")} <a href={self.answer_link}>{self.question_text}</a>:</p>'  # type: ignore # noqa
            f'<pre style="{pre_style}"><code>' + self.raw_code + "</code></pre>"
        )
