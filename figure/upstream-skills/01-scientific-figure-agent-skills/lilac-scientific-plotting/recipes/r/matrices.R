# Source: PDF pp.45-48,112-117. Codex adaptation: explicit finite matrix and missing-cell handling.
heatmap_plot <- function(data, row, column, value, midpoint = NULL, limits = NULL) {
  sp_require("ggplot2")
  sp_data(data, c(row, column, value), value, allow_na = value)
  sp_unique(data, c(row, column))
  if (all(is.na(data[[value]]))) stop("At least one observed cell is required.")
  d <- data.frame(.row = factor(data[[row]], levels = rev(sp_levels(data[[row]]))),
                   .column = factor(data[[column]], levels = sp_levels(data[[column]])), .value = data[[value]])
  if (nrow(d) != nlevels(d$.row) * nlevels(d$.column)) stop("Supply every matrix cell, with NA for missing measurements.")
  if (!is.null(limits) && (length(limits) != 2L || any(!is.finite(limits)) || limits[1] >= limits[2] ||
                           any(d$.value < limits[1] | d$.value > limits[2], na.rm = TRUE)))
    stop("Limits must include all observed values; do not silently censor cells.")
  p <- ggplot2::ggplot(d, ggplot2::aes(.column, .row, fill = .value)) +
    ggplot2::geom_tile(colour = "white", linewidth = 0.25) + ggplot2::coord_equal() +
    ggplot2::labs(x = column, y = row, fill = value) + theme_scientific() +
    ggplot2::theme(panel.grid.major = ggplot2::element_blank())
  if (is.null(midpoint)) p + ggplot2::scale_fill_viridis_c(limits = limits, na.value = "#BDBDBD")
  else p + ggplot2::scale_fill_gradient2(low = "#2166AC", mid = "#F7F7F7", high = "#B2182B",
                                         midpoint = midpoint, limits = limits, na.value = "#BDBDBD")
}

correlation_plot <- function(data, columns, method = c("pearson", "spearman")) {
  sp_require("ggplot2")
  method <- match.arg(method)
  sp_data(data, columns, columns)
  if (length(columns) < 2 || anyDuplicated(columns) || nrow(data) < 3 ||
      any(vapply(data[columns], function(x) stats::sd(x) == 0, logical(1)))) stop("Need >=2 varying columns and >=3 complete rows.")
  m <- stats::cor(data[columns], method = method, use = "everything")
  d <- expand.grid(.row = columns, .column = columns, stringsAsFactors = FALSE)
  d$.value <- as.vector(m)
  p <- heatmap_plot(d, ".row", ".column", ".value", midpoint = 0, limits = c(-1, 1)) +
    ggplot2::labs(x = NULL, y = NULL, fill = paste(method, "r"), caption = paste("Complete observations:", nrow(data)))
  list(plot = p, matrix = m, n = nrow(data), method = method)
}
