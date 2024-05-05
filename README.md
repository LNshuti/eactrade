## Using Network Analysis to Understand International trade

A country is said to have a trade *imbalance* if the country imports more than it exports. 

```
Trade balance = exports - imports
```

**Data Source**
---------------
I use the Atlas of Economic Complexity from the Growth Lab at Harvard University because this data source is: 1) Detailed down to the product level that each country in the World trades from 1962 to 2019. 2) Standardized to simplify the process of building time series to track changes over time. 3) Regularly used and highly cited source with over *eighty thousand downloads*. It is also publicly available and can be downloaded [**here.**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/H8SFD2)

**EDA: Exploratory Data Analysis**
--------------------------------

**Demographics**

**The population of Kenya** 

| Year | Population    | Yearly % Change | Yearly Change | Migrants (net) | Median Age | Fertility Rate | Population Density |
|------|---------------|-----------------|---------------|---------------|------------|----------------|--------------------|
| 2021 | 54,985,698    | 2.35%           | 1,263,985     | -10,000       | 20.2       | 3.64           | 93.0               |
| 2020 | 53,684,456    | 2.30%           | 1,199,696     | -22,989       | 19.7       | 3.65           | 90.0               |
| 2019 | 52,572,682    | 2.28%           | 1,167,794     | -40,000       | 19.1       | 3.66           | 88.1               |
| 2018 | 51,401,880    | 2.26%           | 1,131,429     | -40,000       | 19.5       | 3.52           | 86.2               |
| 2017 | 50,278,424    | 2.69%           | 1,310,247     | -30,000       | 19.4       | 3.9            | 84.4               |
| 2016 | 48,895,434    | 2.99%           | 1,422,713     | -20,000       | 18.9       | 4.09           | 82.0               |
| 2015 | 47,476,954    | 3.20%           | 1,489,934     | -20,000       | 18.5       | 4.35           | 79.7               |

**Kenyan Population Desnity Map: 2023**
![image](https://github.com/LNshuti/eactrade/assets/13305262/5e30e135-ab02-4d73-b47d-e63d2283d37e)


**The population of Rwanda and Uganda** 

| Indicator                                                  | Rwanda   | Uganda   |
|-------------------------------------------------------------|-----------------------|------------------------|
| Total Population (2020)                                     | 12,952,218            | 45,741,007             |
| Population growth (annual %) (2020)                         | 2.58                  | 3.15%                 |
| Urban population (% of total population) (2020)             | 17.57                 |25%                   |
| Rural population (% of total population) (2020)             | 82.43                 | 75%                  |
| Population density (people per sq. km of land area) (2020)  | 525.22                | 229.69                 |
| Age Dependency Ratio (% of working-age population) (2020)   | 73.59 %                 |  90%                |

**Uganda Population Density**
![image](https://github.com/LNshuti/eactrade/assets/13305262/7cf00c48-1dce-4157-9fef-10b6ded35e2a)

**Rwanda Population Density**
Below we plot trade the 2020 trade balances for a select group of African countries. In order to compare apples to apples, we need to weight the trade balance by population. This is because countries with larger populations tend to have larger trade balances. 

### East African Community (EAC)
The East African Community consists of the following countries: Rwanda, Kenya, Uganda, Tanzania, Burundi, the Democratic Republic of Congo and South Sudan. Using 2021 data from the world bank, we plot annual exports/imports of goods only(not including services) of 4 East African countries in **blue** with non-EAC country comparisons. 


![eac_trade_goods](https://user-images.githubusercontent.com/13305262/221357099-99bfd667-d185-4d6a-9bdd-f2213fb68e7d.png)

## **Imports by Country and Product**

**Agricultural Products**
-------------------------

**Rwanda**

![What did Rwanda import in 2020](https://user-images.githubusercontent.com/13305262/231676481-8cc5d45b-f932-4097-8dc3-b5945debf168.png)

**Kenya**

![What did Kenya import in 2020](https://user-images.githubusercontent.com/13305262/231682205-facefe08-d19c-48dc-99a8-43c5e5b0b851.png)

**Uganda**

![What did Uganda import in 2020](https://user-images.githubusercontent.com/13305262/231684963-ba59c419-0b72-48ec-a8a4-0364fd2055a9.png)

**Tanzania**

![What did Tanzania import in 2020](https://user-images.githubusercontent.com/13305262/231685703-fe1a48e0-283e-4401-ac94-f3a43b394a9e.png)

**Combined Chart**
![What did Eastern Africa export in 2020](https://user-images.githubusercontent.com/13305262/234193116-48032fe5-74b0-42d5-8a4b-ebefb8216a5f.png)


**References**
--------------
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2
