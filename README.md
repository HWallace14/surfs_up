# Surfs_Up

## Overview

### Purpose

For this analysis we were tasked with using SQLite to query a database containing varying data from hawaii with two main tables, Measurement and Station. Specifically for this challenge the queries were pertaining to the temperature measurements found in both June and December across all stations.

## Results

### June Temperature Results

June data results:

* The average temperature was 74.94 degrees Fahrenheit.
* The hottest it ever got was 85 degrees Fahrenheit.
* the coldest it ever got was 64 degrees Fahrenheit.

<img width="108" alt="June_temps" src="https://user-images.githubusercontent.com/105998378/182982039-90008b23-273e-492d-a0b3-2fd9f093e0c0.png">

### December Temperature Results

December data results:

* Average temperature was 71.04 degrees Fahrenheit.
* Hottest it got was 83 degrees Fahrenheit.
* Coldest it got was 56 degrees Fahrenheit.

<img width="124" alt="December_temps" src="https://user-images.githubusercontent.com/105998378/182982289-749cb524-d9f8-47c4-a447-ca21ce79620d.png">

## Summary

### June vs December

The temperature in Hawaii doesn't seem to vary all that often depending on the season. As seen above, the average temperature only dropped by a little under 4 degrees for one of the warmer months versus one of the colder months. The max temperature was similarly unaffected by the time of year, with the difference between the two months being an astonishing 2 degrees. Where we did see a marked change, at least so far as there are changes in Hawaii's weather, was in the difference between the coldest temperatures. There we saw a difference of 8 degrees, which is only significant compared to the 2 or 4 degree changes we saw in other categories. Considering the fact that a lot of other states end up well below freezing in December, I believe this analysis can conclude with certainty that Hawaii is a relatively stable climate year-round.

### Ideas for different queries

If I were to query the weather differently for the same months to compare the results I would probably do it one of two ways:

1) Add in another filter where you extract the year and group the results by year and month just to see if the climate remained the same year after year or if it was only relatively stable when looked at with a longer view of things.

2) Import datetime and pick out a single year, then create a variable with a timedelta of 30 days from the end of the months and filter it by that. 
