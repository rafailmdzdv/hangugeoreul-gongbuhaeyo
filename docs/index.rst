Welcome to ssaem's documentation!
==================================================


What is this project all about?
The main idea of this project is to help users learn Korean (for now) by generating
sentences based on their specific vocabulary and known grammar points.
I have been using this method to learn the language with the help of LLMs.
However, constantly providing an updated list of vocabulary and grammar rules to the LLM was difficult. Since I already had a vocabulary learning project, I decided to take it to the next level and integrate an LLM directly into it.


Goals
-----

When developing this template we had several goals in mind:

- Development environment should be bootstrapped easily,
  so we use ``docker-compose`` for that
- Development should be consistent, so we use strict quality and style checks
- Development, testing, and production should have the same environment,
  so again we develop, test, and run our apps in ``docker`` containers
- Documentation and codebase are the only sources of truth


Limitations
-----------

This project implies that:

- You are using ``docker`` for deployment
- You are not using any frontend assets in ``django``,
  you store your frontend separately


How to start
------------

You should start with reading the documentation.
Reading order is important.

There are multiple processes that you need to get familiar with:

- First time setup phase: what system requirements you must fulfill,
  how to install dependencies, how to start your project
- Active development phase: how to make changes, run tests and linters,
  write documentation, and use GitLab CI
- Production phase: deployment checklist, production configuration,
  and operations.


.. toctree::
   :maxdepth: 2
   :caption: Setting things up:

   pages/template/overview.rst
   pages/template/development.rst
   pages/template/django.rst

.. toctree::
   :maxdepth: 2
   :caption: Quality assurance:

   pages/template/documentation.rst
   pages/template/linters.rst
   pages/template/testing.rst
   pages/template/security.rst

.. toctree::
   :maxdepth: 2
   :caption: Production:

   pages/template/production-checklist.rst
   pages/template/production.rst

.. toctree::
   :maxdepth: 1
   :caption: Extras:

   pages/template/upgrading-template.rst
   pages/template/troubleshooting.rst


Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
