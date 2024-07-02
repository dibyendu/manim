import math


iteration = 6
colours = (BLUE, YELLOW, GREEN, GOLD, TEAL, WHITE, MAROON, ORANGE, PURPLE)


class RecursiveCircle(Scene):
  def animate(self, cx, cy, r, color, index, group):
    circle = Circle(radius=r, arc_center=[cx, cy, 0], color=color, stroke_width=1)
    radius = Line(start=[cx, cy, 0], end=[cx, cy - r, 0], color=color, stroke_width=1)
    text = Tex(rf'$R_{{{index}}}$', color=color, font_size=40)
    text.move_to([cx + 0.5, cy - r / 2, 0])
    group = Group(group, circle, radius, text)

    self.play(Create(circle))
    self.play(Create(radius), Write(text))
    self.wait()

    return group

  def construct(self):
    ratio = (math.sqrt(2) - 1)**2

    Cx, Cy, R = 0, 0, 3

    ax = Axes(
      x_range=[0, 10, 1],
      y_range=[0, 10, 1],
      tips=False,
      axis_config={
        'include_ticks': False,
        'include_numbers': False
      },
      x_length=2 * R,
      y_length=2 * R
    )
    ax.set_stroke(width=1)

    self.add(ax)
    g = Group(ax)
    g = self.animate(Cx, Cy, R, RED, 1, g)

    r = R * ratio
    cx, cy = Cx - R + r, Cy - R + r
    for i in range(iteration - 1):
      self.play(
        g.animate
        .shift([Cx - cx, Cy - cy, 0])
        .scale(1 / ratio, about_point=[0, 0, 0])
      )
      self.wait()

      g = self.animate(Cx, Cy, R, colours[i] if i < len(colours) else colours[i % len(colours)], i + 2, g)

    for _ in range(iteration - 1):
      self.play(
        g.animate
        .scale(ratio, about_point=[0, 0, 0])
        .shift([cx - Cx, cy - Cy, 0])
      )
      self.wait()

    text = Tex(r'$\frac{R_1}{R_{2000}} = ?$', color=WHITE, font_size=80)
    text.next_to(g, LEFT, buff=1)
    self.play(Write(text))
    self.wait()
