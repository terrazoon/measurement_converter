# Project Title

Measurement Converter

## Getting Started

This is a demo project that converts temperatures and volumes in various ways.  It uses python, AWS Lambda, and AWS Api Gateway.

## How to run the app

### Via the Demo UI

http://teacher-converter-tool.s3-website-us-east-1.amazonaws.com

This is a simple UI to support this project.  Code for it can be found at [GitHub] (https://github.com/terrazoon/measurement_converter_ui)

### Via the browser URL bar

https://www.kennethkehl.com/api/temperature/{input}/{student response}/{from_units}/{to_units}
https://www.kennethkehl.com/api/volume/{input}/{student response}/{from_units}/{to_units}

Note that if you get tired of typing Fahrenheit or Cubic-feet every time, there is a shorthand you can use. This
shorthand is the first letter of the unit of measurement (Fahrenheit == 'f', etc.) except in the case of cubic-feet ("f")
and cubic-inches ("i")

### Running locally

Install Serverless Framework and its dependencies the normal way you would do for your operating system.

Install serverless-python-requirements plugin:

```
npm install serverless-python-requirements
```

Install serverless-offline-python plugin:

```
npm install serverless-offline-python
```

Run the project in offline mode

```
sls offline start
```

Get the URLs to use from the command prompt (should be localhost:3000 etc.)

7. Call the urls from a browser, or, from a command prompt, invoke the various curl commands (see below).


## Code Reviews

To check in, create a pull request for https://github.com/terrazoon/measurement_converter.  You will need two code reviewers, including at least one code owner.

## CI/CD

The repository uses GitHub Actions so that lint and unit tests are run on every check in.  Right now checking in
does not automatically cause the app to deploy, because to do so AWS credentials would have to be stored as secrets
in GitHub and GitHub specifically recommends not doing this while GitHub Actions is in public beta.

### Prerequisites

No prerequisites if you are just running the app in a browser.

If you want to run the app locally or do development work, you will need Serverless Framework.


## Running the unit tests locally

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

## Things to improve

1. The CI/CD process is set up with Github Actions.  Check-ins currently trigger unit tests and lint checks.  But there is no deploy step right now.
This is because a deploy step would require storing AWS access keys in Github and Github specifically recommends not doing so while
Github Actions is in public beta. 
2. Add CloudWatch alarms to notify if API calls are failing
3. Improve the UI by using CloudFront and a custom domain.
4. Add a dead letter SQS queue to catch any failed requests
5. Register emails to notify users of api changes

## Versioning

Version 0.1

## Authors

* **Kenneth Kehl** - *Initial work* - [terrazoon](https://github.com/terrazoon)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
