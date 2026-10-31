# ENGR315-HabitatDatasetProject
The GitHub Repository of our ENGR 315 Project concerning Endangered Animals.

Project Title: ENGR 315 (Computational Methods in Engineering) Semester Project
Team Name: The Brave Komodo Dragons
Team Members/Contributors: Breanna Yeboah, Kacy Peters, Destiny Jones

Objective:
The dataset chosen for this project centers around endangered animals. It is a list of 10,000 different animals and contains information about their name, class, remaining population in the wild, IUCN Red List status, geographical region, percentage of habitat loss, and their primary threat conservation list. Our goal is to use the dataset to analyze the information and explore if there are any potential connections between our variables.

We will ask the following questions: 
1) For all animal classes, what percent of primary threats are not poaching/overhunting, invasive species, nor habitat loss?
2) Is the estimated percentage of historical natural habitat loss for mammals greater than or equal to 50%?
3) Is there an association between geographical region and primary threat factor?

Introduction:
Left blank for now, may be filled out later

Implementation Details:
1) For all animal classes, what percent of primary threats are not poaching/overhunting, invasive species, nor habitat loss?
The Class and Primary_Threat variables will be the main potential elements analyzed to answer this question. We will need the percentages of each threat for this question. Thus, we will need to get a count of each individual threat category and then divide it by 10,000 since there are 10,000 animals in the dataset. To make things easier, we can filter out data that does not concern the Class and Primary_Threat variables. For coding, NumPy can be used for the math and we can use lists and conditional statements to ensure proper filtering. For visualization, we can make a pie chart for easy viewing.

2) Is the estimated percentage of historical natural habitat loss for mammals greater than or equal to 50%?
The Class, Habitat_Loss_Percentage, and Estimated_Wild_Population will be the main potential elements analyzed to answer this question. We will need to filter the other classes out to only have mammal data. After, we can use scipy.stats to find our sample mean, standard deviation, sample, size, and test statistic. We can then run a One-Sample T-Test to compare our P-value to our alpha. For visualization, a box and whisker plot may be the best option, as it'll show the spread of the data. 

4) Is there an association between geographical region and primary threat factor?
The Primary_Region and Primary_Threat will be the main potential elements analyzed to answer this question. We will need to filter to focus on the Primary_Region and Primary_Threat variables. We can use scipy.stats to find our observed and expected values and run a Chi-Square Test of Independence. For visualization, a grouped bar chart is going to be the best option, as it will show the both the regions and their associated threats, as well as the count of species on the y-axis.


Results:

Conclusions:

Actions to be tested:

References/Source Files:
Kaggle Dataset: https://www.kaggle.com/datasets/yenigellagnandeep/global-endangered-wildlife-dataset
