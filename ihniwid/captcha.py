from IPython.display import display, HTML


__all__ = ('CaptchaError',)


class CaptchaError(Exception):
    def __init__(self, url: str):
        display(HTML(
            '<p style="color: red"><b>Oh noes!</b></p>'
            '<p>StackOverflow suspects me of being a robot (rightfully so!)</p>'
            f'<p>Please solve <a href="{url}">this captcha</a> and then try '
            'again.</p>'
        ))
