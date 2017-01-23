import pygame, tree, item, random, backbone
from backbone import Vector2
pygame.init()

itemCreator = item.item()

size = width, height = 500, 600
white = 100,100,100

posTree = tree.StorageTree()
x = random.randint(0,440)
y = random.randint(0,540)
print(x,y)







posTree.insert([450,400],"lamp")
posTree.insert([250,400],"lamp")
posTree.insert([350,400],"lamp")
posTree.insert([150,400],"lamp")
posTree.insert([200,300],"lamp")
posTree.insert([100,300],"lamp")
posTree.insert([300,300],"lamp")
posTree.insert([400,300],"lamp")
posTree.insert([400,100],"lever")
posTree.insert([200,100],"lever")
posTree.insert([300,100],"lever")
posTree.insert([100,100],"lever")
lineArray = []

screen = pygame.display.set_mode(size)
screen.fill(backbone.background)

#screen.blit(posTree.root.childLeft.childRight.code.img, posTree.root.childLeft.childRight.pos.toArray())


clock = pygame.time.Clock()
oldMouseDown = pygame.mouse.get_pressed()
print(oldMouseDown[0])
while True:
  #clock.tick(60)

  for event in pygame.event.get():
    pass   

  screen.fill(backbone.background)

  for line in lineArray:
    pygame.draw.line(screen,(255,255,0),line[1],line[2],3)

  for result in posTree.readInOrder():
    screen.blit(result.code.img, result.code.pos.toArray())

  mousePos = Vector2(pygame.mouse.get_pos())#Vector2([310,410])#Vector2(pygame.mouse.get_pos()) ###
  mouseDown = pygame.mouse.get_pressed()
  results = posTree.getItemsMouse(mousePos)
  #print(clock.get_fps())

  #screen.blit(item.leverItem().img, [100,100])
  #print(pygame.mouse.get_rel())
  #pygame.draw.line(screen,(0,0,0),(0,0),(200,200),3)
  for result in results:
    if (mouseDown[0] == 1 and oldMouseDown[0] == 0):
      if type(result.code) == item.leverItem:
        result.code.toggleMouse()
      if type(result.code) == item.lampItem:
        lineArray = result.code.select(pygame.mouse,posTree,screen,lineArray)
      screen.blit(result.code.img, result.code.pos.toArray())

  

    #elif (mouseDown[0] == 1 and oldMouseDown[0] == 1z
      
      #result.code.drag()
      #screen.blit(result.code.img, result.code.pos.toArray())

      #result.code
  oldMouseDown = mouseDown
  pygame.display.flip()


