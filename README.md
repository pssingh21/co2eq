# Co<sub>2</sub>eq
 ## [Live App](https://co2eq.netlify.app) Deployment Status:&nbsp; [![Netlify Status](https://api.netlify.com/api/v1/badges/d8891a86-be1d-4e5a-8789-b4592385910a/deploy-status)](https://app.netlify.com/sites/co2eq/deploys)

`co2eq` estimates the CO2 emissions associated to air flights.
It is currently focused on a single meeting. 
CO2 emissions can be estimated according to the flying distance between each attendee and the meeting place (distance mode). 
However, CO2 emissions are highly dependent on the number of legs of a given flight itineraries. 
The originality of `co2eq` is that for each participant, `co2eq` derive an effective flight and estimates the CO2 emissions considering each of these legs (flight mode).

`co2eq` plots the repartitions of CO2 emissions according to any criteria associated to each attendee.

While the focus is on C02 `co2eq` also performs more standard representations of attendance in number of participants (attendee mode).

A detailed description of `co2eq` can be found here:

* Daniel Migault *CO2eq*: "Estimating Meetings' Air Flight CO2 Equivalent Emissions - An Illustrative Example with IETF meetings", Show me the numbers: Workshop on Analyzing IETF Data (AID), 2021. [https://www.iab.org/wp-content/IAB-uploads/2021/11/Migault.pdf](https://www.iab.org/wp-content/IAB-uploads/2021/11/Migault.pdf). 


A example of the outputs of `co2eq` outputs can be found on the `co2eq` web site https://mglt.github.io/co2eq/, 
where CO2 emissions have been computed for the [IETF](https://mglt.github.io/co2eq/IETF/IETF/) meetings and the [ICANN](https://mglt.github.io/co2eq/ICANN/ICANN/).

# Installation 

Installation of co2eq can be done directly from github

```bash
$ git clone https://github.com/pssingh21/co2eq
$ cd co2eq
```
## Local installation

For installing co2eq in a python virtual environment
```bash
$ pip3 install virtualenv       # If you do not have virtualenv installed
$ python3 -m virtualenv co2eq   # Create a bew virtual environment
$ source co2eq/bin/activate     # Activate the virtual environment 
```
```bash
$ pip3 install -r requirements.txt    # Install dependencies
```


# Configuring and using co2eq

You will need a configuration file with filename `.env`. There is already a `.env.example` file contaning the format and required parameters for reference. 
It is recommended to generated it by copying the .env.example file and filling in the configuration details.

```bash
$ cp .env.example .env
```

The `.env` file should have the following format:
```
## co2eq retrieves flight offers to estimate a real flight and uses the AMADEUS API:
## https://developers.amadeus.com/get-started/get-started-with-amadeus-apis-334
## You need to register and request and an API Key and an API Secret for the 
## Flight Offers Search service.
AMADEUS_ID=XXXX
AMADEUS_SECRET=XXXX

## To compute the CO2 emissions associated a flight a request is sent to GO Climate 
## Please go through https://api.goclimate.com/docs to get an account.
GOCLIMATE_SECRET=XXXX
NOMINATIM_ID=XXXX

OUTPUT_DIR=/app/src/co2eq/output                                        #For docker images
OUTPUT_DIR=/home/your_path_to_project_folder/co2eq/src/co2eq/output     #For local development

```

# Running docker container

```bash
$ docker build --tag co2eq .      # Build the image using Docker
$ docker run -p8000:8000 co2eq    # Run the Docker image
```

# Running the frontend

To run the frontend, open [src/frontend/index.html](src/frontend/index.html) on your browser.

If you are running the server on your local machine or a different remote server, make sure to update the backend URL in the [src/frontend/index.html](src/frontend/index.html) file. Change [const socketUrl="ws://..."](https://github.com/pssingh21/co2eq/blob/68983eb8c7506031cb830c9e6989fca2e2028db9/src/frontend/index.html#L325) to your backend URL.

# Deploying the application

To deploy the backend, build the Docker image and push the image to the server. 
To deploy the frontend, upload the [src/frontend/index.html](src/frontend/index.html) file to the server.

# JSON format for upload
Format of JSON file to upload via frontend:
```json
{ 
    "name" : "required", 
    "location" : { 
        "country" : "required", 
        "iata": "optional"
    },
    "attendee_list": [
        {
            "country": "required",
            "iata": "optional",
            "number_of_attendee": required
        }
    ]                                    
}
```
Example:
```json
{ 
    "name" : "IETF_201", 
    "location" : { 
        "country" : "DE", 
        "iata": "SXF"
    },
    "attendee_list": [
        {
            "country": "US",
            "iata": "LAX",
            "number_of_attendee": 1
        },
        {
            "country": "FR",
            "number_of_attendee": 2
        },
        {
            "country": "JP",
            "number_of_attendee": 5
        }
    ]                                    
}

```

# JSON Format for API
Format of data to be sent to API endpoint:
```json
{ 
    "name" : "required", 
    "location" : { 
        "country" : "required", 
        "iata": "optional"
    },
    "attendee_list": [
        {
            "country": "required",
            "iata": "optional"
        }
    ]                                    
}
```
Example:
```json
{ 
    "name" : "IETF_201", 
    "location" : { 
        "country" : "DE", 
        "iata": "SXF"
    },
    "attendee_list": [
        {
            "country": "US",
            "iata": "LAX",
        },
        {
            "country": "FR"
        },
        {
            "country": "FR"
        },
        {
            "country": "JP"
        }
    ]                                    
}

```


