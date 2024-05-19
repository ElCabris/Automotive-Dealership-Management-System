# Automotive Dealership Management System

## Description
This system allows managing test drive requests and vehicle purchases at an automotive dealership.

## Features

### User Registration:
The user enters their identification number and is asked whether they want to schedule a test drive or purchase a vehicle.

### Test Drive:
* A calendar displaying available dates and times for test drives is shown.
* The user selects a date and time.
* The system checks the availability of vehicles for that date and time.
* If there is availability, the user enters their name, identification number, and is instructed to proceed to the nearest dealership.

### Vehicle Purchase
* The user selects the type of vehicle they desire (sports car, van, sedan).
* They select the type of rim (sports, winter, traditional street).
* Choose the vehicle color (black, blue, etc.).
* Select the engine displacement (1500, 2000, 2500).
* Choose the interior color of the vehicle.
* If they want any extras, they are instructed to proceed to the dealership.
* Enter their personal information (name, phone number, identification number).
* Select the payment method (check, cash, transfer, card).
* The system checks the inventory of available vehicles for sale and verifies if the selected vehicle is available.
* If the vehicle is available, the purchase order is generated, and the user is instructed to proceed to the dealership.

## Install packages
To install the packages, you must execute the following command.
```
pip install -r requirements.txt
```

## Program execution guide

To execute the program, follow the following command.

```
python -m src.app
```