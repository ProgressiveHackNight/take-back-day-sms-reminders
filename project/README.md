This is a SMS Reminder Service that pulls list of phone numbers and
uses [Twilio][] to send an SMS message to those phone numbers.

For more details, see
[Hack the Opioid Crisis: Texting reminder service][issue].

## What problem are we trying to solve?

There are two nation-wide Take Back Days held annually. This is a time for people to take their unused and unneeded prescription drugs to designated sites for free and environmentally-friendly disposal. Take Back Days are not on the same days year after year, and people might forget when they are happening. The proposed solution to this is to allow users to sign up for a Texting reminder service, in which they enter their phone number (with no other identifying information), and we send them a reminder two days before a Take Back Day, and then on the day of.

A big concern here is privacy, as people will have to volunteer their phone numbers to this service.

## Who will benefit (directly and indirectly) from this project?

Government stands to benefit as they are running these Take Back Days. Constituents benefit by having free and proper disposal of prescription drugs in a "no questions asked" kind of way.

[issue]: https://github.com/ProgressiveHackNight/project-ideas/issues/8
[Twilio]: https://www.twilio.com/

## Where can we find any research/data available/articles?

The New York Attorney General's office has provided publicly available data [here](https://github.com/NYAG/Takeback_Day_Hackathon).

## What help is needed at this time?

### Designers
We need design for the UI that accepts these phone numbers!

### Developers
#### Frontend
We need an embeddable service that can be added to different webpages to collect phone numbers. We also need to asynchronously send that information to a secure DB to be used later as we send the texted reminders.

Here is a [great example of firing a message with Twilio from Patrick Weaver](https://glitch.com/edit/#!/twilio-example) to start with! You will need your own credentials to set up the environment variables.

#### Backend
We need to process and store phone numbers, protect against SQL injection/sanitize user input. We also need to plug into a P2P texting service (like [Spoke](https://opensource.moveon.org/spoke-p2p/) or [Hustle](https://hustle.com/)) to actually send these messages.

### Creatives
We need copy for all the messaging and texted alerts.

### Data/Security
We need to find a secure way to accept and store this data, as it is personally identifying, and a big tenet of the Take Back Day program is some level of anonymity.

## How can we contact you outside of Github(list social media or places you're present)?

_Add your name here if you plan to stay on with this project through the March 11 HackDay!_

## Sources

This is all based on the presentation from the following people! They presented at the Pre-HackDay!

* Daniel Spencer (full stack dev) - daniel.patrick.spencer@gmail.com
* Carlos Merced (front end dev) - mail.merced@gmail.com
* Annie Hirshman (designer) - anniehirshman@gmail.com
* Anna de Paula Hanika (product) - annadph@gmail.com
* Daeha Ko (IT) - daehako@gmail.com

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
