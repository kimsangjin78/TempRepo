# ETL Project
* Seth Kim
* Trong Nguyen
## Proposed Use of Data
To select the best candidate businesses for a new food delivery service.  The service, unlike existing ones, will ship frozen meals or ingredients along with instructions to all markets within contiguous US.  To aid the selection process, we will need the following data points:
* review of restaurant
* whether the establishment does catering
* income levels of establshment's location
* popularity of the establishment
## Extract
Two sources of data is used
* Yelp dataset challenge.  Format: JSON
* IRS income by zipcode. Format: CSV
## Transform
We performed the following data transformation
### Yelp Dataset
Selected the following fields
* Business ID
* name
* address
* State
* Zip Code
* Has Catering
* Stars
* Review Count
### IRS data
Selected the following fields
* Zip Code
* Income Level
### Load
* Loaded into mySQL, with two tables: Business and Income
* Primary keys for the fhe tables are Busiess:Business ID and Income:Zip Code
* The two tables will be joined using the Zip Code fields
