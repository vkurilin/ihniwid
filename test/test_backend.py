import pytest
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


def test_undefined_is_not_a_function(requests_mock, capsys):
    def read_api_questions_page(i):
        with open(
            f"test/mocked_requests/undefined-is-not-a-function/api-questions-by-ids-page{i}.json"
        ) as f:
            return f.read()

    for i in range(1, 6):
        requests_mock.get(
            f"https://api.stackexchange.com/2.2/questions/9329446;38987;3390396;27509;950087;500431;336859;7975093;27608009;28857189;17289236;6381136;28804334;12694530;28539077/answers/?pagesize=100&page={i}&filter=withbody&site=stackoverflow",
            text=read_api_questions_page(i),
        )

    with open(
        "test/mocked_requests/undefined-is-not-a-function/200.html"
    ) as resp_data, open(
        "test/mocked_requests/undefined-is-not-a-function/api-200.json"
    ) as api_search:
        requests_mock.get(
            "https://stackoverflow.com/search?q=undefined+is+not+a+function",
            text=resp_data.read(),
        )
        requests_mock.get(
            "https://api.stackexchange.com/2.2/sites/?pagesize=1000&page=1&filter=%21%2AL1%2AAY-85YllAr2%29",
            text=api_search.read(),
        )

    with pytest.raises(AttributeError):
        foo("undefined is not a function")

    captured = capsys.readouterr()

    with open(
        "test/mocked_requests/undefined-is-not-a-function/output.txt", "r"
    ) as output:
        assert captured.out.replace("\r", "") == output.read()
