args <- commandArgs(trailingOnly = TRUE)

default_library <- file.path(
  Sys.getenv("USERPROFILE"),
  "Documents", "Codex", "environments", "biomedical-figure-production", "R-library"
)
library_path <- if (length(args) >= 1 && nzchar(args[[1]])) args[[1]] else default_library

dir.create(library_path, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(normalizePath(library_path, winslash = "/", mustWork = TRUE), .libPaths()))
options(repos = c(CRAN = "https://cloud.r-project.org"), timeout = 600)

bootstrap_packages <- c(
  "cli", "glue", "gtable", "isoband", "lifecycle", "rlang", "S7", "vctrs", "withr",
  "farver", "labeling", "R6", "RColorBrewer", "viridisLite", "cpp11", "systemfonts",
  "textshaping", "Rcpp", "generics", "magrittr", "pkgconfig", "pillar", "tibble",
  "tidyselect", "dplyr", "purrr", "stringi", "stringr", "tidyr"
)
core_packages <- c("ggplot2", "patchwork", "ggrepel", "scales", "svglite", "tiff")
optional_packages <- c("cowplot", "forestplot", "pROC", "ragg", "survminer")
survival_support_packages <- c("doBy", "lme4", "pbkrtest", "car")
cran_packages <- c(
  bootstrap_packages,
  core_packages,
  optional_packages,
  survival_support_packages,
  "BiocManager"
)

install_cran_package <- function(package_name) {
  if (requireNamespace(package_name, quietly = TRUE)) return(TRUE)
  message("Installing CRAN package: ", package_name)
  tryCatch(
    {
      install.packages(
        package_name,
        lib = library_path,
        dependencies = c("Depends", "Imports", "LinkingTo"),
        type = "binary"
      )
      requireNamespace(package_name, quietly = TRUE)
    },
    error = function(error_condition) {
      message("Installation failed for ", package_name, ": ", conditionMessage(error_condition))
      FALSE
    }
  )
}

installation_status <- setNames(
  vapply(cran_packages, install_cran_package, logical(1)),
  cran_packages
)

if (isTRUE(installation_status[["BiocManager"]]) && !requireNamespace("ComplexHeatmap", quietly = TRUE)) {
  tryCatch(
    BiocManager::install("ComplexHeatmap", lib = library_path, ask = FALSE, update = FALSE),
    error = function(error_condition) {
      message("Installation failed for ComplexHeatmap: ", conditionMessage(error_condition))
    }
  )
}

cat("Biomedical figure R library:", normalizePath(library_path, winslash = "/"), "\n")
packages_to_report <- c(cran_packages, "ComplexHeatmap", "survival")
for (package_name in packages_to_report) {
  version <- if (requireNamespace(package_name, quietly = TRUE)) {
    as.character(utils::packageVersion(package_name))
  } else {
    "NOT INSTALLED"
  }
  cat(sprintf("%s=%s\n", package_name, version))
}

missing_core <- core_packages[!vapply(core_packages, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing_core) > 0) {
  stop("Required R packages remain unavailable: ", paste(missing_core, collapse = ", "))
}
