from manim import *
import numpy as np


class LinearRegression(Scene):
    # Run "manim -pql linear_regression.py LinearRegression" in terminal to render

    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[0, 10, 1],  # X axis range
            y_range=[-2, 8, 1],  # Y axis range
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Example data points (x, y)
        x = [1, 2, 3, 4, 5, 6, 7, 8]
        y = [2, 3, 2, 4, 5, 4, 6, 7]
        data_points = [(x[i], y[i]) for i in range(len(x))]

        # Linear Regression Line's
        xMean = np.mean(x)
        yMean = np.mean(y)
        regSlope = np.mean([(x[i] - xMean) * (y[i] - yMean) for i in range(len(data_points))]) / np.mean([(x[i] - xMean) ** 2 for i in range(len(data_points))])
        regIntercept = yMean - regSlope * xMean
        regLine = axes.plot(lambda x: regSlope * x + regIntercept, color=BLUE)
        regLine_label = Text(f"y = {round(regSlope, 3)}x + {round(regIntercept, 3)}").to_edge(RIGHT)

        # Scatter plot of points
        scatter_points = [Dot(axes.coords_to_point(x, y), color=BLUE) for x, y in data_points]

        # Incorrect linear regression line's
        slopes = [0.5, 0.9, 0.3]
        intercepts = [1.0, 1.7, -0.5]
        size = len(slopes)

        lines = [axes.plot(lambda x: slopes[i] * x + intercepts[i], color=RED) for i in range(size)]

        #regressionLine = axes.plot(lambda x: 0.7 * x + 1.0, color=BLUE)
        #lines.append(regressionLine)

        # Create linear regression line label's
        line_labels = [Text(f"y = {slopes[i]}x + {intercepts[i]}").to_edge(RIGHT) for i in range(size)]
        
        # Calculate Sum Squared Error values and create labels
        def SumSquaredErrors(slope, intercept):
            y_predicted = [slope * x[i] + intercept for i in range(len(x))]
            OLS = [(y[j] - y_predicted[j]) ** 2 for j in range(len(y))]
            ss_residual = round(np.sum(OLS), 3)
            return ss_residual

        sumSquaredError_values = []
        for i in range(size):
            sumSquaredError_values.append(round(SumSquaredErrors(slopes[i], intercepts[i]), 2))
        SSE_labels = [Text(f"Sum Squared Error: {sumSquaredError_values[i]}").to_corner(DOWN + RIGHT) for i, line_text in enumerate(line_labels)]
        regSSE_label = Text(f"Sum Squared Error: {SumSquaredErrors(regSlope, regIntercept)}").to_corner(DOWN + RIGHT)

        # Animation #
        # Add axes, labels, points and initial line
        self.play(Create(axes), Write(labels))
        self.play(*[FadeIn(point) for point in scatter_points])
        self.play(Create(lines[0]))
        
        # Animate the regression line changing between the regression lines
        for i in range(size - 1):
            self.play(Write(line_labels[i], font_size=15, run_time=0.3))
            self.play(Write(SSE_labels[i], font_size=7.5, run_time=0.3))
            self.wait(0.5)
            self.play(Unwrite(line_labels[i], run_time=0.3))
            self.play(Unwrite(SSE_labels[i], run_time=0.3))
            self.play(Transform(lines[0], lines[i + 1]))
        self.play(Write(line_labels[size - 1], font_size=15, run_time=0.3))
        self.play(Write(SSE_labels[size - 1], font_size=15, run_time=0.3))
        self.play(Unwrite(line_labels[size - 1], font_size=15, run_time=0.3))
        self.play(Unwrite(SSE_labels[size - 1], font_size=15, run_time=0.3)) 

        self.play(Transform(lines[0], regLine))
        self.play(Write(regLine_label, font_size=15, run_time=0.3))
        self.play(Write(regSSE_label, font_size=15, run_time=0.3))
        self.wait(1)