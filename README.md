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
|----------------------------------------------------|------------------------|					
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


| Indicator                              | Uganda Population Data          | Year |
|-----------------------------------------|----------------|------|
| Total Population                       | 45,741,007     | 2020 |
| Population Growth Rate (annual %)      | 3.15%          | 2020 |
| Male Population                        | 22,800,493     | 2020 |
| Female Population                      | 22,940,514     | 2020 |
| Urban Population                       | 9,330,403      | 2020 |
| Rural Population                       | 36,410,604     | 2020 |
| Population Density (people per sq. km) | 229.69         | 2020 |
| Age Dependency Ratio                   | 100.88         | 2020 |
| Youth Literacy Rate (15-24 years)      | 82.25%         | 2018 |
| Life Expectancy at Birth               | 63.37 years    | 2020 |

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

**Unrelated. USA and China.**


| Year | Population of China | Annual Growth Rate of China (%) | Population of the United States | Annual Growth Rate of the United States (%) |
|------|---------------------|----------------------------------|----------------------------------|--------------------------------------------|
| 2010 | 1,359,859,000       | 0.53                             | 309,349,000                       | 0.70                                       |
| 2011 | 1,364,921,000       | 0.37                             | 311,718,000                       | 0.77                                       |
| 2012 | 1,368,558,000       | 0.27                             | 314,058,000                       | 0.75                                       |
| 2013 | 1,371,495,000       | 0.21                             | 316,204,000                       | 0.68                                       |
| 2014 | 1,375,388,000       | 0.28                             | 318,563,000                       | 0.74                                       |
| 2015 | 1,378,665,000       | 0.24                             | 320,897,000                       | 0.73                                       |
| 2016 | 1,381,963,000       | 0.24                             | 323,128,000                       | 0.70                                       |
| 2017 | 1,386,050,000       | 0.30                             | 325,719,000                       | 0.80                                       |
| 2018 | 1,390,094,000       | 0.29                             | 327,170,000                       | 0.45                                       |
| 2019 | 1,397,175,000       | 0.51                             | 328,240,000                       | 0.33                



Below we plot trade the 2020 trade balances for a select group of African countries. In order to compare apples to apples, we need to weight the trade balance by population. This is because countries with larger populations tend to have larger trade balances. 

### East African Community (EAC)
The East African Community consists of the following countries: Rwanda, Kenya, Uganda, Tanzania, Burundi, the Democratic Republic of Congo and South Sudan. Using 2021 data from the world bank, we plot annual exports/imports of goods only(not including services) of 5 of the EAC countries in **blue** with non-EAC country comparisons. 


![eac_trade_goods](https://user-images.githubusercontent.com/13305262/221357099-99bfd667-d185-4d6a-9bdd-f2213fb68e7d.png)

## Individual country summary

Rwanda's top trade partners. With these countries, Rwanda exported more than it imported. This means that Rwanda had a **positive** trade balance.  

![rwanda_top_trade_partners](https://user-images.githubusercontent.com/13305262/221377782-41e9b06f-fcf7-49f7-8302-6c118a72bb68.png)
 
 **Negative trade balance**
![rwanda_bottom_trade_partners](https://user-images.githubusercontent.com/13305262/221378709-f9ab5605-cb23-4146-957e-2f1ebbda8e9f.png)


**References**
--------------
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2
