# Analysis of Nobel Prizes through Visualizations

## Project Overview 

- Explored Nobel Prizes awarded over a period of a hundred years through detailed vizualizations.
- Explored different vizualization methods such as Seaborn and Plotly to effectively display the data
- Detailed analysis of what contributes to being a Nobel Prize awardee.

## Data Exploration 

Data exploration through vizualization always provides interesting insights into a dataset. This vizualization project has focused on Nobel prizes awarded over a period of more than a hundred years. These data explorations through bar graphs and scatter plots provide a clear picture of the background of the awardees. Several columns contain missing values and these can also be vizualized through Python modules. Although it is not apparent why there are so few female awardees over the years, key insights about the dataset can be obtainbed through age, gender and category related visualizations.

### 1. Missing Values Visualized 

The graphs below illustrate the number of missing values in each column. 
The empty lines inside the matix correspond to the missing values. The heatmap vizualizes the correlation between the missing values in each column.

#### a. Bar Graph of Missing Values![](Images/i.png?raw=true "Bar Graph of Missing Values")
#### b. Matrix of Missing Values![](Images/j.png?raw=true "Title")
#### c. Correlation Heatmap ![](Images/k.png?raw=true "Title")


### 2. Number of Nobel Prizes Awarded over the Years in all Categories

![Title](Images/a.png?raw=true "Title")


### 3. Number of Nobel Prizes Awarded by Gender (1996-2016)

![Title](Images/b.png?raw=true "Title")


### 4. Number of Individuals who Received Awards in each Category (2006-2016)

![Title](Images/c.png?raw=true "Title")

### 5. Age Distribution of Nobel Prize Awardees

![Title](Images/e.png?raw=true "Title")


### 6. Relplot of Age vs Years, indexed by hue (Category) and circle size (Prize Share)
Scatterplot with varying point sizes and hues

![Title](Images/f.png?raw=true "Title")


### 7. Relplot of Age vs Years, indexed by hue (Category) and circle size (Gender)
Scatterplot with varying point sizes and hues.

Observation : Note the disparity between the number of men and women awarded over the years

![Title](Images/g.png?raw=true "Title")

### 8. Conditional Kernel Density Estimate for each Category

![Title](Images/h.png?raw=true "Title")

### 9. Stacked Histogram on a Log Scale
Number of awards in each category displayed on a logarithmic scale.

![Title](Images/l.png?raw=true "Title")

### 10. Relplot of Age vs Years plotted for both Genders 
This plot is an extension of Figure 10.

![Title](Images/m.png?raw=true "Title")


![Title](Images/a1.png?raw=true "Title")

### 11. Line plots of Ages of Awardees in all Categories
These plots display the age at which individuals received the Nobel Prizes oveer the years. 

![Title](Images/a3.png?raw=true "Title")


## General Observations 

### a. By Gender 

- Men are more likely to be awarded a Nobel Prize in all categories.
- Women are more likely to receive a Nobel Prize in Peace or Literature
- Women awarded too few Physics and Economics awards to produce a box plot. 


### b. By Category

- Median age is lower for women in Chemistry, Peace and Physics categories.
- Medicine has the highest number of awardees among all categories. 


### c. By Age 

- The highest median ages to receive a Nobel Prize are in Economics and Literature.
- Physics laureates are the youngest among all prize categories.
- The average age of Nobel Prize laureates has increased over the years. 


### d. By Country and City

- Individuals born in the United States have been awarded the most number of prizes in Science categories.
- Individuals from the University of California system have been awarded the highest number of prizes.
- Individuals born in New York City have received the highest number of Nobel Prizes.






