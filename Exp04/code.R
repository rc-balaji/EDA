
library(ggplot2)

# Sample data for plotting
set.seed(42)  # For reproducibility
data <- data.frame(
  Category = factor(rep(c("A", "B", "C"), each = 20)),
  Value = c(rnorm(20, mean = 50, sd = 10), rnorm(20, mean = 60, sd = 15), rnorm(20, mean = 55, sd = 5)),
  X = rnorm(60),
  Y = rnorm(60)
)

# Scatter Plot
ggplot(data, aes(x = X, y = Y, color = Category)) +
  geom_point() +
  ggtitle("Scatter Plot")

# Bar Plot
ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  ggtitle("Bar Plot")

# Box Plot
ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_boxplot() +
  ggtitle("Box Plot")

# Line Plot
ggplot(data, aes(x = X, y = Value, group = Category, color = Category)) +
  geom_line() +
  ggtitle("Line Plot")

# Contour Plot
# First we need to create some density data
dens <- MASS::kde2d(data$X, data$Y, n = 50)  # Using MASS package for 2D density
contour_data <- data.frame(expand.grid(X = dens$x, Y = dens$y), Z = as.vector(dens$z))

ggplot(contour_data, aes(x = X, y = Y, z = Z)) +
  geom_contour(aes(color = ..level..)) +
  ggtitle("Contour Plot")

# You can also save each plot to a file if desired
ggsave("scatter_plot.png")
ggsave("bar_plot.png")
ggsave("box_plot.png")
ggsave("line_plot.png")
ggsave("contour_plot.png")
