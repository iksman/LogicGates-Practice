from backbone import Vector2
import item

class StorageTree:
  def __init__(self,node=None):
    self.root = node

  def readInOrder(self,currentNode=None,result=None):
    if currentNode == None:
      currentNode = self.root
    if result == None:
      result = []
    if (currentNode.childLeft != None):
      result = self.readInOrder(currentNode.childLeft,result)
    result += [currentNode]
    if (currentNode.childRight != None):
      result = self.readInOrder(currentNode.childRight,result)

    return result


  def insert(self,position,code,checkX=True,currentNode=None):
    if (type(position) == list):
      position = Vector2(position[0],position[1])
    if self.root == None:
      self.root = StorageNode(position, code)
    else:
      if currentNode == None:
        currentNode = self.root
      
      if checkX:
        if currentNode.code.pos.X >= position.X:
          if currentNode.childLeft == None:
            currentNode.childLeft = StorageNode(position,code)
          else:
            self.insert(position,code,False,currentNode.childLeft) #
        else:
          if currentNode.childRight == None:
            currentNode.childRight = StorageNode(position,code)
          else:
            self.insert(position,code,False,currentNode.childRight) #
      else:
        if currentNode.code.pos.Y >= position.Y:
          if currentNode.childLeft == None:
            currentNode.childLeft = StorageNode(position,code)
          else:
            self.insert(position,code,True,currentNode.childLeft) #
        else:
          if currentNode.childRight == None:
            currentNode.childRight = StorageNode(position,code)
          else:
            self.insert(position,code,True,currentNode.childRight) #

  def getItemsMouse(self,mousePos,checkX=True,currentNode=None,results=None):
    if currentNode == None:
      currentNode = self.root
    if results == None:
      results = []
    isInsideX = False

    if ((mousePos.X >= currentNode.code.pos.X) and 
        (mousePos.X <= currentNode.code.pos.X + currentNode.code.img.get_width())):
      isInsideX = True
      if (checkX):
        if (currentNode.childLeft != None):
          results = self.getItemsMouse(mousePos,False,currentNode.childLeft,results)
        if (currentNode.childRight != None):
          results = self.getItemsMouse(mousePos,False,currentNode.childRight,results)
    elif(checkX):
      if(mousePos.X < currentNode.code.pos.X):
        if (currentNode.childLeft != None):
          results = self.getItemsMouse(mousePos,False,currentNode.childLeft,results)
      elif (mousePos.X > (currentNode.code.pos.X + currentNode.code.img.get_width())):
        if (currentNode.childRight != None):
          results = self.getItemsMouse(mousePos,False,currentNode.childRight,results)

    if ((mousePos.Y >= currentNode.code.pos.Y) and (mousePos.Y <= currentNode.code.pos.Y + currentNode.code.img.get_height())):
      if isInsideX:
        results += [currentNode]
      if (not checkX):
        if (currentNode.childLeft != None):
          results = self.getItemsMouse(mousePos,True,currentNode.childLeft,results)
        if (currentNode.childRight != None):
          results = self.getItemsMouse(mousePos,True,currentNode.childRight,results)
    elif(not checkX):
      if(mousePos.Y < currentNode.code.pos.Y):
        if (currentNode.childLeft != None):
          results = self.getItemsMouse(mousePos,True,currentNode.childLeft, results)
      elif(mousePos.Y > (currentNode.code.pos.Y + currentNode.code.img.get_height())):
        if (currentNode.childRight != None):
          results = self.getItemsMouse(mousePos,True,currentNode.childRight, results)
    return results


    

class StorageNode:
  def __init__(self,position,itemType):
    if (type(position) == list):
      position = Vector2(position[0],position[1]) #type Vector2

    self.code = item.item.create(itemType,position)
    self.childLeft = None
    self.childRight = None



