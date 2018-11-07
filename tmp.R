

plant_list <- dir('data/preprocessed_images/scraped_filtered')
for (p in plant_list) {
  dir.create(sprintf('machine_learning/results/%s', p))
}
