# Giant Ball of String: Tropo

Giant Ball of String (GBoS) is a sample demonstration applicaiton that illustrates how several technologies from Cisco can be brought together to address a business problem.  

## Demo Application Background

All across the United States, there are roadside attractions like *The Worlds Largest Fork*, *The Biggest Donut*, and *The Giant Ball of String*.  The organization that manages these attractions is facing pressure to provide better metrics and details about the visitors to the attractions, and to provide a better experience for those visitors.  If they can't meet this demand, they may see their funding reduced.  

To address this problem, the technical staff has built their next generation attraction support platform.  This platform provides the following capabilities:

* Monitor activity at each site using motion detectors.  
* Turn on lights, signage, and resources at each site only when vistors are present
* Provide centralized logging of visits at all attractions
* Informational Kiosks at each attraction 
* Direct interaction with visitors by providing facts and Q/A through their mobile devices

## Full Demo Details

This repository and README provide details on setting up just the gbos_iox code and deployment.  More details available at: 

* [gbos_demo](https://github.com/imapex/gbos_demo) - Full Demo Application Setup and Details
* [gbos_iox](https://github.com/imapex/gbos_iox) - Details on the Cisco IOx Client Application 
* [gbos_arduino](https://github.com/imapex/gbos_arduino) - Details on the Arduino Microcontroller Code 
* [gbos_kiosk](https://github.com/imapex/gbos_kiosk) - Details on the Welcome Web Portal Page
* [gbos_tropo](https://github.com/imapex/gbos_tropo) - Details on the Tropo Service for SMS based communication with visitors

---

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




