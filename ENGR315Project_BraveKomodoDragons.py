import numpy as np
import pandas as pd
#import scipy.stats

file_path = '../../Global_Endangered_Wildlife.csv'

data = pd.read_csv(file_path)
df = pd.DataFrame(data)

#Question 1
#For all animal classes, what percent of primary threats are not poaching/overhunting, invasive species, 
#nor pollution? The Class and Primary_Threat variables will be the main potential elements analyzed to 
#answer this question. We will need the percentages of each threat for this question. Thus, we will need 
#to get a count of each individual threat category and then divide it by 10,000 since there are 10,000 
#animals in the dataset. To make things easier, we can filter out data that does not concern the Class 
#and Primary_Threat variables. For coding, NumPy can be used for the math and we can use lists and 
#conditional statements to ensure proper filtering. For visualization, we can make a pie chart for 
#easy viewing. From the results of this question, we plan to find the animals with the lowest populations.
#This can help us research which animals are in the most danger and actually find support with this from
#online sources

primary_threat = df["Primary_Threat"]

#find each threat
if primary_threat == "Climate Change":
    climate_count = np.count_values(primary_threat == "Climate Change")
    climate_percent = climate_count / 10000
if primary_threat == "Disease":
    disease_count = np.count_values(primary_threat == "Disease")
    disease_percent = disease_count / 10000
if primary_threat == "Habitat Loss":
    habitat_count = np.count_values(primary_threat == "Habitat Loss")
    habitat_percent = habitat_count / 10000
sum_threat = climate_percent + disease_percent + habitat_percent

print("The percent of primary threats that are not Poaching/Overhunting, Invasive Species, or Pollution are:",
      climate_percent, disease_percent, habitat_percent, sum_threat)







#Question 2
#Is the estimated percentage of historical natural habitat loss for mammals greater than or equal to 50%? 
#The Class, Habitat_Loss_Percentage, and Estimated_Wild_Population will be the main potential elements 
#analyzed to answer this question. We will need to filter the other classes out to only have mammal data. 
#After, we can use scipy.stats to find our sample mean, standard deviation, sample, size, and test statistic. 
#We can then run a One-Sample T-Test to compare our P-value to our alpha. For visualization, a box and whisker
#plot may be the best option, as it'll show the spread of the data.




#Question 3
#Is there an association between geographical region and primary threat factor? The Primary_Region and 
#Primary_Threat will be the main potential elements analyzed to answer this question. We will need to filter
#to focus on the Primary_Region and Primary_Threat variables. We can use scipy.stats to find our observed and
#expected values and run a Chi-Square Test of Independence. For visualization, a grouped bar chart is going 
#to be the best option, as it will show the both the regions and their associated threats, as well as the 
#count of species on the y-axis.