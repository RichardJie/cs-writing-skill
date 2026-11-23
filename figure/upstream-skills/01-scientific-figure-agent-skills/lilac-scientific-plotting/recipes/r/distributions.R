# Source: PDF pp.21-25,44-45. Codex adaptation: explicit binwidth, no silent NA removal.
# Source scripts/figure-tools.R first. See references/recipe-catalog.md for contracts.
distribution_plot <- function(data, value, binwidth) {
  sp_require("ggplot2")
  sp_data(data, value, value)
  if (length(binwidth) != 1L || !is.finite(binwidth) || binwidth <= 0) stop("Positive binwidth required.")
  if (nrow(data) < 3 || length(unique(data[[value]])) < 2) stop("Density needs varying observations.")
  ggplot2::ggplot(data, ggplot2::aes(x = .data[[value]])) +
    ggplot2::geom_histogram(ggplot2::aes(y = ggplot2::after_stat(density)), binwidth = binwidth,
                            fill = "#B7D8E8", colour = "white", linewidth = 0.25) +
    ggplot2::geom_density(colour = "#0072B2", linewidth = 0.65) +
    ggplot2::labs(x = value, y = "Density") + theme_scientific()
}

group_distribution <- function(data, group, value, violin = TRUE, seed = 1L) {
  sp_require("ggplot2")
  sp_data(data, c(group, value), value)
  groups <- sp_levels(data[[group]])
  d <- data.frame(.group = factor(data[[group]], levels = groups), .value = data[[value]])
  if (violin && any(vapply(split(d$.value, d$.group), function(x) length(x) < 3 || length(unique(x)) < 2, logical(1))))
    stop("Violin density requires at least three varying observations per group; use violin=FALSE.")
  p <- ggplot2::ggplot(d, ggplot2::aes(.group, .value, fill = .group))
  if (violin) p <- p + ggplot2::geom_violin(alpha = 0.28, colour = NA, trim = TRUE)
  p + ggplot2::geom_boxplot(width = 0.20, outlier.shape = NA, alpha = 0.55, linewidth = 0.4) +
    ggplot2::geom_point(position = ggplot2::position_jitter(width = 0.08, height = 0, seed = seed),
                        shape = 21, size = 1.4, stroke = 0.25, alpha = 0.65) +
    ggplot2::scale_fill_manual(values = scientific_palette(groups), guide = "none") +
    ggplot2::labs(x = group, y = value) + theme_scientific()
}

ridge_plot <- function(data, group, value, bandwidth) {
  sp_require(c("ggplot2", "ggridges"))
  sp_data(data, c(group, value), value)
  if (length(bandwidth) != 1L || !is.finite(bandwidth) || bandwidth <= 0) stop("Positive bandwidth required.")
  groups <- sp_levels(data[[group]])
  d <- data.frame(.group = factor(data[[group]], levels = groups), .value = data[[value]])
  if (any(table(d$.group) < 3)) stop("At least three observations per ridge required.")
  ggplot2::ggplot(d, ggplot2::aes(.value, .group, fill = .group)) +
    ggridges::geom_density_ridges(bandwidth = bandwidth, scale = 0.9, alpha = 0.65,
                                  rel_min_height = 0.01, linewidth = 0.3) +
    ggplot2::scale_fill_manual(values = scientific_palette(groups), guide = "none") +
    ggplot2::labs(x = value, y = group) + theme_scientific()
}
