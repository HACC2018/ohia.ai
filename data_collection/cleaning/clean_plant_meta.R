library(data.table)

# load data
DT <- fread('data/plant_meta_v4.csv')
DT[, created_at := NULL]
DT[, updated_at := NULL]
DT[, image_count := NULL]
DT[, id := .I]

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

# capatilize first word
capatilize_first <- function(x) {
  paste0(toupper(substr(x,1,1)), substring(x,2))
}
DT[, scientific_name := sapply(scientific_name, capatilize_first)]
DT[, species := sapply(species, capatilize_first)]
DT[, genus := sapply(genus, capatilize_first)]
DT[, status := sapply(status, capatilize_first)]

# reassign plant_name (can be other than genus in the future)
DT[, plant_name := genus]

# add time
time_stamp <- now()
trail <- 1e6*round(second(time_stamp) - floor(second(time_stamp)), 6)
DT[, created_at := sprintf('%s.%d+00', time_stamp, trail)]
DT[, updated_at := sprintf('%s.%d+00', time_stamp, trail)]

# reorder columns
setcolorder(DT, c(
  'id', 'plant_name', 'status', 'hawaiian_name', 'common_name', 'scientific_name',
  'genus', 'species', 'description', 'story', 'uses', 'created_at', 'updated_at'
))

fwrite(DT, 'data/plant_meta_v5.csv')
