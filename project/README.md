This is a SMS Reminder Service that pulls list of phone numbers and
uses [Twilio][] to send an SMS message to those phone numbers.

For more details, see
[Hack the Opioid Crisis: Texting reminder service][issue].

[issue]: https://github.com/ProgressiveHackNight/project-ideas/issues/8
[Twilio]: https://www.twilio.com/

## Requirements

* Python 3.6
* [pip and virtualenv](http://stackoverflow.com/q/4324558)

## Quick Start

```
python3 -m venv venv

# On Windows, replace the following line with 'venv\Scripts\activate'.
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

At this point you'll be prompted for a username and password; enter
whatever you want. Then run:

```
python manage.py runserver
```

At this point, you can visit http://localhost:8000/admin and log in
as the user you created earlier.

## Environment Variables

Unlike traditional Django settings, we use environment variables
for configuration to be compliant with [twelve-factor][] apps.

**Note:** When an environment variable is described as representing a
boolean value, if the variable exists with *any* value (even the empty
string), the boolean is true; otherwise, it's false.

**Note:** When running `manage.py`, the following environment
variables are given default values: `SECRET_KEY`. Also, `DEBUG` is enabled.

* `SECRET_KEY` is a large random value.
* `DEBUG` is a boolean value that indicates whether debugging is enabled
  (this should always be false in production).
* `DATABASE_URL` is the URL for the database. Defaults to a `sqlite://`
  URL pointing to `db.sqlite3` at the root of the repository.


[twelve-factor]: http://12factor.net/
