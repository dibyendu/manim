import sys
import math


a, b = 4, 3.5
iteration = 10
focus_length = math.sqrt(a**2 - b**2)
origin, θ = (-focus_length, 0), 60


class EllipseRay(Scene):
  
  # ellipse: (x - h)**2 / a**2 + (y - k)**2 / b**2 = 1
  #    line: y = tan(θ) * x
  def find_intersection(self, a, b, h, k, θ):
    m = math.tan(math.radians(θ))
    D = 4*((h*b**2 + m*k*a**2)**2 - (b**2 + (m*a)**2) * ((h*b)**2 + (k*a)**2 - (a*b)**2))
    if D < 0:
      raise Exception('No real root found')
    x1 = (math.sqrt(D) - 2*(h*b**2 + m*k*a**2)) / (2*(b**2 + (m*a)**2))
    x2 = -(math.sqrt(D) + 2*(h*b**2 + m*k*a**2)) / (2*(b**2 + (m*a)**2))
    y1, y2 = m * x1, m * x2
  
    if abs(x1) < 1e-10 and abs(y1) < 1e-10:
      return x2 + h, y2 + k
    elif abs(x2) < 1e-10 and abs(y2) < 1e-10:
      return x1 + h, y1 + k
  
    x, y = x1, y1
    if θ < 180:
      x, y = (x1, y1) if y1 >= y2 else (x2, y2)
    elif θ == 180:
      x, y = x2, y2
    else:
      x, y = (x2, y2) if y1 >= y2 else (x1, y1)
    return x + h, y + k

  
  def find_intersection_after_reflection(self, a, b, x, y, θ):
    m = math.tan(math.radians(θ))
    slope = (m * y**2 * a**4 - m * x**2 * b**4 + 2 * x * b**2 * y * a**2) / \
            (    x**2 * b**4 -     y**2 * a**4 + 2 * x * b**2 * y * a**2 * m)
    θ = math.degrees(math.atan(slope))
    θ = 360 + θ if θ < 0 else θ
    x, y = self.find_intersection(a, b, x, y, θ)
    return θ, x, y

    
  def construct(self):
    global θ
    global origin

    x, y = origin
    if (x**2 / a**2 + y**2 / b**2) >= 1:
      print('Select a point within the ellipse')
      sys.exit(0)

    ellipse = Ellipse(width=2 * a, height=2 * b, color=BLUE, stroke_width=1)
    self.add(ellipse)

    point = Dot([*origin, 0], radius=0.04, color=RED)  
    path = TracedPath(point.get_center, stroke_width=0.8, dissipating_time=0.4, stroke_opacity=[0, 1])
    self.add(point, path)

    try:
      x, y = self.find_intersection(a, b, *origin, θ)
      self.play(point.animate.move_to([x, y, 0]))
      self.wait()
    except Exception as error:
      print(error)

    for _ in range(iteration):
      try:
        θ, x, y = self.find_intersection_after_reflection(a, b, x, y, θ)
        path = TracedPath(point.get_center, stroke_width=0.8, dissipating_time=0.4, stroke_opacity=[0, 1])
        self.add(path)
        self.play(point.animate.move_to([x, y, 0]))
        self.wait()
      except Exception as error:
        print(error)
