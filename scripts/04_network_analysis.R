library(igraph)
library(tidyverse)
# library(network)
# library(visNetwork)
# library(networkD3)


# A random graph has two parameters: N and P where N represents the number of nodes, 
# and P the probability distribution that connects a given set of nodes.
# A node is a vertex of a graph.
# An edge is a connection or link between nodes.

rwanda_trade_df <- 
  read_csv("rwandatrade/processed/rwa_sum_features.csv") %>% 
  #mutate(unique_identifier = cat()) %>%
  filter(year == "2019") 

simple_edge_df <-
  rwanda_trade_df %>% 
  mutate(partner_product_id = paste0(partner_id, product_id)) %>%
  mutate(partner_product_id = as.integer(partner_product_id)) %>%
  mutate(imports = as.integer(imports)) %>%
  select(partner_product_id, imports) %>%
  #rowid_to_column("id") %>% 
  unique() %>%
  sample_n(10)

# simple networks with vertices =======================================================
simple_vertex_df <-
  simple_edge_df %>%
  select(partner_product_id, imports) %>%
  unique()

g4 <- graph(c("metals", "special transactions", "metals","cement", "metals","telecom" ),
            isolates=c("60164056", "52215168", "45673992", "37488872") )

# In named graphs we can specify isolates by providing a list of their names.
plot(g4, edge.arrow.size=.5, vertex.color="gold", vertex.size=15,
     vertex.frame.color="gray", vertex.label.color="black",
     vertex.label.cex=0.8, vertex.label.dist=2, edge.curved=0.2)



# References
# https://www.jessesadler.com/post/network-analysis-with-r/