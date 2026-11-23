# Source: PDF pp.196-201. Codex adaptation: collecting guides requires explicit shared semantics.
compose_panels <- function(plots, ncol = 2, widths = NULL, heights = NULL,
                            collect = FALSE, shared_encoding = FALSE, tags = TRUE) {
  sp_require("patchwork")
  if (!is.list(plots) || !length(plots)) stop("Provide a nonempty plot list.")
  if (collect && !isTRUE(shared_encoding)) stop("Confirm identical encodings before collecting legends.")
  p <- patchwork::wrap_plots(plots, ncol = ncol, widths = widths, heights = heights,
                             guides = if (collect) "collect" else "keep")
  if (tags) p <- p + patchwork::plot_annotation(tag_levels = "A")
  p
}
