#===============================================================================
# epiaim.R
#===============================================================================

# Imports ======================================================================

#' @import gaston

#' @title compute ld matrix
#'
#' @description compute ld matrix
#'
#' @param snps path to vcf file
#' @return ld matrix
#' @export
compute_ld_matrix <- function(vcf) {
  bm <- read.vcf(vcf)
  lim <- c(1, nrow(bm@snps))
  LD(bm, lim)
}