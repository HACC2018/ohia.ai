library(data.table)
library(stringr)

data_path <- '../data'
DT <- data.table(species = dir('../data/thumbnails'))

# get genus
words <- DT[, unlist(lapply(species, strsplit, ' '))]

word_counts <- table(words)
top_genera <- names(word_counts[word_counts>10])
top_genera <- setdiff(top_genera, 'Unknown')
top_genera <- top_genera[substr(top_genera, 1, 1) == toupper(substr(top_genera, 1, 1))]
top_genera

DT[, genus := str_extract(species, paste(top_genera, collapse='|'))]
DT <- DT[!is.na(genus)]

# get species count
DT[, `:=`(
  species_count = sapply(species, function(s) length(dir(sprintf('../data/thumbnails/%s', s))))
)] 

DT[, genus_count := sum(species_count), by=genus]
DT[ is.na(genus), genus_count := 0]

setorder(DT, -genus_count)
DT[!is.na(genus)]

DT[, .(
  image_count = genus_count[1],
  species_count = .N),
  by=genus][1:10]

top10_genera <- DT[, .(count = genus_count[1]), by=genus][1:10, genus]
out_files <- top10_genera[, file.path()]
in_files <- top10_genera[, file.path()]

for (g in top10_genera) {
  dir.create(sprintf('../data./top10_genera/%s', g), F)
  species_list <- DT[genus == g, species]
  for (s in species_list) {
    for (f in dir(sprintf('thumbnail_images/%s', s))) {
      print(f)
      file.copy(
        sprintf('thumbnail_images/%s/%s', s, f),
        sprintf('genus_images/%s/%s', g, f)
      )
    }
  }
}


