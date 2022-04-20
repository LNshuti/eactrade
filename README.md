## Using Network Analysis to Understand International trade

#### Definitions
- **A random graph** has two parameters: *N* and *P* where *N* represents the number of nodes, and *P* the probability distribution that connects a given set of nodes.

- **A node** is a vertex of a graph.

- **An edge** is a connection or link between **nodes**.

Given a dataframe with x features, we can express the data in a graph format as follows: 
**A Nodes tibble with features m**

**An esdges tibble with the following columns: from, to, feature 1...n**

#### Methods
Using the *tidygraph* and *ggraph* packages from R, we explore the following properties: 

- **hclust:** Hierarchical clustering
- **dendrogram**
- **phylo**
- **data.tree**
- **Adjacency matrices**
- **Adjacency lists**
- **Edge list**
- **Set memberships**
- **Incidence matrix**


##### Data Source
As in my [other work](https://github.com/LNshuti/LNSHUTI.github.io), I use the Atlas of Economic Complexity from the Growth Lab at Harvard University because this data source is: 1) Detailed down to the product level that each country in the World trades from 1962 to 2019. 2) Standardized to simplify the process of building time series to track changes over time. 3) Regularly used and highly cited source with over *fifty thousand downloads*. It is also publicly available and can be downloaded [**here.**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/H8SFD2)

##### Introduction 


##### Methods 



#### Conclusions



#### **References**
- Sadler, Jesse. Network Analysis with R. https://www.jessesadler.com/post/network-analysis-with-r/
- Katherine Ognyanova. Network analysis with R and igraph: NetSci X Tutorial.
  https://kateto.net/networks-r-igraph
- Matthew Kay (2021). tidybayes: Tidy Data and Geoms for Bayesian Models. R package version 3.0.2, https://mjskay.github.io/tidybayes/. DOI: 10.5281/zenodo.1308151.
- The Growth Lab at Harvard University. International Trade Data (SITC, Rev. 2). 2019-05-31. 2019. V5. Harvard Dataverse. URL. https://doi.org/10.7910/DVN/H8SFD2. doi/10.7910/DVN/H8SFD2