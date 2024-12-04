from manim import *

class LinearRegressionAnimation(Scene):
    # Run "manim -pql linear_regression_animation.py LinearRegressionAnimation" in terminal to run

    def construct(self):
        # Create sample data points
        data_points = [
            [1, 2], [2, 3], [3, 5], [4, 7], [5, 7]
        ]
        numPoints = len(data_points)
        
        # Create the points
        points = [Dot(point=i, color=BLUE) for i in range(numPoints)]
        print(points)
        
        # Create and add axes and data points 
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 1], 
            axis_config={"include_numbers": True, "color": BLUE}
        )
        
        # Add axes and points to the scene
        # Scatter plot of points
        scatter_points = [Dot(axes.coords_to_point(x, y), color=BLUE) for x, y in data_points]
        self.play(Create(axes))
        self.play(*[Create(point) for point in scatter_points])
        

        # Initial line (guess m=1, b=0)
        line = axes.plot(lambda x: x, color=YELLOW)

        # Draw the line and the SSE squares
        self.play(Create(line))
        self.wait(1)
        
        # Create vertical lines representing errors
        errors = []
        for i, point in enumerate(data_points):
            predicted_y = point[0]  # line formula: y = x
            error_line = Line(
                start=point[0] * RIGHT + point[1] * UP,
                end=point[0] * RIGHT + predicted_y * UP,
                color=RED
            )
            errors.append(error_line)
        
        self.play(*[Create(error) for error in errors])
        self.wait(1)

        # Update the line to minimize SSE (example with slope 1.5, intercept 0)
        new_line = axes.plot(lambda x: 1.5 * x, color=YELLOW)
        self.play(Transform(line, new_line))
        
        # Clear the previous errors and show new ones
        self.play(*[FadeOut(error) for error in errors])
        new_errors = []
        for i, point in enumerate(data_points):
            predicted_y = 1.5 * point[0]  # new line formula: y = 1.5x
            error_line = Line(
                start=point[0] * RIGHT + point[1] * UP,
                end=point[0] * RIGHT + predicted_y * UP,
                color=RED
            )
            new_errors.append(error_line)
        
        self.play(*[Create(error) for error in new_errors])
        self.wait(1)

        # Repeat the process with another updated line, for example, m=1.7, b=0
        final_line = axes.plot(lambda x: 1.7 * x, color=YELLOW)
        self.play(Transform(line, final_line))

        self.play(*[FadeOut(error) for error in new_errors])
        final_errors = []
        for i, point in enumerate(data_points):
            predicted_y = 1.7 * point[0]  # final line formula: y = 1.7x
            error_line = Line(
                start=point[0] * RIGHT + point[1] * UP,
                end=point[0] * RIGHT + predicted_y * UP,
                color=RED
            )
            final_errors.append(error_line)

        self.play(*[Create(error) for error in final_errors])
        self.wait(2)