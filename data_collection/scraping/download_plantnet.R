library(data.table)
library(parallel)

# load meta data
load_meta <- function(dataset) {
  select_cols <- c(
    "Species", "Origin", "OriginalUrl", "Genus", "Family", "ObservationId",
    "MediaId", "YearInCLEF", "LearnTag", "ClassId", "BackUpLink")    
  file_name <- ifelse(
    dataset == 'train',
    'data/external/plantnet/PlantCLEF2017TrainWeb.csv',
    'data/external/plantnet/PlantCLEF2017OnlyTest.csv'  )
  fread(file_name, select=select_cols)
}
plantnet_meta <- rbind(load_meta('train'), load_meta('test'))
fwrite(plantnet_meta, 'data/external/plantnet/plantnet_meta.csv')


# download all images
try_download <- function(f, url1, url2) {
  tryCatch({
    download.file(url1, f, mode='wb') 
  }, 
  error = function(cond) {
    tryCatch({
      if (!is.na(url2)) {
        download.file(url2, f, mode='wb')   
      }
    })
  })
}

cl <- makeCluster(7)
x <- clusterMap(
  cl, try_download,
  plantnet_meta[, sprintf('data/external/plantnet/downloads/%s.jpg', ObservationId)],
  plantnet_meta[, OriginalUrl],
  plantnet_meta[, BackUpLink]
)
stopCluster(cl)
