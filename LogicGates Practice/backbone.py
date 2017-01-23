black = (0,0,0)
background = (100,100,100)
line = (255,255,0)
white = (255,255,255)

def getCenter(code):
  xcor = code.pos.X + (code.img.get_width() / 2)
  ycor = code.pos.Y + (code.img.get_height() / 2)
  return (xcor,ycor)


class Vector2:
  def __init__(self,X,Y=None):
    if (Y == None ) and (type(X) == list or type(X) == tuple):
      self.X = X[0]
      self.Y = X[1]
    else:
      self.X = X
      self.Y = Y      
  def toArray(self):
    return [self.X, self.Y]
