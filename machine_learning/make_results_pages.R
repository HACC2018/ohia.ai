library(data.table)

results <- fread('results/results.csv')
find_replace <- function(x, f, r) {
  lapply(x, function(xi) gsub(f, r, xi))
}

for (plant in results$labels) {
  
  DT <- results[labels==plant]
  template <- readLines('results/template.md')  
  
  template <- find_replace(template, 'PLANT_PLACEHOLDER', plant)
  template <- find_replace(template, 'TOP_1_PLACEHOLDER', sprintf('%0.2f%%', 100*DT$top_1))
  template <- find_replace(template, 'TOP_3_PLACEHOLDER', sprintf('%0.2f%%', 100*DT$top_3))
  template <- find_replace(template, 'TOP_5_PLACEHOLDER', sprintf('%0.2f%%', 100*DT$top_5))
  
  f <- file(sprintf('results/%s/README.md', plant))
  writeLines(as.character(template), f)
  close(f)
  
}
