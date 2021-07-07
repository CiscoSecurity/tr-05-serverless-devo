[![Gitter Chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter Chat")

# Devo Relay (Cisco Hosted)

A Cisco SecureX Concrete Relay implementation using [Devo](https://www.devo.com/) as a third-party Cyber Threat Intelligence service provider.

The Relay itself is just a simple application written in Python that can be easily packaged and deployed.

The code is provided here purely for educational purposes.

## Rationale

- We need an application that will translate API requests from SecureX Threat Response to the third-party integration, and vice versa.
- We need an application that can be completely self contained within a virtualized container using Docker.

## Testing (Optional)

Open the code folder in your terminal.
```
cd code
```

If you want to test the application you have to install dependencies from the [requirements.txt](code/requirements.txt) file:
```
pip install --upgrade --requirement requirements.txt
```

You can perform two kinds of testing:

- Run static code analysis checking for any semantic discrepancies and
[PEP 8](https://www.python.org/dev/peps/pep-0008/) compliance:

  `flake8 .`

- Run the suite of unit tests and measure the code coverage:

  `coverage run --source api/ -m pytest --verbose tests/unit/ && coverage report`

**NOTE**. If you need input data for testing purposes you can use data from the
[observables.json](code/observables.json) file.

### Building the Docker Container
In order to build the application, we need to use a `Dockerfile`.  

 1. Open a terminal.  Build the container image using the `docker build` command.

```
docker build -t tr-05-devo .
```

 2. Once the container is built, and an image is successfully created, start your container using the `docker run` command and specify the name of the image we have just created.  By default, the container will listen for HTTP requests using port 9090.

```
docker run -dp 9090:9090 --name tr-05-devo tr-05-devo
```

 3. Watch the container logs to ensure it starts correctly.

```
docker logs tr-05-devo
```

 4. Once the container has started correctly, open your web browser to http://localhost:9090.  You should see a response from the container.

```
curl http://localhost:9090
```

## Implementation Details

This application was developed and tested under Python version 3.9

### Implemented Relay Endpoints

- `POST /health`
  - Verifies the Authorization Bearer JWT and decodes it to restore the original credentials.
  - Authenticates to the underlying external service to check that provided credentials are valid and the service is available at the moment. 
  
- `Post /observe/observables`
  - Accepts a list of observables.
  - Verifies the Authorization Bearer JWT and decodes it to restore the original credentials.
  - Makes request to the underlying external service to query for some cyber threat intelligence data on each supported observable.
  - Maps the fetched data into appropriate CTIM entities.
  - Returns a list per each of the following CTIM entities (if any extracted):
    - Sighting
  
- `POST /version`
  - Returns the current version of the application.

### Supported Types of Observables

`ALL`

### CTIM Mapping Specifics

Each response from the Devo API for the supported observables generates the following CTIM entities:

| Property in CTIM          | Required | Maps to                                                      |
| ------------------------- | -------- | ------------------------------------------------------------ |
| confidence                | yes      | High                                                         |
| count                     | yes      | 1                                                            |
| id                        | yes      | type, title, .object[].eventdate, and observable.value are used as seed to generate ID |
| observed_time: start_time | yes      | .object[].eventdate                                          |
| schema_version            | yes      | 1.1.6                                                        |
| type                      | yes      | sighting                                                     |
| data: columns             |          | Keys (as `"type": "string"`) for the following fields: "technology", "brand", "phylum", "family", "genus", "species" |
| data: rows                |          | Values for associated fields used in columns                 |
| description               |          | .object[].message                                            |
| internal                  |          | True                                                         |
| observables               |          | The observable and type that was searched for                |
| short_description         |          | Devo received a log message from {.object[].hostName} containing the observable |
| source                    |          | Devo                                                         |
| title                     |          | Log message received by Devo in last 30 days contains observable |


Used values:
  - .object[]
  - .object[].eventdate
  - .object[].message
  - .object[].technology
  - .object[].brand
  - .object[].phylum
  - .object[].family
  - .object[].genus
  - .object[].species
