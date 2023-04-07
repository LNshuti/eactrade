## Using Network Analysis to Understand International trade

A country is said to have a trade *imbalance* if the country imports more than it exports. By calculating the trade balance, we can express trade relationship between countries as an undirected graph a.k.a a **Markov network** in statistical literature.

```
Trade balance = exports - imports
```

**Data Source**
---------------
As in my [other work](https://github.com/LNshuti/LNSHUTI.github.io), I use the Atlas of Economic Complexity from the Growth Lab at Harvard University because this data source is: 1) Detailed down to the product level that each country in the World trades from 1962 to 2019. 2) Standardized to simplify the process of building time series to track changes over time. 3) Regularly used and highly cited source with over *eighty thousand downloads*. It is also publicly available and can be downloaded [**here.**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/H8SFD2)

**EDA: Exploratory Data Analysis**
--------------------------------

**Demographics**
| Indicator | Rwanda Population Data |					
|----------------------------------------------------|				
| Total Population (2020) | 12,952,218 |					
| Population growth (annual %) (2020) | 2.58 |					
| Urban population (% of total population) (2020) | 17.57 |					
| Rural population (% of total population) (2020) | 82.43 |					
| Population density (people per sq. km of land area) (2020) | 525.22 |					
| Age Dependency Ratio (% of working-age population) (2020) | 73.59 |					
| Fertility rate, total (births per woman) (2018) | 4.0 |					
| Poverty headcount ratio at national poverty lines (% of population) (2016-2017) | 38.2 |					
| Life expectancy at birth, total (years) (2018) | 68.7 |					
| Population, ages 0-14 (% of total) (2020) | 39.57 |					
| Population, ages 15-64 (% of total) (2020) | 56.14 |					
| Population, ages 65 and above (% of total) (2020) | 4.29 |					


| Indicator                              | Uganda Population Data          |
|-----------------------------------------|----------------|------|
| Total Population  (2020)                       | 45,741,007     | 
| Population Growth Rate (annual %)  (2020)          | 3.15%          |
| Male Population  (2020)                            | 22,800,493     | 
| Female Population  (2020)                          | 22,940,514     | 
| Urban Population  (2020)                            | 9,330,403      | 
| Rural Population   (2020)                         | 36,410,604     | 
| Population Density (people per sq. km) (2020)      | 229.69         | 
| Age Dependency Ratio   (2020)                     | 100.88         | 
| Youth Literacy Rate (15-24 years) (2020)          | 82.25%         | 
| Life Expectancy at Birth   (2020)                 | 63.37 years    | 

**Summary table for the population of Kenya** 

| Year | Population    | Yearly % Change | Yearly Change | Migrants (net) | Median Age | Fertility Rate | Population Density |
|------|---------------|-----------------|---------------|---------------|------------|----------------|--------------------|
| 2021 | 54,985,698    | 2.35%           | 1,263,985     | -10,000       | 20.2       | 3.64           | 93.0               |
| 2020 | 53,684,456    | 2.30%           | 1,199,696     | -22,989       | 19.7       | 3.65           | 90.0               |
| 2019 | 52,572,682    | 2.28%           | 1,167,794     | -40,000       | 19.1       | 3.66           | 88.1               |
| 2018 | 51,401,880    | 2.26%           | 1,131,429     | -40,000       | 19.5       | 3.52           | 86.2               |
| 2017 | 50,278,424    | 2.69%           | 1,310,247     | -30,000       | 19.4       | 3.9            | 84.4               |
| 2016 | 48,895,434    | 2.99%           | 1,422,713     | -20,000       | 18.9       | 4.09           | 82.0               |
| 2015 | 47,476,954    | 3.20%           | 1,489,934     | -20,000       | 18.5       | 4.35           | 79.7               |


Below we plot trade the 2020 trade balances for a select group of African countries. In order to compare apples to apples, we need to weight the trade balance by population. This is because countries with larger populations tend to have larger trade balances. 

### East African Community (EAC)
The East African Community consists of the following countries: Rwanda, Kenya, Uganda, Tanzania, Burundi, the Democratic Republic of Congo and South Sudan. Using 2021 data from the world bank, we plot annual exports/imports of goods only(not including services) of 5 of the EAC countries in **blue** with non-EAC country comparisons. 


![eac_trade_goods](https://user-images.githubusercontent.com/13305262/221357099-99bfd667-d185-4d6a-9bdd-f2213fb68e7d.png)

**References**
--------------
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2
