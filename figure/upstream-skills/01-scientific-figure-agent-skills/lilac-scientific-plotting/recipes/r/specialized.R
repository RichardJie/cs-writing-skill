# Source: PDF pp.130-134,143-149,149-161. Codex adaptations, see specialized-graphics.md.
sequence_logo <- function(sequences, method = c("bits", "prob")) {
  sp_require(c("ggseqlogo", "ggplot2"))
  method <- match.arg(method)
  if (!is.character(sequences) || length(sequences) < 2L || anyNA(sequences) ||
      any(nchar(sequences) == 0) || length(unique(nchar(sequences))) != 1L ||
      any(!grepl("^[ACGT]+$", sequences))) stop("Supply >=2 equal-length, aligned uppercase ACGT sequences without gaps.")
  ggseqlogo::ggseqlogo(sequences, method = method, seq_type = "dna") +
    ggplot2::labs(x = "Aligned position", y = if (method == "bits") "Information (bits)" else "Probability") +
    theme_scientific() + ggplot2::theme(panel.grid.major = ggplot2::element_blank())
}

draw_chord <- function(matrix, directional = FALSE, colors = NULL, transparency = 0.35) {
  sp_require("circlize")
  if (!is.matrix(matrix) || !is.numeric(matrix) || !length(matrix) || any(!is.finite(matrix)) ||
      any(matrix < 0) || sum(matrix) <= 0) stop("Need a finite nonnegative matrix with positive total.")
  if (is.null(rownames(matrix)) || is.null(colnames(matrix)) ||
      anyDuplicated(rownames(matrix)) || anyDuplicated(colnames(matrix)) ||
      anyNA(rownames(matrix)) || anyNA(colnames(matrix)) ||
      any(!nzchar(c(rownames(matrix), colnames(matrix))))) stop("Unique nonempty row/column labels required.")
  sectors <- unique(c(rownames(matrix), colnames(matrix)))
  if (is.null(colors)) colors <- scientific_palette(sectors)
  if (is.null(names(colors)) || !all(sectors %in% names(colors))) stop("Named colors must cover every sector.")
  circlize::circos.clear()
  on.exit(circlize::circos.clear(), add = TRUE)
  circlize::circos.par(start.degree = 90, gap.degree = 5)
  result <- circlize::chordDiagram(matrix, grid.col = colors, transparency = transparency,
                                    directional = if (directional) 1 else 0,
                                    annotationTrack = c("name", "grid"))
  invisible(result)
}

choropleth_plot <- function(geometry, data, geo_key, data_key, value, value_label,
                             midpoint = NULL, allow_unmatched = FALSE) {
  sp_require(c("sf", "ggplot2"))
  if (!inherits(geometry, "sf") || is.na(sf::st_crs(geometry))) stop("An sf object with a documented CRS is required.")
  sp_data(as.data.frame(sf::st_drop_geometry(geometry)), geo_key)
  sp_data(data, c(data_key, value), value, allow_na = value)
  sp_unique(sf::st_drop_geometry(geometry), geo_key)
  sp_unique(data, data_key)
  extra <- setdiff(as.character(data[[data_key]]), as.character(geometry[[geo_key]]))
  missing <- setdiff(as.character(geometry[[geo_key]]), as.character(data[[data_key]]))
  if (length(extra)) stop("Data keys have no geometry: ", paste(extra, collapse = ", "))
  if (length(missing) && !allow_unmatched) stop("Geometry keys have no data; review then opt in with allow_unmatched=TRUE.")
  idx <- match(as.character(geometry[[geo_key]]), as.character(data[[data_key]]))
  z <- geometry
  z$.sp_value <- data[[value]][idx]
  p <- ggplot2::ggplot(z) + ggplot2::geom_sf(ggplot2::aes(fill = .sp_value), colour = "white", linewidth = 0.3) +
    ggplot2::coord_sf() + ggplot2::labs(fill = value_label,
      caption = paste("Gray: missing value; regions:", nrow(z), "; missing:", sum(is.na(z$.sp_value)))) +
    theme_scientific() + ggplot2::theme(panel.grid.major = ggplot2::element_blank())
  if (is.null(midpoint)) p <- p + ggplot2::scale_fill_viridis_c(na.value = "#BDBDBD")
  else p <- p + ggplot2::scale_fill_gradient2(low = "#2166AC", mid = "#F7F7F7", high = "#B2182B", midpoint = midpoint, na.value = "#BDBDBD")
  list(plot = p, data = z, unmatched_geometry = missing, missing_values = sum(is.na(z$.sp_value)))
}
