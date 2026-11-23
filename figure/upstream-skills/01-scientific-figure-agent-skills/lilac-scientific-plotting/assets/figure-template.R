# Project template. Set SCIENTIFIC_PLOTTING_SKILL to the installed skill folder.
# Adapt this standalone plotting template to a real dataset and project.
skill <- Sys.getenv("SCIENTIFIC_PLOTTING_SKILL")
if (!nzchar(skill)) stop("Set SCIENTIFIC_PLOTTING_SKILL to the skill directory before running.")
source(file.path(skill, "scripts", "figure-tools.R"))
source(file.path(skill, "recipes", "r", "estimates.R"))

# estimates.csv must contain one estimate and already-computed bounds per outcome/group.
data <- read.csv("estimates.csv", check.names = FALSE)
p <- estimate_plot(data, "outcome", "estimate", "lower", "upper",
                   interval_label = "95% CI; specify the actual analysis method", group = "group")
export_figure(p, file.path("figures", "estimates"), width_mm = 170, height_mm = 100)
# Reopen exported files and complete references/figure-qc.md before delivery.
