# gbos_tropo

This is the backend Tropo application for the Giant Ball of String application. This microservice is used to send SMS
messages to visitors of the giant ball of string, as well as respond to requests for facts about the giant ball of string

## Usage

Sessions are generally initiated via the Tropo REST API as such

https://api.tropo.com/1.0/sessions?action=create&<token>={}&numberToDial=<phone>"

This will send a welcome message to the phone number provided. The user can respond back via SMS to get additional information

## Installation

TODO
