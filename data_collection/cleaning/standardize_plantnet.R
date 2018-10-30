library(data.table)
library(parallel)
library(xml2)

# # move all images into a single folder (do once)
# file_list <- c(
#   dir('data/external/plantnet/train_data', recursive=T, full.names=T),
#   dir('data/external/plantnet/test_data', recursive=T, full.names=T))
# for (f in file_list) {
#   fid <- strsplit(f, '/')[[1]][6]  
#   if (grepl('jpg', fid)) {
#     file.rename(f, sprintf('data/external/plantnet/tmp/%s', fid))
#   } else {
#     file.rename(f, sprintf('data/external/plantnet/xml/%s', fid))
#   }
# }

# load meta data
LOOKUP_FIELDS <- c('FileName', 'Species', 'Genus', 'Family', 'ObservationId', 'MediaId', 'ClassId')
LOOKUP_FIELDS <- setNames(sprintf('//%s', LOOKUP_FIELDS), LOOKUP_FIELDS)
lookup <- function(fid) {
  x <- tryCatch(read_xml(fid, options='HUGE'), error=function(cond) NULL)
  if (is.null(x)) return(NULL)
  data.table(t(sapply(LOOKUP_FIELDS, function(f) xml_text(xml_find_all(x, f)))))
}

# setup cluster
cl <- makeCluster(7)
clusterEvalQ(cl, {library(data.table); library(xml2)})
clusterExport(cl, 'LOOKUP_FIELDS')

# lookup
file_list <- dir('data/external/plantnet/xml', full.names=T)
plantnet_meta <- rbindlist(parLapply(cl, file_list, lookup))
stopCluster(cl)

# save 
fwrite(plantnet_meta,  'data/external/plantnet/plantnet_meta.csv')
plantnet_meta <- fread('data/external/plantnet/plantnet_meta.csv')

# copy images into folders
for (g in unique(plantnet_meta$Genus)) {
  dir.create(sprintf('data/external/plantnet/images/%s', g), F)
  for (f in plantnet_meta[Genus==g, FileName]) {
    file.copy(
      sprintf('data/external/plantnet/tmp/%s', f),
      sprintf('data/external/plantnet/images/%s/%s', g, f)
    )
  }
}

# load local meta
local_meta <- fread('data/plant_meta_v3.csv')
local_meta[, .(species, genus, common_name, status)]

# find intersection between local and plantnet
meta <- plantnet_meta[Genus %in% local_meta$genus]
DT[, .N, keyby=genus]for (g in unique(meta$Genus)) {
  dir.create(sprintf('data/plantnet/%s', g), F)
  for (f in meta[Genus==g, FileName]) {
    file.copy(
      sprintf('data/external/plantnet/tmp/%s', f),
      sprintf('data/plantnet/%s/%s', g, f)
    )
  }
}

# copy images in intersection
for (g in meta[, unique(Genus)]) {
  dir.create(sprintf('data/images/%s', g), showWarnings=F)
  for (id in meta[Genus == g, ObservationId]) {
    file.copy(
      sprintf('data/external/clef/images/%s.jpg', id),
      sprintf('data/images/%s/%s.jpg', g, id)
    )
  }
}
