# ihniwid

i have no idea what i'm doing
----------

A simple tool that will try to find answers on [Stack Overflow](https://stackoverflow.com) for you.

## Participants:

* Sergey Bugaev, 620, login: bugaevc
* Vladimir Kurilin, 620, login: vkurilin

## Formulation of the problem

Create a tool that automates the basic search for a solution of your problem on Stack Overflow. 

Rough equivalent for 

![try-catch-stackoverflow](https://github.com/vkurilin/ihniwid/blob/main/description/try-catch-stackoverflow.png)

The base intended interface for displaying search results is the HTML code which should work just well with Jupyter notebook cell.


## Interface model:

Intended use case:
![](https://github.com/vkurilin/ihniwid/blob/main/description/interface-model.png)

## Setup
```sh
# Install dependencies
$ poetry install

# Setup pre-commit and pre-push hooks
$ poetry run pre-commit install -t pre-commit
$ poetry run pre-commit install -t pre-push
```

## Documentation

To build the Sphinx documentation, run:
```sh
$ cd docs
$ poery run make html
```

Then open `_build/html/index.html` in your web browser.

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
