# Election_Analysis

## Overview of Election Audit

This election audit was conducted to support Colorado board of elections employee, Tom.  His request was to audit the tabulated results for a U.S.congressional precinct in Colorado proceeding with the automation way with Python instead of Excel. A report was generated to present the results below to the election commission.

 - The total number of votes cast in this congressional election. 
 - The total number of votes and the percentage of votes for each county. 
 - The largest county turnout. 
 - The total number of votes and the percentage of votes for each candidate.
 - The winner of the election with their vote count and percentage of the total votes. 

# Election Audit Results 

The dataset was collected from CSV file chaining with the following script.

    file_to_load = os.path.join(".", "Resources", "election_results.csv")

Based on this analysis, the results are as follows: 

![This is an image](https://github.com/tomoko1T/Election_Analysis/blob/main/Resources/ElectionResults.png) 

The script detail is found [GitHub Pages](https://github.com/tomoko1T/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Election Audit Summary 

This election audit has proved that this method with python could be applied to any election as long as the dataset is collected in csv format.  It saves time to summarize the election results rather than using excel.  Chaining style is clean and simple to load the dataset.

By loop, the information of each row such as each county and candidate is collected efficienty.  In addition to county and candidate name in the current csv, their voting method information can be added to find out which method is the most popular method.  This may help to analyze how to promote the participation for the election as well.
