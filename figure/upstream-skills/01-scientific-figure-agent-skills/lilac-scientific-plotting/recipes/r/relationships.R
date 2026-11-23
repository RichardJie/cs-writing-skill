# Source: PDF pp.26-43,58-60,117-123. All functions are parameterized Codex adaptations.
scatter_fit <- function(data, x, y, group = NULL, fit_scope = c("group", "overall"), level = 0.95) {
  sp_require("ggplot2")
  sp_data(data, c(x, y, group), c(x, y))
  fit_scope <- match.arg(fit_scope)
  if (length(level) != 1L || !is.finite(level) || level <= 0 || level >= 1) stop("level must be between 0 and 1.")
  groups <- if (is.null(group)) "All" else sp_levels(data[[group]])
  d <- data.frame(.x = data[[x]], .y = data[[y]],
                   .group = factor(if (is.null(group)) rep("All", nrow(data)) else data[[group]], levels = groups))
  subsets <- if (fit_scope == "overall") list(Overall = d) else split(d, d$.group)
  models <- list(); predictions <- list(); statistics <- list()
  for (nm in names(subsets)) {
    z <- subsets[[nm]]
    if (nrow(z) < 3 || length(unique(z$.x)) < 2) stop("OLS requires at least 3 rows and varying x in each fitted subset.")
    model <- stats::lm(.y ~ .x, data = z)
    grid <- data.frame(.x = seq(min(z$.x), max(z$.x), length.out = 100))
    bounds <- stats::predict(model, newdata = grid, interval = "confidence", level = level)
    models[[nm]] <- model
    predictions[[nm]] <- data.frame(grid, bounds, .fit = nm)
    statistics[[nm]] <- data.frame(group = nm, n = nrow(z), r_squared = summary(model)$r.squared)
  }
  pred <- do.call(rbind, predictions)
  palette <- scientific_palette(groups)
  p <- ggplot2::ggplot(d, ggplot2::aes(.x, .y))
  if (fit_scope == "overall") {
    p <- p + ggplot2::geom_ribbon(data = pred, ggplot2::aes(x = .x, ymin = lwr, ymax = upr),
                                  inherit.aes = FALSE, fill = "#666666", alpha = 0.16) +
      ggplot2::geom_line(data = pred, ggplot2::aes(.x, fit), inherit.aes = FALSE, colour = "#333333", linewidth = 0.6)
  } else {
    p <- p + ggplot2::geom_ribbon(data = pred, ggplot2::aes(x = .x, ymin = lwr, ymax = upr, fill = .fit),
                                  inherit.aes = FALSE, alpha = 0.15, colour = NA, show.legend = FALSE) +
      ggplot2::geom_line(data = pred, ggplot2::aes(.x, fit, colour = .fit), inherit.aes = FALSE, linewidth = 0.6) +
      ggplot2::scale_fill_manual(values = palette)
  }
  p <- p + ggplot2::geom_point(ggplot2::aes(colour = .group), size = 1.6, alpha = 0.65) +
    ggplot2::scale_colour_manual(values = palette, name = group) + theme_scientific() +
    ggplot2::labs(x = x, y = y, caption = paste0(round(100 * level, 2), "% pointwise mean CI; OLS y ~ x"))
  if (is.null(group)) p <- p + ggplot2::guides(colour = "none")
  list(plot = p, models = models, statistics = do.call(rbind, statistics), predictions = pred)
}

bubble_plot <- function(data, x, y, magnitude, group = NULL, max_size = 9) {
  sp_require("ggplot2")
  sp_data(data, c(x, y, magnitude, group), c(x, y, magnitude))
  if (any(data[[magnitude]] < 0)) stop("Bubble area requires nonnegative magnitudes.")
  d <- data.frame(.x = data[[x]], .y = data[[y]], .magnitude = data[[magnitude]])
  if (!is.null(group)) d$.group <- factor(data[[group]], levels = sp_levels(data[[group]]))
  p <- ggplot2::ggplot(d, ggplot2::aes(.x, .y, size = .magnitude))
  if (is.null(group)) p <- p + ggplot2::geom_point(shape = 21, fill = "#0072B2", alpha = 0.65, stroke = 0.3)
  else p <- p + ggplot2::geom_point(ggplot2::aes(fill = .group), shape = 21, alpha = 0.65, stroke = 0.3) +
    ggplot2::scale_fill_manual(values = scientific_palette(sp_levels(data[[group]])), name = group)
  p + ggplot2::scale_size_area(max_size = max_size, name = magnitude) + theme_scientific() +
    ggplot2::labs(x = x, y = y)
}

density2d_plot <- function(data, x, y, bins = 8L) {
  sp_require("ggplot2")
  sp_data(data, c(x, y), c(x, y))
  if (nrow(data) < 10 || any(vapply(data[c(x, y)], function(z) length(unique(z)) < 3, logical(1))))
    stop("2D density requires enough varying observations.")
  ggplot2::ggplot(data, ggplot2::aes(.data[[x]], .data[[y]])) +
    ggplot2::geom_point(size = 0.7, alpha = 0.2, colour = "#555555") +
    ggplot2::stat_density_2d(ggplot2::aes(colour = ggplot2::after_stat(level)), bins = bins, linewidth = 0.6) +
    ggplot2::scale_colour_viridis_c(name = "Density") + theme_scientific()
}

highlight_scatter <- function(data, x, y, label, selected, seed = 1L) {
  sp_require(c("ggplot2", "ggrepel"))
  sp_data(data, c(x, y, label), c(x, y))
  if (!is.logical(selected) || length(selected) != nrow(data) || anyNA(selected)) stop("selected must be one logical per row.")
  focus <- data[selected, , drop = FALSE]
  ggplot2::ggplot(data, ggplot2::aes(.data[[x]], .data[[y]])) +
    ggplot2::geom_point(colour = "#AAAAAA", alpha = 0.55, size = 1.2) +
    ggplot2::geom_point(data = focus, colour = "#0072B2", size = 2) +
    ggrepel::geom_text_repel(data = focus, ggplot2::aes(label = .data[[label]]),
                              seed = seed, size = 2.8, max.overlaps = Inf, min.segment.length = 0,
                              colour = "#005681", segment.colour = "#777777") + theme_scientific()
}
