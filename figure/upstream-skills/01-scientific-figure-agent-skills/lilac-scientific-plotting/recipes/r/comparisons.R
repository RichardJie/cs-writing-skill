# Source: PDF pp.48-56,84-106. Codex adaptation: explicit keys/order, no data-coordinate edits.
trend_plot <- function(data, x, y, group) {
  sp_require("ggplot2")
  sp_data(data, c(x, y, group), c(x, y))
  sp_unique(data, c(group, x))
  d <- data.frame(.x = data[[x]], .y = data[[y]], .group = factor(data[[group]], levels = sp_levels(data[[group]])))
  ggplot2::ggplot(d, ggplot2::aes(.x, .y, colour = .group, group = .group)) +
    ggplot2::geom_line(linewidth = 0.55) + ggplot2::geom_point(size = 1.8) +
    ggplot2::scale_colour_manual(values = scientific_palette(sp_levels(data[[group]])), name = group) +
    ggplot2::labs(x = x, y = y) + theme_scientific()
}

paired_slope <- function(data, id, occasion, value, occasions) {
  sp_require("ggplot2")
  sp_data(data, c(id, occasion, value), value)
  if (length(occasions) != 2L || anyNA(occasions) || anyDuplicated(occasions)) stop("Two ordered occasions required.")
  sp_unique(data, c(id, occasion))
  if (!all(as.character(data[[occasion]]) %in% occasions) || any(table(data[[id]]) != 2L))
    stop("Each ID must have exactly one observation at each specified occasion.")
  d <- data.frame(.id = data[[id]], .occasion = factor(data[[occasion]], levels = occasions), .value = data[[value]])
  ggplot2::ggplot(d, ggplot2::aes(.occasion, .value, group = .id)) +
    ggplot2::geom_line(colour = "#999999", alpha = 0.65, linewidth = 0.4) +
    ggplot2::geom_point(ggplot2::aes(colour = .occasion), size = 1.8) +
    ggplot2::scale_colour_manual(values = scientific_palette(occasions), guide = "none") +
    ggplot2::labs(x = occasion, y = value) + theme_scientific()
}

ordered_values <- function(data, category, value, kind = c("lollipop", "bar"), order = NULL) {
  sp_require("ggplot2")
  sp_data(data, c(category, value), value)
  sp_unique(data, category)
  kind <- match.arg(kind)
  if (is.null(order)) order <- as.character(data[[category]][order(data[[value]])])
  if (anyDuplicated(order) || !setequal(order, as.character(data[[category]]))) stop("Order must include each category once.")
  d <- data.frame(.category = factor(data[[category]], levels = order), .value = data[[value]])
  p <- ggplot2::ggplot(d, ggplot2::aes(.value, .category))
  if (kind == "lollipop") p <- p +
    ggplot2::geom_segment(ggplot2::aes(x = 0, xend = .value, yend = .category), colour = "#A0A0A0", linewidth = 0.5) +
    ggplot2::geom_point(colour = "#0072B2", size = 2)
  else p <- p + ggplot2::geom_col(fill = "#0072B2", width = 0.65)
  p + ggplot2::expand_limits(x = 0) + ggplot2::labs(x = value, y = NULL) + theme_scientific() +
    ggplot2::theme(panel.grid.major.y = ggplot2::element_blank())
}

grouped_bars <- function(data, category, group, value, position = c("dodge", "stack", "fill")) {
  sp_require("ggplot2")
  sp_data(data, c(category, group, value), value)
  sp_unique(data, c(category, group))
  position <- match.arg(position)
  if (any(data[[value]] < 0)) stop("This grouped/part-to-whole recipe requires nonnegative values.")
  if (position == "fill" && any(tapply(data[[value]], data[[category]], sum) == 0)) stop("Zero-total groups cannot be proportions.")
  d <- data.frame(.category = factor(data[[category]], levels = sp_levels(data[[category]])),
                   .group = factor(data[[group]], levels = sp_levels(data[[group]])), .value = data[[value]])
  p <- ggplot2::ggplot(d, ggplot2::aes(.category, .value, fill = .group)) +
    ggplot2::geom_col(position = position, width = 0.7) +
    ggplot2::scale_fill_manual(values = scientific_palette(sp_levels(data[[group]])), name = group) +
    ggplot2::labs(x = category, y = value) + theme_scientific()
  if (position == "fill") p <- p + ggplot2::labs(y = "Proportion")
  p
}
