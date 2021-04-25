from IPython.display import HTML, display

__all__ = ("CaptchaError",)


class CaptchaError(Exception):
    def __init__(self, url: str):
        display(
            HTML(
                f'<p style="color: red"><b>{_("Oh noes!")}</b></p>'  # type: ignore # noqa
                f'<p>{_("StackOverflow suspects me of being a robot (rightfully so!)")}</p>'  # type: ignore # noqa
                f'<p>{_("""Please solve <a href="{}">this captcha</a> and then try again.""").format(url)}</p>'  # type: ignore # noqa
            )
        )
