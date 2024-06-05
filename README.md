# Vodafone Tech Challenge

Code challenge for Vodafone python developer. Statement can be found [here](statement.2.0.md)

### Requirements

having docker installed

### Instructions

* build the docker image with `make build`
* start the container with `make up`
* stop the container with `make down`
* run the application with `make run`. __NOTE:__ a source file named `customers.csv` is expected to be in a `data` directory
* run the tests with `make tests`

### Assumptions

* The csv parsing assumes no commas are present within the columns
* Also the file reader assumes all columns are present and in the same order.
* A __letter__ (term used to describe the mask behaviour) is understood as an alphabetical character, excluding numerical and others

### Solution notes

The project has an entrypoint `app.py` which basically instantiates and executes the use case and handles the result. The `use_case` is an orchestrator with many collaborators injected in its constructor (to match inversion of control principle). 

As we're expecting to have more sources of customers in the future, the `csv_customer_reader` is not directly injected into the use case but an abstract class `customer_reader` so the use case is not coupled to that implementation and a `db_customer_reader` with the connection & mapping implementation details could be easily injected instead.

Even no splicit linter have been used, the `pep8` standard was configured to auto-format the files from the editor during the development.