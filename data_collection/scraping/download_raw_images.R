library(rvest)

download_html <- function(url, os='windows') {
  
  # create phantomjs script
  x <- readLines('js/thumbnail_template.js')
  x <- sub('REPLACEMENT_URL', sprintf("'%s'", url), x)
  fc <- file('js/download.js')
  writeLines(x, fc)
  close(fc)
  
  # run phantomjs
  if (os == 'windows') {
    system('phantomjs.exe js/download.js')
  } else {
    system('phantomjs js/download.js')
  }
}
 
# get list of species
base_url <- "http://www.starrenvironmental.com/images"
species_list <- read_html(base_url) %>%
  html_nodes("i") %>% 
  html_text()
head(species_list)


# download all images
for (species in species_list) {
  
  # download html
  species_url <- gsub(' ', '+', species)
  species_url <- sprintf('%s/search/?q=%s', base_url, species_url)
  download_html(species_url, os='ubuntu')
  
  # parse html
  image_url_list <- read_html('species.html') %>%
    html_nodes("#flickr_images .image_inserted") %>%
    html_attr('src')
  
  # download all images
  dir.create(file.path('images', species), showWarnings=F)
  for (image_url in image_url_list) {
    file_name <- tail(strsplit(image_url, '/')[[1]], 1)
    file_name <- file.path('images', species, file_name)
    download.file(image_url, destfile=file_name, mode='wb')
  }
}
