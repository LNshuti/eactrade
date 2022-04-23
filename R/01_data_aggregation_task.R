repo_ <- "eactrade"
source(paste0(repo_, "/R/manifest.R"))

country_ids <- 
  read_csv("eactrade/data/countries_codes_and_coordinates.csv") %>%
  janitor::clean_names() %>%
  select(alpha_3_code, numeric_code) %>%
  filter(alpha_3_code %in% c("RWA","UGA","TZA","BDI", "COD", "KEN"))  %>%
  mutate(numeric_code = as.character(numeric_code))

#Combine trade data from 2015 to 2019
trade_data_all_years <-
 list.files(paste0("dataverse_files"), recursive = TRUE) %>%
 as_tibble() %>%
 filter(grepl(pattern = "partner_sitcproduct4digit", x = value)) %>%
 pull(value)

allcountries_trade_df <-
 trade_data_all_years %>%
 map(~data.table::fread(file = paste0("dataverse_files/",.x)) %>%
       janitor::clean_names() %>% as_tibble() %>%
       mutate_all(as.character)
     ) %>%
 bind_rows() %>% as_tibble() 


eaccountries_trade_df <- 
  allcountries_trade_df %>%
  inner_join(country_ids, by = c("location_id" = "numeric_code")) %>%
  rename(to = alpha_3_code) %>%
  inner_join(country_ids, by = c("partner_id" = "numeric_code")) %>%
  rename(from = alpha_3_code)  %>%
  select(-location_id, -partner_id) %>%
  select(from, to, everything())

saveRDS(object = eaccountries_trade_df, "eactrade/data/processed/eac_trade_df_2015_2019.rds")