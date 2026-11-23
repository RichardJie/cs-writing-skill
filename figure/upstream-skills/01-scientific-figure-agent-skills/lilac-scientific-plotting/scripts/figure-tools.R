# Codex implementation helpers; visual rationale: PDF pp.170-184,201-205.
sp_require <- function(packages) {
  missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly = TRUE)]
  if (length(missing)) stop("Install required package(s) in your project environment: ",
                            paste(missing, collapse = ", "), call. = FALSE)
}

sp_data <- function(data, columns, numeric = character(), allow_na = character()) {
  if (!is.data.frame(data) || !nrow(data)) stop("Expected a nonempty data frame.")
  if (anyDuplicated(names(data))) stop("Column names must be unique.")
  absent <- setdiff(columns, names(data))
  if (length(absent)) stop("Missing columns: ", paste(absent, collapse = ", "))
  for (nm in columns) {
    x <- data[[nm]]
    if (!(nm %in% allow_na) && anyNA(x)) stop("Handle missing values explicitly in: ", nm)
    if (nm %in% numeric && (!is.numeric(x) || any(!is.finite(x) & !is.na(x))))
      stop("Expected finite numeric values in: ", nm)
  }
  invisible(data)
}

sp_unique <- function(data, columns) {
  if (anyDuplicated(data[columns])) stop("Duplicate observational keys: ", paste(columns, collapse = ", "))
}

sp_levels <- function(x) {
  if (is.factor(x)) levels(droplevels(x)) else unique(as.character(x))
}

scientific_palette <- function(groups) {
  groups <- as.character(groups)
  colors <- c("#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#333333")
  if (!length(groups) || anyNA(groups) || anyDuplicated(groups) || length(groups) > length(colors))
    stop("Supply 1-7 unique nonmissing groups; for more groups choose an explicit design.")
  stats::setNames(colors[seq_along(groups)], groups)
}

theme_scientific <- function(base_size = 9, base_family = "sans") {
  sp_require("ggplot2")
  ggplot2::theme_minimal(base_size = base_size, base_family = base_family) +
    ggplot2::theme(panel.grid.minor = ggplot2::element_blank(),
                   panel.grid.major = ggplot2::element_line(colour = "#E3E3E3", linewidth = 0.25),
                   plot.title = ggplot2::element_text(face = "bold", size = base_size + 1),
                   axis.title = ggplot2::element_text(size = base_size),
                   legend.position = "bottom", legend.key.width = grid::unit(4, "mm"),
                   plot.margin = ggplot2::margin(6, 7, 6, 6))
}

export_figure <- function(plot, stem, width_mm, height_mm,
                          formats = c("png", "pdf"), dpi = 300, overwrite = FALSE) {
  sp_require("ggplot2")
  dims <- c(width_mm, height_mm, dpi)
  if (length(dims) != 3L || any(!is.finite(dims)) || any(dims <= 0)) stop("Positive dimensions and DPI required.")
  if (!length(formats) || any(!formats %in% c("png", "pdf", "svg")) || anyDuplicated(formats))
    stop("Formats must be a unique selection of png, pdf, svg.")
  if (length(stem) != 1L || !nzchar(stem)) stop("One output stem is required.")
  paths <- paste0(stem, ".", formats)
  metadata <- paste0(stem, ".metadata.txt")
  if (!overwrite && any(file.exists(c(paths, metadata)))) stop("Output exists; choose a new stem or overwrite=TRUE.")
  if ("png" %in% formats) sp_require("ragg")
  if ("svg" %in% formats) sp_require("svglite")
  if ("pdf" %in% formats && !capabilities("cairo")) stop("This R build has no Cairo PDF device.")
  dir.create(dirname(stem), recursive = TRUE, showWarnings = FALSE)
  for (i in seq_along(formats)) {
    device <- switch(formats[i], png = ragg::agg_png, pdf = grDevices::cairo_pdf, svg = svglite::svglite)
    ggplot2::ggsave(paths[i], plot = plot, device = device, width = width_mm,
                   height = height_mm, units = "mm", dpi = dpi, bg = "white")
  }
  writeLines(c(paste("width_mm:", width_mm), paste("height_mm:", height_mm),
               paste("raster_dpi:", dpi), paste("formats:", paste(formats, collapse = ", ")),
               capture.output(sessionInfo())), metadata)
  invisible(paths)
}
