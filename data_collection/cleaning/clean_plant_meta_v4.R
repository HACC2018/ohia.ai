# load data
local_meta <- rbind(
  fread('data/canoe_meta.csv'),
  fread('data/local_meta_v3.csv') 
)

# add counts to meta data
DT <- data.table(fid = dir('data/images/', recursive=T))
DT[, genus := sapply(fid, function(f) strsplit(f, '/')[[1]][1])]
DT[, id    := sapply(fid, function(f) strsplit(f, '/')[[1]][2])]

counts <- DT[, .(image_count=.N), keyby=genus]
local_meta[counts, image_count:=image_count, on='genus']
local_meta[is.na(image_count), image_count := 0]

setorder(local_meta, -image_count)
fwrite(local_meta, 'data/plant_meta_v4.csv')

local_meta[, .(genus, hawaiian_name, common_name, status, image_count)]
