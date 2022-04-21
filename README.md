## Using Network Analysis to Understand International trade

#### Definitions
- **A random graph** has two parameters: *N* and *P* where *N* represents the number of nodes, and *P* the probability distribution that connects a given set of nodes. **A node** is a vertex of a graph while **An edge** is a connection or link between **nodes**.

To perform network analysis in R, we use two *tidygraph* and *ggraph*, both of which support common graph data structures like **dendrogram** and **igraph** from the *igraph* R package.

##### Data Source
As in my [other work](https://github.com/LNshuti/LNSHUTI.github.io), I use the Atlas of Economic Complexity from the Growth Lab at Harvard University because this data source is: 1) Detailed down to the product level that each country in the World trades from 1962 to 2019. 2) Standardized to simplify the process of building time series to track changes over time. 3) Regularly used and highly cited source with over *fifty thousand downloads*. It is also publicly available and can be downloaded [**here.**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/H8SFD2)


#### Conclusions



#### **References**
- Sadler, Jesse. Network Analysis with R. https://www.jessesadler.com/post/network-analysis-with-r/
- https://cran.r-project.org/web/packages/ggraph/vignettes/tidygraph.html
- https://www.data-imaginist.com/2017/ggraph-introduction-layouts/
- Katherine Ognyanova. Network analysis with R and igraph: NetSci X Tutorial.
  https://kateto.net/networks-r-igraph
- Matthew Kay (2021). tidybayes: Tidy Data and Geoms for Bayesian Models. R package version 3.0.2, https://mjskay.github.io/tidybayes/. DOI: 10.5281/zenodo.1308151.
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2