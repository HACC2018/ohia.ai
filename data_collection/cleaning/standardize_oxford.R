
library(data.table)
library(stringdist)
library(xml2)

plant_meta <- fread('data/plant_categories_v3.csv')
plant_meta[, .(plant_name, common_name)]

dir_name <- 'data/external/oxford/oxford-102-flowers'
labels <- fread(sprintf('%s/labels.csv', dir_name))

f <- 'home/marifel/repos/ohia.ai/data/tmp'
read_xml('')


most_similar <- function(n) {
  
}
unique(labels$class)

plant_meta[, sim := mapply(function(a, b) {
  a <- strsplit(' ', a)[[1]]
  b <- strsplit(' ', b)[[1]]
  max(stringsim(a, b, method='osa'))
}, genus, species)]


plant_meta[, .(genus, species, sim)]


file_list <- labels[grepl('frangipani', plant_name), file_name]
for (f in file_list) {
  # file.copy(
  #   sprintf('%s/%s', dir_name, f),
  #   sprintf('%s/frangipani/%s', dir_name, strsplit(f,'/')[[1]][2])
  # )
}



# # instagram
# for (p in dir('data/external/google/common genus', full.names=T, recursive=T)) {
#   file.rename(p, gsub('genus|\\s+', '', p))
#   
# }
