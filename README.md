# take-back-day-sms-reminders
SMS Reminder Service, pulls list of phone numbers and uses Twilio to send an SMS message to those phone numbers

All information about the work that has been done thus far can be found in [this issue](https://github.com/ProgressiveHackNight/project-ideas/issues/8).

Here is a [great example of firing a message with Twilio from Patrick Weaver](https://glitch.com/edit/#!/twilio-example) to start with! You will need your own credentials to set up the environment variables.

<!--- Keep everything below and click 'Submit new issue'  --->

### What problem are we trying to solve?

There are two nation-wide Take Back Days held annually. This is a time for people to take their unused and unneeded prescription drugs to designated sites for free and environmentally-friendly disposal. Take Back Days are not on the same days year after year, and people might forget when they are happening. The proposed solution to this is to allow users to sign up for a Texting reminder service, in which they enter their phone number (with no other identifying information), and we send them a reminder two days before a Take Back Day, and then on the day of.

A big concern here is privacy, as people will have to volunteer their phone numbers to this service.

### Who will benefit (directly and indirectly) from this project?

Government stands to benefit as they are running these Take Back Days. Constituents benefit by having free and proper disposal of prescription drugs in a "no questions asked" kind of way.

### Where can we find any research/data available/articles?

The New York Attorney General's office has provided publicly available data [here](https://github.com/NYAG/Takeback_Day_Hackathon).

### What help is needed at this time?

#### Designers
We need design for the UI that accepts these phone numbers!

#### Developers
##### Frontend
We need an embeddable service that can be added to different webpages to collect phone numbers. We also need to asynchronously send that information to a secure DB to be used later as we send the texted reminders.

##### Backend
We need to process and store phone numbers, protect against SQL injection/sanitize user input. We also need to plug into a P2P texting service (like [Spoke](https://opensource.moveon.org/spoke-p2p/) or [Hustle](https://hustle.com/)) to actually send these messages.

#### Creatives
We need copy for all the messaging and texted alerts.

#### Data/Security
We need to find a secure way to accept and store this data, as it is personally identifying, and a big tenet of the Take Back Day program is some level of anonymity.

### What are the next steps (validation, research, coding, design)?
We need research for the best P2P texting platform to use to power most of this, and we need basic architectural discussions of how this service should work.

### How can we contact you outside of Github(list social media or places you're present)?
_Add your name here if you plan to stay on with this project through the March 11 HackDay!_

### Sources
This is all based on the presentation from the following people! They presented at the Pre-HackDay!
Daniel Spencer (full stack dev) - daniel.patrick.spencer@gmail.com
Carlos Merced (front end dev) - mail.merced@gmail.com
Annie Hirshman (designer) - anniehirshman@gmail.com
Anna de Paula Hanika (product) - annadph@gmail.com
Daeha Ko (IT) - daehako@gmail.com

----
If you get stuck at any point, feel free to reach out to the leadership team with an email to steering@progressivehacknight.org or come find an organizer at a HackNight. We're here to help bring great ideas to life!
