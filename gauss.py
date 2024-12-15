from manim import *

class GaussianElim(Scene):
    def construct(self):
        
        title = Tex("Gaussian Elmination")
        self.play(Write(title))
        self.wait(0.15)
        self.play(FadeOut(title))
        self.remove(title)
        
        # showing the equations
        eq1 = Tex("$x+y-z=-2$")
        eq2 = Tex("$2x-y+z=5$")
        eq3 = Tex("$-x+2y+2z=1$")
        self.play(Write(eq1))
        self.play(eq1.animate.shift(UP*0.6))
        self.play(Write(eq3))
        self.play(eq3.animate.shift(DOWN*0.6))
        self.play(Write(eq2))

        box = Rectangle(color=RED)
        self.play(Circumscribe(box, color=RED))

        self.play(Group(eq1,eq2,eq3).animate.shift(UP*2.75))

        # creating the augmented matrix
        self.wait(0.3)
        example = Matrix([[1,1,-1,-2],[2,-1,1,5],[-1,2,2,1]])
        values = example.get_entries()

        bar = Line(start=[1.4,1,0], end=[1.4,-1.1,0])
        self.play(Create(example))
        self.play(Write(bar))

        self.wait(0.25)

        # showing the operations

        example1 = Matrix([[1,1,-1," -2"],[2,-1,1," 5"],[0,3,1," -1"]])
        self.play(Transform(example,example1))
        self.play(bar.animate.move_to([1.3,-0.05,0]))
        self.wait(0.3)

        example2 = Matrix([[1,1,-1,-2],[0,-3,3,9],[0,3,1,-1]])
        self.play(Transform(example,example2))
        self.wait(0.3)

        example3 = Matrix([[1,1,-1,-2],[0,-3,3,9],[0,0,4,8]])
        self.play(Transform(example,example3))
        self.wait(0.3)

        example4 = Matrix([[1,1,-1,-2],[0,1,-1,-3],[0,0,4,8]])
        self.play(Transform(example,example4))
        self.wait(0.3)

        example5 = Matrix([[1,1,-1,-2],[0,1,-1,-3],[0,0,1,2]])
        self.play(Transform(example, example5))
        self.wait(0.3)


        # solving final matrix

        self.play(Group(eq1,eq2,eq3).animate.shift(UP*2.75))
        self.remove(eq1)
        self.remove(eq2)
        self.remove(eq3)

        self.play(Group(example,bar).animate.shift(UP*2.4))

        srow1 = Tex("$x+y-z=-2$")
        srow2 = Tex("$y-z=-3$")
        srow3 = Tex("$z=2$")
        self.play(Write(srow1))
        self.play(srow1.animate.shift(UP*0.6))
        self.play(Write(srow3))
        self.play(srow3.animate.shift(DOWN*0.6))
        self.play(Write(srow2))

        self.play(srow3.animate.shift(DOWN*1.8))

        subz = Tex("$y-2=-3$")
        solvey = Tex("$y=-3+2$")
        ansy = Tex("$y=-1$")
        self.play(Transform(srow2, subz))
        self.wait(0.07)
        self.play(Transform(srow2,solvey))
        self.wait(0.07)
        self.play(Transform(srow2, ansy))
        self.play(srow2.animate.shift(DOWN*1.9))


        subz2 = Tex("$x+y-2=-2$")
        suby = Tex("$x-1-2=-2$")
        simplify = Tex("$x-3=-2$")
        solvex = Tex("$x=-2+3$")
        ansx = Tex("$x=1$")

        self.play(Transform(srow1, subz2))
        self.wait(0.07)
        self.play(Transform(srow1, suby))
        self.wait(0.07)
        self.play(Transform(srow1, simplify))
        self.wait(0.07)
        self.play(Transform(srow1, solvex))
        self.wait(0.07)
        self.play(Transform(srow1, ansx))
        self.play(srow1.animate.shift(DOWN*1.25))

        self.wait(0.07)
        boxans = Rectangle().move_to([0,-1.8,0])
        self.play(Circumscribe(boxans, color=YELLOW))

        self.wait(3)