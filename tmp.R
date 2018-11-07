library(parallel)

dir_list <- dir('data/plantnet', full.names=T)
plant_count <- sapply(dir_list, function(d) length(dir(d)))

keep_plants <- names(plant_count[plant_count>=100])
file_list <- as.character(unlist(sapply(keep_plants, dir, full.names=T)))

