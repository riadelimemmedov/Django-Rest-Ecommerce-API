
# Ecommerce RESTful API

This repository contains the source code for a RESTful API built with Django Rest Framework for an e-commerce platform.
The new system will provide a client interface returning detailed and accurate update-to-date product information.

###

Installation and Setup

* To run this project on your local machine, follow these steps:

              1 - Clone the repository: 
                    * git clone https://github.com/riadelimemmedov/Django-Rest-Ecommerce-API.git

              2 - Create a virtual environment:
                    * cd Django-Rest-Ecommerce-API
                    * python3 -m venv env 
                    * source env/bin/activate  # for Linux/Mac
                    * env\Scripts\activate or env/Scripts/activate  # for Windows
              
              3 - Install the required packages:
                    * pip install -r requirements.txt

              4 - Set up the database:
                    * python manage.py migrate

              5 - Create a superuser:
                    * python manage.py createsuperuser

              6 - Start the server:
                    * python manage.py runserver

              7 - Access the API at:
                    * http://localhost:8000.

###

* Functional Objectives

  * High Priority

            1) The system shall provide the following data collection API endpoints:
                * Return all categories
                * Return a specified product and associated metadata
                * Return Product(s), including associated product metadata from a specified category
            
            2) The system shall allow employees to add and administrate product inventory
            
            3) The system shall reflect new and changed products and product data changes x minutes of the database being updated by the product owner.

###

* Supportability

        * The system should be able to accommodate new products and product lines
        * The system should support multiple types of product types with varying characteristics. In addition, the system should accommodate physical shippable and downloadable products.

###

* Security

        * The system will provide password-protected access to product data management and administration.

###

* RESTful API documentation

        * The system shall provide web-based documentation detailing all API endpoints and endpoint-specific details.

* Interfaces
  * The system must interface with

            * An SQLite database and be compatible with future migration to other database technologies.

###

<img src="D:\DRF-Ecommerce\Screenshot 2023-05-13 193317.png">
