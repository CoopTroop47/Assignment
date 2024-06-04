import pygame
import sqlite3
pygame.init




# this name implies 4 other games and at least one other edition. 
# of course, these games do not exist, and i think that's funny.
pygame.display.set_caption('Space Runner 5: Ultimate Edition')




class datastore():
    def __init__(self):
        self.conn = sqlite3.connect("Assignment.db")
        self.cur = self.conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS
                users(userid INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)"""
        self.cur.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS
                    scores(scoreid INTEGER PRIMARY KEY  AUTOINCREMENT,
                    username TEXT, score INTEGER)"""
        self.cur.execute(sql)

    def users_to_db(self, username, password):
        print("users to db method called")
        self.cur.execute(
            """
                INSERT INTO users(username, password)
                VALUES (:Username, :Password)

            """,
            {
                'Username':username,
                'Password':password
            }
        )
        self.conn.commit

    def login_check(self, user, pw):
        results = self.cur.execute("""
                SELECT userid from users
                WHERE username = :username
                AND password = :password
                """,
                {
                    'username':user,
                    'password':pw
                }
            )
        rows = results.fetchall()
        print(rows)
        self.id = rows[0][0]
        print(self.id)



ds = datastore()
ds.users_to_db("Tom", "secret")

username = input('Username: ')
password = input('Password: ')
user = ds.login_check(username, password)
win = pygame.display.set_mode((1212, 608))
space = pygame.image.load('bg_0-1.png (1).png')
ui = [pygame.image.load('bg_new_0.png'), pygame.image.load('bg_new_1.png'),pygame.image.load('bg_new_2.png'),pygame.image.load('bg_new_3.png')]

#this convoluted mess of variables makes the player the bigger.
pa1 = pygame.image.load('player_ship0.png')
pa2 = pygame.image.load('player_ship1.png')
pa3 = pygame.image.load('player_ship2.png')



#beeg animation
animation = [pygame.transform.scale(pa1, (96, 96)), pygame.transform.scale(pa2, (96, 96)), pygame.transform.scale(pa3, (96, 96))]



# player class
class player(object):
    
    def __init__(self,x,y,width,height,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.flyCount = -1
       
# this is so pygame knows what to draw
    def draw(self, win):
        if self.flyCount >= 2:
            self.flyCount = -1
        self.flyCount += 1
        win.blit(animation[self.flyCount], (self.x,self.y))

class midEnemy(object):
    def __init__(self,x,y,width,height, end, basey):
        self.x = x
        self.y = y 
        self.aniCount = -1
        self.end = end 
        self.path = [end, self.y, self.x]
        self.width = width
        self.height = height
        self.vel = 8
        self.basey = basey
        self.ea1 = pygame.image.load("enemy_ship0.png")
        self.ea2 = pygame.image.load("enemy_ship1.png")
        self.ea3 = pygame.image.load("enemy_ship2.png")
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        self.move()
        if self.aniCount >= 2:
            self.aniCount = -1
        self.aniCount += 1
        win.blit(self.animation[self.aniCount], (self.x,self.y))
    def move(self):
        if self.vel > 0:
            if self.x < self.path[2] + self.vel:
                self.x += self.vel
                if self.y != 10:
                    self.y -= self.vel
            else: 
                self.vel = self.vel * -1
                self.x += self.vel
                #self.y -= self.vel
        elif score > 200:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
                #self.y -= self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.y += self.vel
        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.y += self.vel

        if score == 200 or 400 or 600:
            self.y = self.basey



class bigEnemy(object):
    def __init__(self,x,y,width,height, end, ):
        self.x = x
        self.y = y 
        self.aniCount = -1
        self.end = end 
        self.path = [end, self.y, self.x]
        self.width = width
        self.height = height
        self.vel = 8
        self.ea1 = pygame.image.load("Enemy_Large_0.png")
        self.ea2 = pygame.image.load("Enemy_Large_1.png")
        self.ea3 = pygame.image.load("Enemy_Large_2.png")
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        self.move()
        if self.aniCount >= 2:
            self.aniCount = -1
        self.aniCount += 1
        win.blit(self.animation[self.aniCount], (self.x,self.y))
    def move(self):
            if self.vel > 0:
                if self.x < self.path[2] + self.vel:
                    self.x += self.vel

                else: 
                    self.vel = self.vel * -1
                    self.x += self.vel
                    
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                    
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    



class boss(object):
    def __init__(self,x,y,width,height, end, ):
        self.x = x
        self.y = y 
        self.aniCount = -1
        self.end = end 
        self.path = [end, self.y, self.x]
        self.width = width
        self.height = height
        self.vel = 8
        self.ea1 = pygame.image.load("Enemy_massive_0.png")
        self.ea2 = pygame.image.load("Enemy_massive_1.png")
        self.ea3 = pygame.image.load("Enemy_massive_2.png")
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        if score > 600:
            self.move()
            if self.aniCount >= 2:
                self.aniCount = -1
            self.aniCount += 1
            win.blit(self.animation[self.aniCount], (self.x,self.y))
    def move(self):
            if self.vel > 0:
                if self.x < self.path[2] + self.vel:
                    self.x += self.vel

                else: 
                    self.vel = self.vel * -1
                    self.x += self.vel
                    
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                    
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    

class drone(object):
    def __init__(self,x,y,width,height, end,):
            self.x = x
            self.y = y 
            self.aniCount = -1
            self.end = end 
            self.path = [end, self.y, self.x]
            self.width = width
            self.height = height
            self.vel = 8
            self.ea1 = pygame.image.load("drone_0.png")
            self.ea2 = pygame.image.load("drone_1.png")
            self.ea3 = pygame.image.load("drone_2.png")
            self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        self.move()
        if self.aniCount >= 2:
            self.aniCount = -1
        self.aniCount += 1
        win.blit(self.animation[self.aniCount], (self.x,self.y))
    def move(self):
            if self.vel > 0:
                if self.x < self.path[2] + self.vel:
                    self.x += self.vel
                    #if self.y != 10:
                        #self.y -= self.vel
                else: 
                    self.vel = self.vel * -1
                    self.x += self.vel
                    #self.y -= self.vel
            elif score > 200:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                    #self.y -= self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    #self.y += self.vel
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    #self.y += self.vel

class projectile(object):
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.bullet_ani = [pygame.image.load("projectile_1.png"), pygame.image.load("projectile_0.png"), pygame.image.load("projectile_2.png"), pygame.image.load("projectile_3.png"), pygame.image.load("projectile_4.png"), pygame.image.load("projectile_5.png"), pygame.image.load("projectile_6.png")]
        self.bulletCount = 0
        self.vel = 8 
        self.fire = False

    def draw(self, win):
        if self.fire == True:
            if self.bulletCount >= 6:
                self.bulletCount = 0
            self.bulletCount += 1
            self.move()
            win.blit(self.bullet_ani[self.bulletCount], (self.x, self.y))
    def move(self):
        self.x += self.vel
        if bullet.x > 1200:
             bullets.pop(bullets.index(bullet))

        
        

#These variables has to go up here. I don't know why but pygame likes it this way.
bgcount = 0
ship = player(500, 300, 32, 32)
bullet = projectile(ship.x, ship.y)



def redrawGameWindow():
    
    #All the things that run at the end

    #I have had SO MANY ERRORS
    #this section is the BANE of my existance
    
    win.blit(space, (0,0))
    win.blit(ui[bgcount],(0,0))
    ship.draw(win)
    enemy1.draw(win)
    enemy2.draw(win)
    enemybig[0].draw(win) 
    enemybig[1].draw(win)
    enemybig[2].draw(win)
    for bullet in bullets:
        bullet.draw(win)
    print(score)
    drones[0].draw(win)
    drones[1].draw(win)
    drones[2].draw(win)
    drones[3].draw(win)
    enemyboss.draw(win)

    pygame.display.update()
    

# variables
score = 0
clock = pygame.time.Clock()
run = True
enemyboss = boss(1100, 200, 92, 92, 500)
enemy1 = midEnemy(1000, 100, 92, 92, 200, 100)
enemy2 = midEnemy(1000, 300, 92, 92, 200, 300)
enemybig = [bigEnemy(1000, 350, 92, 92, 300), bigEnemy(900, 200, 92, 92, 300), bigEnemy(1000, 60, 92, 92, 300) ]
#I want a lot of these ones, so i made a list!
drones = [drone(800, 250, 32, 32, 300, ), drone(9000, 200, 32, 32, 300, ), drone(9000, 100, 32, 32, 300,) , drone(800, 150, 32, 32, 300, )]

bullets = []

shootloop = 0
# main loop:
while run:
    score += 1
    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    


    bgcount += 1
    if bgcount > 3:
        bgcount = 0

    clock.tick(12)
    


    #closes the game safely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ship.y -= ship.vel
    if keys[pygame.K_DOWN]:
        ship.y += ship.vel
    if keys[pygame.K_LEFT]:
        ship.x -= ship.vel
    if keys[pygame.K_RIGHT]:
        ship.x += ship.vel

    if keys[pygame.K_SPACE] and shootloop == 0:
        bullet.fire = True
        bullets.append(projectile(ship.x, ship.y))
            
        
       

            


    # calls the code we wrote before that blits objects onto the window.
    redrawGameWindow()


pygame.quit

pygame.quit
