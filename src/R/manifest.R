# Load necessary libraries and functions
library(finnts)
library(data.table)
library(ggraph)
library(tidygraph)
library(gt)
library(leafdown)
library(imola)
library(rhino)
library(ggraph)
library(igraph)
library(graphlayouts)
library(gridExtra)
library(sparklyr)
library(networkD3)
library(tidyverse)

theme_tufte_revised <- function(base_size = 11, base_family = "Gill Sans", ticks = TRUE) {
  
  ret <- ggplot2::theme_bw(base_family = base_family, base_size = base_size) +
    ggplot2::theme(
      axis.line = ggplot2::element_line(color = 'black'),
      axis.title.x = ggplot2::element_text(vjust = -0.3),
      axis.title.y = ggplot2::element_text(vjust = 0.8),
      legend.background = ggplot2::element_blank(),
      legend.key = ggplot2::element_blank(),
      legend.title = ggplot2::element_text(face="plain"),
      panel.background = ggplot2::element_blank(),
      panel.border = ggplot2::element_blank(),
      panel.grid = ggplot2::element_blank(),
      plot.background = ggplot2::element_blank(),
      strip.background = ggplot2::element_blank()
    )
  
  if (!ticks) {
    ret <- ret + ggplot2::theme(axis.ticks = ggplot2::element_blank())
  }
  
  ret
}


my_theme <- 
  theme_classic(base_family = "Times") +
  theme(axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        panel.border = ggplot2::element_blank(),
        panel.grid = ggplot2::element_blank(),
        axis.line.y = element_blank(), 
        legend.background = element_rect()
  ) 


# Create function to convert dataframe to bipartite matrix
convert_to_bipartite <- function(df,id) {
  id <- enquo(id)
  nn <- df %>% pull(!!id)
  foo <- df %>% select(-!!id) %>%
    as.matrix()
  
  rownames(foo) <- nn
  foo
}
