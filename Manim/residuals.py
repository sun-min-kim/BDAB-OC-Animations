from manim import *

class LinearRegressionWithLabels(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": WHITE},
        ).add_coordinates()

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Scatter plot points
        points = [(1, 1.5), (2, 3), (3, 2.5), (4, 4), (5, 5.5), (6, 5), (7, 6.5)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in points])

        # Initial line (bad guess)
        initial_line = axes.plot(lambda x: 2 * x - 2, x_range=[0, 8], color=RED)
        initial_line_label = Text("y = 2x - 2", color=RED).next_to(initial_line, UP)

        # Target regression line
        regression_line = axes.plot(lambda x: 0.8 * x + 1, x_range=[0, 8], color=GREEN)
        regression_line_label = Text("y = 0.8x + 1", color=GREEN).next_to(regression_line, UP)

        # Residual lines for the initial line
        initial_residuals = VGroup(
            *[
                Line(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x, 2 * x - 2),
                    color=RED,
                    stroke_width=2,
                )
                for x, y in points
            ]
        )

        # Residual lines for the regression line
        final_residuals = VGroup(
            *[
                Line(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x, 0.8 * x + 1),
                    color=GREEN,
                    stroke_width=2,
                )
                for x, y in points
            ]
        )

        # Title for the scene
        title = Text("Linear Regression Animation").to_edge(UP)

        # Labels for the residuals
        residual_label = Text("Residuals", color=RED).next_to(initial_residuals, RIGHT)

        # Animation sequence
        self.play(Write(title))
        self.play(Create(axes), Write(labels))
        self.play(FadeIn(dots))
        self.play(Create(initial_line))
        self.play(Write(initial_line_label))
        self.play(Create(initial_residuals))
        self.play(Write(residual_label))

        # Transition to regression line
        self.play(
            Transform(initial_line, regression_line),
            Transform(initial_line_label, regression_line_label),
            Transform(initial_residuals, final_residuals),
            run_time=3,
        )

        # Fade out the initial residuals
        self.play(FadeOut(initial_residuals), FadeOut(residual_label))

        # Write the regression line label
        self.play(Write(regression_line_label))

        # Highlight the regression line
        self.play(Indicate(regression_line, color=GREEN))

        # Hold the final view
        self.wait(2)


if __name__ == "__main__":
    scene = LinearRegressionWithLabels()
    scene.render()
