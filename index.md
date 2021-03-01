# Analysis of Nobel Prizes through Visualizations

## Project Overview 

- Explored Nobel Prizes awarded over a period of a hundred years through detailed vizualizations.
- Explored different EDA packages such as **Seaborn and Plotly** to effectively display the data insights.
- Detailed visual analysis of what contributes to being a Nobel Prize awardee.

## Data Exploration 

Data exploration through vizualization always provides interesting insights into a dataset. This vizualization project has focused on Nobel prizes awarded over a period of more than a hundred years. These data explorations through bar graphs and scatter plots provide a clear picture of the background of the awardees. Several columns contain missing values and these can also be vizualized through Python modules. Although it is not apparent why there are so few female awardees over the years, key insights about the dataset can be obtainbed through age, gender and category related visualizations.

### 1. Missing Values Visualized 

The graphs below illustrate the number of missing values in each column. 

#### a. Bar Graph of Missing Values![](Images/i.png?raw=true "Bar Graph of Missing Values")
This grapgh shows the number of missing values in each column (feature).

#### b. Matrix of Missing Values![](Images/j.png?raw=true "Title")
The empty lines inside the matix correspond to the missing values.

#### c. Correlation Heatmap ![](Images/k.png?raw=true "Title")
The heatmap vizualizes the correlation between the missing values in each column. 

### 2. Number of Nobel Prizes Awarded over the Years in all Categories

![Title](Images/a.png?raw=true "Title")


### 3. Number of Nobel Prizes Awarded by Gender (1996-2016)

![Title](Images/b.png?raw=true "Title")


### 4. Number of Individuals who Received Awards in each Category (2006-2016)

![Title](Images/c.png?raw=true "Title")

### 5. Age Distribution of Nobel Prize Awardees 
This graph represents a kernel density estimate (kde), which is used to visualize the distribution of observations related to a particular feature.
The solid line represents the expected distribution and the histogram represents the distribution of the 'Age' feature. This graph essentially represents the underlying probability density function of the distribution.

![Title](Images/e.png?raw=true "Title")

The above graph can be further elaborated to represent the age distribution of each category.

![Title](Images/kde.png?raw=true "Title")


### 6. Relplot of Age vs Years, indexed by hue (Category) and circle size (Prize Share)
Scatterplot with varying point sizes and hues

![Title](Images/f.png?raw=true "Title")


### 7. Relplot of Age vs Years, indexed by hue (Category) and circle size (Gender)
Scatterplot with varying point sizes and hues.

Note the disparity between the number of men and women awarded over the years

![Title](Images/g.png?raw=true "Title")

### 8. Conditional Kernel Density Estimate for each Category

![Title](Images/h.png?raw=true "Title")

### 9. Stacked Histogram on a Log Scale
Number of awards in each category displayed on a logarithmic scale.

![Title](Images/l.png?raw=true "Title")

### 10. Relplot of Age vs Years plotted for both Genders 
This plot is an extension of Figure 6, with the axes reversed.

![Title](Images/m.png?raw=true "Title")


### 11. Line plots of Ages of Awardees in all Categories
These plots display the age at which individuals received the Nobel Prizes over the years. 

![Title](Images/a3.png?raw=true "Title")

### 12. Country, City and Organization based Graphs
These charts display the top 20 (by count) countries, cities and organizations that have received Nobel Prizes.

#### a. Country of Birth 

![Title](Images/b1.png?raw=true "Title") 
![Title](Images/a11.png?raw=true "Title") 

#### b. City of Birth

![Title](Images/b2.png?raw=true "Title") 
![Title](Images/a13.png?raw=true "Title") 

#### c. Organization Affiliated With 

![Title](Images/b3.png?raw=true "Title")
![Title](Images/a12.png?raw=true "Title") 

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


## Final Note 

Based on the visual analyses performed above, the most favorable path to become a Nobel Prize laureate is to be a male from the United States, to be born in New York City and to have studied or worked in the University of California system. 



