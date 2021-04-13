import requests

from ihniwid.backend import foo


def test_nocaptcha(requests_mock, capsys):
    def custom_matcher(request):
        if (
            request.url
            == "https://stackoverflow.com/search?q=undefined+is+not+a+function"
        ):
            resp = requests.Response()
            resp.status_code = 200
            resp.url = "https://stackoverflow.com/nocaptcha?s=a9596900-03df-4660-88f5-03949ed99dad"
            return resp
        return None

    requests_mock._adapter.add_matcher(custom_matcher)

    foo("undefined is not a function")

    captured = capsys.readouterr()
    assert (
        "Oh noes! Please solve this captcha: https://stackoverflow.com/nocaptcha?s=a9596900-03df-4660-88f5-03949ed99dad"
        in captured.err
    )
