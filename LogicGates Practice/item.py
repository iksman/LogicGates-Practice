import pygame, random, backbone

class item:
  def create(type,position):
    if type.lower() == "lever":
      return leverItem(position)
    elif type.lower() == "lamp":
      return lampItem(position)

class leverItem:
  def __init__(self,position):
    self.img = pygame.Surface((50,70))
    self.img.fill((255,0,0))
    self.pos = position
    self.toggle = False
    self.out = []

  #def drag(self,relative):
  #  if relative != (0,0):
  #    self.pos.X += relative[0]
  #    self.pos.Y += relative[1]
  def getSize(self):
    return self.img.get_size()
  def toggleMouse(self):
    if not self.toggle:
      self.onMouse()
      if self.out != []:
        for it in self.out:
          it.toggleMouse(False)
      self.toggle = True
    else:
      self.revertOnMouse()
      if self.out != []:
        for it in self.out:
          it.toggleMouse(True)
      self.toggle = False
  def onMouse(self):
    self.img.fill((0,255,0))
  def revertOnMouse(self):
    self.img.fill((255,0,0))
  def set(self,code):
    self.out += [code]
  def remove(self,code):
    array = []
    for it in self.out:
      if it != code:
        array += [it]
    self.out = array
  


class lampItem:
  def __init__(self,position):
    self.img = pygame.Surface((50,70))
    self.img.fill((0,0,0))
    self.pos = position
    self.toggle = False
    self.receive = None

  #def drag(self,relative):
  #  if relative != (0,0):
  #    self.pos.X += relative[0]
  #    self.pos.Y += relative[1]
  def getSize(self):
    return self.img.get_size()

  def select(self,initialMouseState,list,screen,lineArray):
    oldPos = initialMouseState.get_pos()
    oldClick = pygame.mouse.get_pressed()[0]
    while True:
      for event in pygame.event.get():
        pass 

      newPos = pygame.mouse.get_pos()
      newClick = pygame.mouse.get_pressed()[0]

      pygame.draw.line(screen, backbone.background, oldPos, backbone.getCenter(self),3)

      for other in lineArray:
        pygame.draw.line(screen, backbone.line, other[1], other[2], 3)

      pygame.draw.line(screen, backbone.black, newPos, backbone.getCenter(self),3)

      for it in list.readInOrder():
        screen.blit(it.code.img, it.code.pos.toArray())

      pygame.display.flip()

      if oldClick == 0 and newClick == 1:
        check = list.getItemsMouse(backbone.Vector2(newPos))
        #print(check)
        if len(check) == 1:
          if (type(check[0].code) != lampItem):
            if self.receive != None: #Remove remnant code
              self.receive.remove(self)
              self.receive = None
              array = []
              for line in lineArray:
                if line[0] != self:
                  array += [line]
              lineArray = array
            check[0].code.set(self) 
            self.receive = check[0].code
            if (self.receive.toggle == True):
              self.onMouse()
              self.toggle = True
            else:
              if (self.toggle == True):
                self.revertOnMouse()
                self.toggle = False
            contains = False
            for line in lineArray:
              if line[0] == self:
                line[1] = backbone.getCenter(self.receive)#newPos
                line[2] = backbone.getCenter(self)
                contains = True
            if not contains:
              #print(backbone.getCenter(self))
              
              lineArray += [[self,backbone.getCenter(self.receive),backbone.getCenter(self)]]
        else:
          if (self.receive != None): #Remove remnant code
            self.toggle = False
            self.revertOnMouse()
            self.receive.remove(self)
            self.receive = None
            array = []
            for line in lineArray:
              if line[0] != self:
                array += [line]
            lineArray = array
                
        return lineArray

      oldPos = newPos
      oldClick = newClick

  def toggleMouse(self,boolvalue=None):
    if boolvalue != None:
      self.toggle = boolvalue
    if not self.toggle:
      self.onMouse()
      self.toggle = True
    else:
      self.revertOnMouse()
      self.toggle = False
  def onMouse(self):
    self.img.fill(backbone.white)
  def revertOnMouse(self):
    self.img.fill(backbone.black)


    


