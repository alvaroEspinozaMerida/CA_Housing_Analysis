# Predicting Housing Prices in SD?
#### Alvaro Espinoza, Johnny Rosas, Kristen Waterford

## Installation Instructions: 
### Dataset 
Please make sure to download all the datasets before running the code.
We have provided a link to a google drive that contains all the datasets that were used for this project. 
The datasets listed down below are the ones in their original state. These datasets in the drive 
have been cleaned and organized for ease of uses through EXCEL. The one's in the orignal state contained
some formatting issues that were fixed through EXCEL and the datasets were also reorganized into a more 
readable format. Some names from the original datasets were changed to make them more readable and only specific tables 
were kept for this project. For this project please use the datasets in the drive listed below. Feel free to explore the original datasets if you wish.
However these will not work with the code provided as their names and formats are different.
### Dependencies: 

- numpy==2.3.5
- pandas==2.3.3
- scipy==1.16.3
- matplotlib==3.10.8
- seaborn==0.13.2
- scikit-learn==1.8.0
- statsmodels==0.14.6
- duckdb==1.4.3
- jupyterlab==4.5.0
- notebook==7.5.0
- duckdb==1.4.3

Please make sure to install all the dependencies before running the code. 

If using UV please feel free to install with uv lock file using uv syns


## GOOGLE DRIVE LINK: 
https://drive.google.com/drive/folders/1y0IBR_L_SCslCzZhVG-HVn98-4qIYbWO

## Problem Statement: 
The primary purpose for predicting housing prices in California is to give residents some insight into the current state of the housing market. This information could possibly be used by potential real estate investors to get an idea as to the type of budget they would need for investing in housing in the state. This project could also be used by government officials in the creation of legislation to show how potentially greater supply is needed to bring down prices or push for more governmental support for home buyers through governmental loans. 

## Presentation Slides:
Here is a link to the presentation slides for this project: 
The slides provide a nicer view of the final results of the project. 

https://docs.google.com/presentation/d/1A9m-T36JaRxlzX7Mzs4CADtC7rVYLF9hSODgQ7Z4sck/edit?usp=sharing

## Final Report: 
Here is a link to the final report for this project: 
Formal analysis for the final results of this proeject. 

https://docs.google.com/document/d/1IeKgp9KA8KQNeCMQZvFEgCGeT74g5XdCwv5S8ep0Z7c/edit?usp=sharing

## Data Sets: 

___ 
## Median Price Dataset 

### 1. Source of the Data
California Association of Realtors 
#### Link:
https://www.car.org/marketdata/data/housingdata


### 2. What the Dataset Contains
Overall description: One row represents the median price of a single family detached home at a specific city and month/year. Each Column represents the data for a specific region in California. 

#### 3. Data Organization
    •    Format: CSV 
    •    Dimensions (Rows x Columns): (429, 64)
    •    Structure: One row represents the median price for specific M/Y and Column is a region 
    •    Time range : ​​1990 - 2025
    •    Geographic coverage (if applicable): Statewide 

### 4. Unit of Observation
#### What does one row in the dataset represent?
One row represents the median price of a single family detached home in a specific city and month/year.
### 5. Data Quality & Cleaning
Converted strings that represented Month/Year to actual DateTime Objects
Converted strings for money values into float values 
Converted NA values to 0 
For some reason data set contained values that were from 1925 , it was only 3 values so I had to remove these 
### 6. Limitations of the Dataset
Dataset covered a good amount of different regions that we were planning on exploring, we did not run into major issues with data limitations of the dataset 
### 7. How This Dataset Fits Into the Project
This dataset contains one of the most important values when it comes to our project's main goal of trying to predict the future price of homes in southern California; the value being the median price of homes in different counties of southern California. This data is the piece of data that will be main dataset that our project is built off of as it gives the most insight into the value we are trying assess. 
### 8. Exploratory Data Analysis 
Upon plotting each data point on scatterplot we are able to see a general trend of the median cost of a home in the state of california maintaining a relative stable price during the 90s, with increase occurring between 2000-2008 and major dip around 2008 and then a slow increase in price between 2008-2020 that saw prices reach 2008 prices within 12 years opposed to the eight years between 2000-2008. Around 2020 we can see a major increase in home prices with some stabilization happening after 2020. Other cities within southern california followed this general trend. 
___ 

## Debt Dataset 
### 1. Source of the Data
Where does the dataset come from?
Federal Reserve Bank of New York 
Link (if applicable):
https://www.newyorkfed.org/microeconomics/hhdc
### 2. What the Dataset Contains
Overall description: Total Debt of households divided by columns for Mortgage, HE Revolving , Auto Loan, Credit Card, Student Loan, Other, Total. Each row represents the debt for a specific fiscal quarter and year. 
### 3. Data Organization
    •    Format: XLSX  ->  CSV 
    •    Dimensions (Rows x Columns):  (104, 12)
    •    Structure: One row represents the total debt measured in percentages of trillion 
    •    Time range : ​​1999 - 2024
    •    Geographic coverage (if applicable): Nationwide  
### 4. Unit of Observation/Measurment 
#### What does one row in the dataset represent?
Each row represents the total debt for a specific category and  quarter of fiscal year. Each csv in this dataset  is measured in values of trillions of US dollars. 
### 5. Data Quality & Cleaning
Converted strings that represented fiscal quarter/Year to actual DateTime Objects
Converted strings for money values into float values 
For some reason data set was divided into separate datasets for data after 2003 and another before 2003 that covered time between 1999 - 2003
Had to combine both of these datasets into one dataframe to get the full picture of debt between 1999 - 2024 
One dataset had to transposed inorder for this conversion to be possible 
### 6. Limitations of the Dataset
The dataset gives really good insight into the total debt within the country and the different categories of debt. Despite it not being month to month the fiscal quarter division is still a great way of dividing time. This financial data may be too broad as it covers the entire Nation rather than just California. However it can still be used to give good insight on debt trends within the state as debt within the state more than likely follows national trends. 
### 7. How This Dataset Fits Into the Project
	This dataset provides us with insight into the total debt within the United States and is one of the factors that can be considered with housing prediction. This financial data is insightful because we can potentially study a relationship between mortgage debt and median house price. It can also give us a general idea into consumer spending habits and health of the national economy. 
### 8. Exploratory Data Analysis 
	Upon plotting on a scatter plot the total amount of debt data I can see that between 2000 - 2008 that there was steady increase in debt. Then we see after 2008 there was a decrease in debt and then 2016  another steady increase in total debt. 
	When plotting debt for just mortgages I saw relatively the same plot as the total debt, with a slightly deeper curve around 2008 and slower increase after that year. 

___ 
## Property Tax Dataset 
### 1. Source of the Data
Where does the dataset come from?
California State Controller Office 
Link :
https://propertytax.bythenumbers.sco.ca.gov/#!/year/default
### 2. What the Dataset Contains
Overall description: Contains information on total gross taxes collected on properties throughout different regions in California. 

### 3. Data Organization
    •    Format: XLSX  ->  CSV 
    •    Dimensions (Rows x Columns): (986, 9)
    •    Structure: One row  represents a specific city/regions tax total taxes collected for a specific year 
    •    Time range : ​​2003 - 2019 
    •    Geographic coverage (if applicable): State
### 4. Unit of Observation
#### What does one row in the dataset represent?
Each row represents the total taxes that were collected for a specific year for a specific city. 
### 5. Data Quality & Cleaning
Converted strings that represented Year to int values
### 6. Limitations of the Dataset
This data is limited in the time that spans, as it is between 2003 - 2019, so it does not take into account current trends and is pre covid data. 
### 7. How This Dataset Fits Into the Project
This data can give good insight in the total amount of taxes that were collected on properties by the state. Based on how tax laws work in the state this could provide us some insight on the general buying trends within the state and how much new homebuyers contributed to tax revenue. 


___ 

## Housing Units Dataset 
### 1. Source of the Data
Where does the dataset come from?
United States Census Bureau 
Link :
https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-housing-units.html
https://www.census.gov/programs-surveys/popest/technical-documentation/research/evaluation-estimates/2020-evaluation-estimates/2010s-totals-housing-units.html
https://www.census.gov/data/tables/time-series/demo/popest/intercensal-2000-2010-housing-units.html
### 2. What the Dataset Contains
    •    Overall description: Census Estimates on the number of housing units within the state of California. 
### 3. Data Organization
    •    Format: XLSX  ->  CSV 
    •    Dimensions (Rows x Columns): 00-09:(59,14) 10-19:(59,12) 20-24:(59, 7)
    •    Structure: Each row represents a specific cities estimated number of housing units within a given range of years 
    •    Time range : ​​2000 - 2009, 2010 - 2019, 2020 - 2024  
    •    Geographic coverage (if applicable): State
### 4. Unit of Observation
#### What does one row in the dataset represent?
Each row represents a specific cities estimated number of housing units within a given range of years. Each column represents a YEARLY estimate. 
### 5. Data Quality & Cleaning
Converted strings that represented Year to int values
Converted strings to ints for estimate data 
### 6. Limitations of the Dataset
These are estimates created the census bureau so these may not be accurate to a T, however institution generating these values is a trusted source. This is not exactly new housing units built but can be derived from it. 
### 7. How This Dataset Fits Into the Project
This data can give good insight into the total number of homes that are in California giving us an insight into the total units out there. These aren’t necessarily single family homes or empty homes for sale but just raw numbers of houses out there. This is a good way to gauge the total population growth in terms of housing units. 
___ 

## CA Population Dataset 
### 1. Source of the Data
Where does the dataset come from?
Federal Reserve 
Link :
https://fred.stlouisfed.org/series/CAPOP
### 2. What the Dataset Contains
Overall description: Census estimates for U.S population from 1900 to 2024 
### 3. Data Organization
    •    Format: CSV
    •    Dimensions (Rows x Columns): (125, 2)
    •    Structure: Each row represents the estimated census population for a specific year 
    •    Time range : 1900 - 2024  
    •    Geographic coverage (if applicable): State
### 4. Unit of Observation
What does one row in the dataset represent?
One row represents the estimated census population for a specific year for a specific county witin California.
5. Data Quality & Cleaning
    - Converted strings that represented estimates to float values

6. Limitations of the Dataset
    - These are estimates created the census bureau so these may not be accurate to a T, however institution generating these values is a trusted source. 

7. How This Dataset Fits Into the Project
    - Knowing the population of California can give us an idea of the general population growth in California.
    - Can give us an idea of the general demand for housing in California.

___ 
Dataset Analysis:
Housing Units - Yearly (2000 - 2024) -  Use 
Debt Dataset - Quarterly  (1999 - 2024) - Use 
Property Tax - Yearly (2003-2019) - Not Useful 
Median Price - Yearly (1990-2025) - Use 

Common shared time (2000 - 2024)  YEARLY 

___ 
## Model's Implemented 
- Dataset Search and EDA = ca_pop_EDA.ipynb, debt_EDA.ipynb, median_price_EDA.ipynb, housing_price_analysis.ipynb property_tax_EDA.ipynb, housing_units_EDA.ipynb
- Linear Regression Model = regression_debt_price_unit.ipynb
- Logistic Regression Model = logistic_regression.ipynb
- Small Neural Network & Decision Tree w/ Feature Permeance = small_neural.ipynb
- SQL Querying for Datasets = SQL-database.ipynb
                

## Original Project Proposal: 
https://docs.google.com/document/d/1UEKSPVgGHj_XSsh-tD3FvK-E0BKICGmghwmHqhi8EWo/edit?usp=sharing 

## Revisions: 
https://docs.google.com/document/d/1IyJpNT5hduANF2altTnuHc1tp0TJyeEA5oyGJA5PeJM/edit?usp=sharing

## Progress Report: 
https://docs.google.com/document/d/1OwlQwWAIElfaNmId2wzfRmYrEpjc61Yi4AhWUQHFt6c/edit?usp=sharing

