## Using Network Analysis to Understand International trade

**Definitions**
------------------------
**A random graph** has two parameters: *N* and *P* where *N* represents the number of nodes, and *P* the probability distribution that connects a given set of nodes. **A node** is a vertex of a graph while **An edge** is a connection or link between **nodes**.

To perform network analysis in R, we use two packages; *tidygraph* and *ggraph*, both of which support common graph data structures implemented in the *igraph* R package.

One property of great interest in network analysis is **Community** defined as a subset of nodes with stronger connections than usual. In our analysis, we attempt to detect communities of trading partners based on the flow of goods betweeen countries. For example, we would like to test whether we can infer existing communities such as the **EAC** and **ECOWAS** based on the data.

A country is said to have a trade *imbalance* if the country imports more than it exports. By calculating the trade balance, we can express trade relationship between countries as an undirected graph a.k.a a **Markov network** in statistical literature.

```
Trade balance = exports - imports
```

**Data Source**
---------------
As in my [other work](https://github.com/LNshuti/LNSHUTI.github.io), I use the Atlas of Economic Complexity from the Growth Lab at Harvard University because this data source is: 1) Detailed down to the product level that each country in the World trades from 1962 to 2019. 2) Standardized to simplify the process of building time series to track changes over time. 3) Regularly used and highly cited source with over *eighty thousand downloads*. It is also publicly available and can be downloaded [**here.**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/H8SFD2)

**EDA: Exploratory Data Analysis**
--------------------------------

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
- Use Vaex and Streamlit to accomodate very large file sizes. https://vaex.io/blog/vaex-plus-streamlit-where-simplicity-meets-big-data

- Hastie, T., Tibshirani, R., Friedman, J.H. and Friedman, J.H., 2009. The elements of statistical learning: data mining, inference, and prediction (Vol. 2, pp. 1-758). New York: springer.

- Sadler, Jesse. Network Analysis with R. https://www.jessesadler.com/post/network-analysis-with-r/

- Katherine Ognyanova. Network analysis with R and igraph: NetSci X Tutorial.
  https://kateto.net/networks-r-igraph
  
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2
