# Source: PDF pp.106-109 (codes 56-57). Codex adaptation renders supplied intervals, never infers them.
estimate_plot <- function(data, category, estimate, lower, upper, interval_label,
                           group = NULL, connect = FALSE, reference = NULL) {
  sp_require("ggplot2")
  sp_data(data, c(category, estimate, lower, upper, group), c(estimate, lower, upper))
  sp_unique(data, c(category, group))
  if (length(interval_label) != 1L || is.na(interval_label) || !nzchar(interval_label)) stop("Define interval type/method in interval_label.")
  if (any(data[[lower]] > data[[estimate]] | data[[upper]] < data[[estimate]])) stop("Bounds must contain each estimate.")
  groups <- if (is.null(group)) "All" else sp_levels(data[[group]])
  d <- data.frame(.category = data[[category]], .estimate = data[[estimate]], .lower = data[[lower]], .upper = data[[upper]],
                   .group = factor(if (is.null(group)) rep("All", nrow(data)) else data[[group]], levels = groups))
  dodge <- ggplot2::position_dodge(width = 0.55)
  p <- ggplot2::ggplot(d, ggplot2::aes(.category, .estimate, colour = .group, group = .group))
  if (!is.null(reference)) p <- p + ggplot2::geom_hline(yintercept = reference, colour = "#999999", linetype = 2, linewidth = 0.35)
  p <- p + ggplot2::geom_errorbar(ggplot2::aes(ymin = .lower, ymax = .upper), position = dodge, width = 0.12, linewidth = 0.45)
  if (connect) p <- p + ggplot2::geom_line(position = dodge, linewidth = 0.45)
  p <- p + ggplot2::geom_point(position = dodge, size = 2) +
    ggplot2::scale_colour_manual(values = scientific_palette(groups), name = group) +
    ggplot2::labs(x = category, y = estimate, caption = interval_label) + theme_scientific()
  if (is.null(group)) p <- p + ggplot2::guides(colour = "none")
  p
}
