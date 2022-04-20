# Examples from the Networkx package by 
# Carter T. Butts buttsc@uci.edu and David Hunter dhunter@stat.psu.edu

# networks from data frames ===========================================================
#* simple networks ====================================================================
simple_edge_df <- data.frame(
  from = c("b", "c", "c", "d", "a"),
  to = c("a", "b", "a", "a", "b"),
  weight = c(1, 1, 2, 2, 3),
  stringsAsFactors = FALSE
)

as.network(simple_edge_df)

# simple networks with vertices =======================================================
simple_vertex_df <- data.frame(
  name = letters[1:5],
  residence = c("urban", "rural", "suburban", "suburban", "rural"),
  stringsAsFactors = FALSE
)
simple_vertex_df

as.network(simple_edge_df, vertices = simple_vertex_df)

as.network(simple_edge_df,
           directed = FALSE, vertices = simple_vertex_df,
           multiple = TRUE
)

#* splitting multiplex data frames into multiple networks =============================
simple_edge_df$relationship <- c(rep("friends", 3), rep("colleagues", 2))
simple_edge_df

lapply(split(simple_edge_df, f = simple_edge_df$relationship),
       as.network,
       vertices = simple_vertex_df
)

#* bipartite networks without isolates ================================================
bip_edge_df <- data.frame(
  actor = c("a", "a", "b", "b", "c", "d", "d", "e"),
  event = c("e1", "e2", "e1", "e3", "e3", "e2", "e3", "e1"),
  actor_enjoyed_event = rep(c(TRUE, FALSE), 4),
  stringsAsFactors = FALSE
)
bip_edge_df

bip_node_df <- data.frame(
  node_id = c("a", "e1", "b", "e2", "c", "e3", "d", "e"),
  node_type = c(
    "person", "event", "person", "event", "person",
    "event", "person", "person"
  ),
  color = c(
    "red", "blue", "red", "blue", "red", "blue",
    "red", "red"
  ),
  stringsAsFactors = FALSE
)
bip_node_df

as.network(bip_edge_df, directed = FALSE, bipartite = TRUE)
as.network(bip_edge_df, directed = FALSE, vertices = bip_node_df, bipartite = TRUE)

#* bipartite networks with isolates ===================================================
bip_nodes_with_isolates <- rbind(
  bip_node_df,
  data.frame(
    node_id = c("f", "e4"),
    node_type = c("person", "event"),
    color = c("red", "blue"),
    stringsAsFactors = FALSE
  )
)
# indicate which vertices are actors via a column named `"is_actor"`
bip_nodes_with_isolates$is_actor <- bip_nodes_with_isolates$node_type == "person"
bip_nodes_with_isolates

as.network(bip_edge_df,
           directed = FALSE, vertices = bip_nodes_with_isolates,
           bipartite = TRUE
)

#* hyper networks from data frames ====================================================
hyper_edge_df <- data.frame(
  from = c("a/b", "b/c", "c/d/e", "d/e"),
  to = c("c/d", "a/b/e/d", "a/b", "d/e"),
  time = 1:4,
  stringsAsFactors = FALSE
)
tibble::as_tibble(hyper_edge_df)

# split "from" and "to" at `"/"`, coercing them to list columns
hyper_edge_df$from <- strsplit(hyper_edge_df$from, split = "/")
hyper_edge_df$to <- strsplit(hyper_edge_df$to, split = "/")
tibble::as_tibble(hyper_edge_df)

as.network(hyper_edge_df,
           directed = FALSE, vertices = simple_vertex_df,
           hyper = TRUE, loops = TRUE
)

# convert network objects back to data frames =========================================
simple_g <- as.network(simple_edge_df, vertices = simple_vertex_df)
as.data.frame(simple_g)
as.data.frame(simple_g, unit = "vertices")

bip_g <- as.network(bip_edge_df,
                    directed = FALSE, vertices = bip_node_df,
                    bipartite = TRUE
)

as.data.frame(bip_g, unit = "vertices")

hyper_g <- as.network(hyper_edge_df,
                      directed = FALSE, vertices = simple_vertex_df,
                      hyper = TRUE, loops = TRUE
)

as.data.frame(hyper_g, unit = "vertices")
