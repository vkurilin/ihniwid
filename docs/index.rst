Welcome to Ihniwid's documentation!
===================================

ihniwid integrates with IPython / Jupyter to make it easy to search
for solutions on Stack Overflow.

To load ihniwid into IPython, use the ``%load_ext`` magic, like this::

  %load_ext ihniwid

Then later, when you get an error, use the ``%ihniwid`` magic to look it
up and suggest code snippets::

  %ihniwid

ihniwid will automatically find the latest exception using ✨ **dark magic** ✨,
search for it on Stack Overflow, and suggest code snippets that you can
easily copy and paste into your notebook.

Alternatively, you can always specify a serach term explicitly::

  %ihniwid numpy.ones

In this case ihniwid will not look for any exceptions and instead search
for the term you have provided.

In addition to IPython integration, ihniwid also provides programmatic API.
Please see the :py:meth:`ihniwid.backend.find_code_suggestions` function
for the entry point to the API.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
