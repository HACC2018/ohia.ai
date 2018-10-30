library(data.table)

# load data
DT <- fread('data/plant_meta.csv')

# combine genus with multiple species
select_species <- DT[, .(x=species[1]), keyby=genus]$x
DT <- DT[species %in% select_species]

# clean text
clean_text <- function(x) {
  x <- gsub('\n', ' ', x)         # replace new lines with space
  x <- gsub('\\[\\d+\\]', '', x)  # remove references [\\d+]
  x <- gsub('\\"+', '\\"', x)     # remove double quotes
  x <- gsub('\\s+', ' ', x)       # remove extra whitespace
  x <- trimws(x)                  # remove leading and trailing ws
  x
}
DT[, description := clean_text(description)]
DT[, story := clean_text(story)]
DT[, uses := clean_text(uses)]

# change common to non-native
DT[status=='common', status := 'non-native']

# capatilize all words
capatilize_all <- function(x) {
  s <- strsplit(x, " ")[[1]]
  paste(toupper(substring(s, 1, 1)), substring(s, 2), sep="", collapse=" ")
}
DT[, hawaiian_name := sapply(hawaiian_name, capatilize_all)]
DT[, common_name := sapply(common_name, capatilize_all)]
DT[, status := sapply(status, capatilize_first)]

# capatilize first word
capatilize_first <- function(x) {
  paste0(toupper(substr(x,1,1)), substring(x,2))
}
DT[, scientific_name := sapply(scientific_name, capatilize_first)]
DT[, species := sapply(species, capatilize_first)]
DT[, genus := sapply(genus, capatilize_first)]

# reassign plant_name
DT[, species_count := .N, keyby=genus]
DT[, plant_name := ifelse(species_count==1, genus, species)]

# reorder columns
DT[, species_count := NULL]
setcolorder(DT, c(
  'plant_name', 'status', 'hawaiian_name', 'common_name', 'scientific_name',
  'genus', 'species', 'description', 'story', 'uses'
))

fwrite(DT, 'data/plant_meta_v3.csv')
