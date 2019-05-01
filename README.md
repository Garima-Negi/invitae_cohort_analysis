# invitae_cohort_analysis

This code performs a cohort analysis on customers to help identify changes in ordering behavior based on their signup date.
We analyse the number of customers who made their first purchase in first, second or third week after signing up.

The script cohort2.py takes the following inputs:

* starting signup date for cohort
* ending signup date for cohort
* the path to a customers CSV file (see customers.csv for example format)
* the path to an orders CSV file (see orders.csv for example format)

## Example Input
```python cohort2.py 4/05/2015 4/08/2015 customers.csv orders.csv```

## Example Output
```
Cohort: 4/05/2015 - 4/08/2015
Customers: 363
Week 1: 10.192837465564738% customers (37) / 10.192837465564738% 1st time (37)
Week 2: 4.132231404958678% customers (15) / 1.3774104683195594% 1st time (5)
Week 3: 4.40771349862259% customers (16) / 0.8264462809917356% 1st time (3)
```
