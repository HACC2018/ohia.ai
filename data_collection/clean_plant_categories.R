library(data.table)

clean_text <- function( x){
  x <- gsub('\n', ' ', x)         # replace new lines with space
  x <- gsub('\\[\\d+\\]', '', x)  # remove references [\\d+]
  x <- gsub('\\"+', '\\"', x)     # remove double quotes
  x <- gsub('\\s+', ' ', x)       # remove extra whitespace
  x <- trimws(x)                  # remove leading and trailing ws
  x
}

DT <- fread('../data/plant_categories_v2.csv')
DT[, description := clean_text(description)]
DT[, story := clean_text(story)]
DT[, uses := clean_text(uses)]

fwrite(DT, '../data/plant_categories_v3.csv')