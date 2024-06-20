from manim import *
from manim_fonts import *
config.max_files_cached = -1

class FirstProplem(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=0, focal_distance=1000)

        circles = VGroup(
            Circle(2, YELLOW).move_to([0, 0, 1.5]),
            Circle(2, YELLOW).move_to([0, 0, -1.5])
        )
        vertical_axis = VGroup(
            DashedLine([0, 0, 2.5], [0, 0, -2.5], dash_length=.3),
            DashedLine([0, 0, 2.5], [0, 0, -2.5], dash_length=.09)
        )

        plane1 = VGroup(
            Polygon([1, 0, 0], [-1, 0, 0], [0, 4, 0], color=YELLOW_A, fill_opacity=1).scale(.1).move_to([2, 0, 1.5]).rotate(90*DEGREES, UP),
            Arrow3D([2, 0, 1.5], [2, 2, 1.5]),
            Arrow3D([2, 0, 1.5], [2, -2, 1.5]).fade(1)
        )
        plane2 = VGroup(
            Polygon([1, 0, 0], [-1, 0, 0], [0, -4, 0], color=YELLOW_A, fill_opacity=1).scale(.1).move_to([2, 0, -1.5]).rotate(90*DEGREES, UP),
            Arrow3D([2, 0, -1.5], [2, -3, -1.5]),
            Arrow3D([2, 0, -1.5], [2, 3, -1.5]).fade(1)
        )
        current_angle = 0

        self.add(circles, vertical_axis, plane1, plane2)

        self.play(plane1.animate.rotate(144*DEGREES, IN), MoveAlongPath(plane1, Arc(2, current_angle, 144*DEGREES).shift(OUT*1.5)), rate_functions=linear)
        
