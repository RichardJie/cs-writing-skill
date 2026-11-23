args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: Rscript smoke_test.R <R-library> <output-directory>")
}

library_path <- normalizePath(args[[1]], winslash = "/", mustWork = TRUE)
output_directory <- args[[2]]
.libPaths(c(library_path, .libPaths()))
dir.create(output_directory, recursive = TRUE, showWarnings = FALSE)

set.seed(20260801)
smoke_data <- data.frame(
  group = rep(c("Synthetic A", "Synthetic B"), each = 24),
  response = c(rnorm(24, 0, 1), rnorm(24, 0.75, 1))
)

plot_object <- ggplot2::ggplot(smoke_data, ggplot2::aes(group, response, colour = group)) +
  ggplot2::geom_boxplot(width = 0.5, outlier.shape = NA, colour = "#333333") +
  ggplot2::geom_jitter(width = 0.15, size = 1.4) +
  ggplot2::scale_colour_manual(values = c("#2878B5", "#D55E00"), guide = "none") +
  ggplot2::labs(
    title = "Environment smoke test\n(synthetic; not research data)",
    x = NULL,
    y = "Synthetic response (a.u.)"
  ) +
  ggplot2::theme_classic(base_size = 9) +
  ggplot2::theme(plot.title = ggplot2::element_text(size = 8.5, hjust = 0.5))

ggplot2::ggsave(file.path(output_directory, "r_smoke_test.png"), plot_object, width = 85, height = 68, units = "mm", dpi = 300)
ggplot2::ggsave(file.path(output_directory, "r_smoke_test.tiff"), plot_object, width = 85, height = 68, units = "mm", dpi = 600, compression = "lzw")
ggplot2::ggsave(file.path(output_directory, "r_smoke_test.svg"), plot_object, width = 85, height = 68, units = "mm", device = svglite::svglite)
