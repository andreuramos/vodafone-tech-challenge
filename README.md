# Vodafone Tech Challenge

Code challenge for Vodafone python developer. Statement can be found [here](statement.2.0.md)

### Requirements

having docker installed

### Instructions

* build the docker image with `make build`
* start the container with `make up`
* stop the container with `make down`
* run the application with `make run`
* run the tests with `make tests`

### Solution Notes

* The csv parsing assumes no commas are present within the columns
* Also the file reader assumes all columns are present and in the same order.