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
