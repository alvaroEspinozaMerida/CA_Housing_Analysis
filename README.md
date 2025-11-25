## Running with UV 



# Professor Feedback from Proposal 

Feedback from Professor:

- I’d recommend starting with multiple linear regression and investigating the 
regression coefficients -- do a small number of variables account for most of the 
predictive ability or are there many small contributions from a larger number of variables?
Current Status:
- created regreesion model for each region in CA
- write report on model results

Feedback from Professor:

- One of the problems that you’re going to run into may be non-stationarity.
To accurately predict housing prices you would almost certainly need data other
than housing prices -- like macroeconomic and financial data (how much debt people have,
how much people spend, amount of new housing built, age of existing housing stock) 
as well as any changes in housing laws or taxation (mortgage deductions,
first-time homeowner incentives, etc.). Remember the housing crash around 2008.
Don’t be a turkey!
Current Status:
- start looking for new datasets that cover macroeconomic and financial data 


Feedback from Professor:
- Maybe the right place to start is to look at the distribution of housing
prices changes over time.  What family of distribution does it come from? 
Is it more like the normal (Gaussian) or like the Pareto (or log-normal)?
This is a tough question to answer with confidence,but you can at least check
whether the normal distribution is ruled out for something more fat tailed.

Current Status:
- Create Scatterplot for each region in CA
- Create report on these scatterplot distributions



Feedback from Professor:
- An alternative would be to look at different regions (cities or counties) in CA,
look at the average or median price in CA, and then try to predict which regions
will have average/median prices grow faster or slower than the state average/median
(not simply higher average/median, but faster growing). 
That may be less noisy and more predictable than trying to predict prices of individual houses.

Current Status:
- calculated descriptive statistics for each region in CA


