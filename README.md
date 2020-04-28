# Project Title

Measurement Converter

## Getting Started

This is a demo project that converts temperatures and volumes in various ways.  It uses python, AWS Lambda, and AWS Api Gateway.

## TODO

1. Add CloudWatch alerts to notify if API calls are failing
2. Add S3-hosted static website so users can use a UI
3. Add a dead letter SQS queue to catch any failed requests
4. Add API throttling
5. 

### Prerequisites

1. Serverless Framework
2. An AWS Account (if you want to test in the cloud and not locally)

### Installing

(Note that these commands should work pretty easily on Linux or Mac, but for Windows you should probably install GitBash)

1. Install node.js follow the proper instructions for your operating system
2. Install npm following the proper instructions for your operating system
3. Install Serverless Framework:

```
npm install -g serverless
```

4. Install serverless-python-requirements plugin:

```
npm install serverless-python-requirements
```

5. Install serverless-offline-python plugin:

```
npm install serverless-offline-python
```

6. Run the project in offline mode

```
sls offline start
```

7. From a command prompt, invoke the various curl commands (see below).

## Running the unit tests

Open the project in Pycharm.  Right click on the test folder and run "pytest in tests"

### Sample CURL Commands to test functionality

Convert a temperature from Fahrenheit to Celsius

```
curl -v localhost:3000/32/0/f/c
```

Convert a temperature from Kelvin to Celsius

```
curl -v localhost:3000/273.15/0/k/c
```

## Versioning

Version 0.1

## Authors

* **Kenneth Kehl** - *Initial work* - [terrazoon](https://github.com/terrazoon)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
