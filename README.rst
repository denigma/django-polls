=====
Polls
=====

Polls is a simple Django app to conduct web-based polls. For each question, 
visitors can choose between a fixed number of answers.

Detailed documentation will be available in the "docs" directory.


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    ...
    INSTALLED_APPS = (
        ...
        'polls',
    )
    ...

2. Include the polls URLcong in your project ursl.py like this::

    (r'^polls/', include('polls.urls')),

3. Optionally: Customize and integrate templates.
   Create a polls/base.html in your project template directory to extend it
   with the site base template:
   
    mkdir polls
    nano base.html
    {% extends "site_base.html" %} # or any other respective base name.
    {% block title %}Polls{% endblock %}
    {% block subtitle %}{% endblock %}
    {% block content %}{% endblock %}

4. Run `python manage.py syncdb` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Amdin app enabled).

6. Visit http:/127.0.0.1:8000/polls/ to participate in the poll.
