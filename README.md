# gbos_tropo

This is the backend Tropo application for the Giant Ball of String application. This microservice is used to send SMS
messages to visitors of the giant ball of string, as well as respond to requests for facts about the giant ball of string

## Usage

Sessions are generally initiated via the Tropo REST API as such

https://api.tropo.com/1.0/sessions?action=create&token={{TOKEN}}&numberToDial={{PHONE}}"

This will send a welcome message to the phone number provided. The user can respond back via SMS to get additional information


# Prerequisites

To use this application effectively, you will need the following

* A tropo account with outbound SMS enabled
* A Mantl or marathon stack

## Installation


This application is designed to be ran in a Mantl (marathon) stack, an installation script is provided for your convenience

```
bash marathon_install.sh
```

This script will gather all of the required information, install the application into your Mantl instance, as well
as create the application using Tropo's REST API service.




