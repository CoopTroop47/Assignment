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
        self.vel = 6
        self.flyCount = -1
        self.hitbox = (self.x + 20, self.y, 92, 92)
        self.visible = True
        self.iframes = 0
       
# this is so pygame knows what to draw
    def draw(self, win):
        if self.visible == True:
            if self.flyCount >= 2:
                self.flyCount = -1
            self.flyCount += 1
            win.blit(animation[self.flyCount], (self.x,self.y))
            self.hitbox = (self.x + 35, self.y + 25, 40, 40)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self,):
        print('hit')
        if hearts.hits < 3:
            hearts.hits += 1
        else: 
            self.visible = False
        self.iframes += 10

class midEnemy(object):
    def __init__(self,x,y,width,height, end, basey):
        self.x = x
        self.y = y 
        self.aniCount = -1
        self.end = end 
        self.path = [end, self.y, self.x]
        self.width = width
        self.height = height
        self.vel = 10
        self.basey = basey
        self.hitbox = (self.x + 20, self.y, 20, 60)
        self.health = 3
        self.visible = True
        self.ea1 = pygame.image.load("enemy_ship0.png")
        self.ea2 = pygame.image.load("enemy_ship1.png")
        self.ea3 = pygame.image.load("enemy_ship2.png")
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        if self.visible == True:
            self.move()
            if self.aniCount >= 2:
                self.aniCount = -1
            self.aniCount += 1
            win.blit(self.animation[self.aniCount], (self.x,self.y))
            self.hitbox = (self.x + 20, self.y + 25, 50, 50)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        print('hit')
        if self.health > 0:
            self.health -= 1
        else: 
            self.visible = False

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
        self.hitbox = (self.x + 20, self.y, 20, 60)
        self.vel = 8
        self.health = 5
        self.visible = True
        self.ea1 = pygame.image.load("Enemy_Large_0.png")
        self.ea2 = pygame.image.load("Enemy_Large_1.png")
        self.ea3 = pygame.image.load("Enemy_Large_2.png")
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        if self.visible == True:
            self.move()
            if self.aniCount >= 2:
                self.aniCount = -1
            self.aniCount += 1
            win.blit(self.animation[self.aniCount], (self.x,self.y))
            self.hitbox = (self.x + 20, self.y + 20, 50, 50)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
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
    def hit(self):
        print('hit')
        if self.health > 0:
            self.health -= 1
        else: 
            self.visible = False
                    



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
        self.health = 10
        self.visible = True
        self.ea1 = pygame.image.load("Enemy_massive_0.png")
        self.ea2 = pygame.image.load("Enemy_massive_1.png")
        self.ea3 = pygame.image.load("Enemy_massive_2.png")
        self.hitbox = (self.x + 30, self.y + 30, 30, 90)
        self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        if self.visible == True:
            if time > 600:
                self.move()
                if self.aniCount >= 2:
                    self.aniCount = -1
                self.aniCount += 1
                win.blit(self.animation[self.aniCount], (self.x,self.y))
                self.hitbox = (self.x + 30, self.y, 40, 100)
                #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    def move(self):
            if self.vel > 0:
                if self.y < self.path[1] + self.vel:
                    self.y += self.vel

                else: 
                    self.vel = self.vel * -1
                    self.y += self.vel
                    
            else:
                if self.y + self.vel > self.path[0]:
                    self.y += self.vel
                    
                else:
                    self.vel = self.vel * -1
                    self.y += self.vel
    def hit(self):
        print('hit')
        if self.health > 0:
            self.health -= 1
        else: 
            self.visible = False
                    

class drone(object):
    def __init__(self,x,y,width,height, end,):
            self.x = x
            self.y = y 
            self.aniCount = -1
            self.end = end 
            self.path = [end, self.y, self.x]
            self.width = width
            self.height = height
            self.vel = 15
            self.hitbox = (self.x + 20, self.y, 50, 50)
            self.health = 1
            self.visible = True
            self.ea1 = pygame.image.load("drone_0.png")
            self.ea2 = pygame.image.load("drone_1.png")
            self.ea3 = pygame.image.load("drone_2.png")
            self.animation = [pygame.transform.scale(self.ea1, (96, 96)), pygame.transform.scale(self.ea2, (96, 96)), pygame.transform.scale(self.ea3, (96, 96))]
    def draw(self, win):
        if self.visible == True:
            self.move()
            if self.aniCount >= 2:
                self.aniCount = -1
            self.aniCount += 1
            win.blit(self.animation[self.aniCount], (self.x,self.y))
            self.hitbox = (self.x + 40, self.y + 40, 10, 10)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
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
    def hit(self):
        print('hit')
        if self.health >= 0:
            self.health -= 1
        else: 
            self.visible = False
        

class projectile(object):
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.bullet_ani = [pygame.image.load("projectile_1.png"), pygame.image.load("projectile_0.png"), pygame.image.load("projectile_2.png"), pygame.image.load("projectile_3.png"), pygame.image.load("projectile_4.png"), pygame.image.load("projectile_5.png"), pygame.image.load("projectile_6.png")]
        self.bulletCount = 0
        self.vel = 15 
        self.fire = False
        self.hitbox = (self.x, self.y + 10, 40, 10)
        

    def draw(self, win):
        if self.bulletCount >= 6:
            self.bulletCount = 0
        self.bulletCount += 1
        self.move()
        win.blit(self.bullet_ani[self.bulletCount], (self.x, self.y))
    def move(self):
        self.x += self.vel
        self.hitbox = (self.x, self.y + 10, 40, 10)
        

class healthui(object):
    def __init__(self, x, y):
        self.hp_3 = pygame.image.load("life_0.png")
        self.hp_2 = pygame.image.load("life_1.png")
        self.hp_1 = pygame.image.load("life_2.png")
        self.hp_0 = pygame.image.load("life_3.png")
        self.hp = [pygame.transform.scale(self.hp_3, (128, 128)), pygame.transform.scale(self.hp_2, (128, 128)), pygame.transform.scale(self.hp_1, (128, 128)),pygame.transform.scale(self.hp_0, (128, 128)),]
        self.hits = 0
        self.x = x
        self.y = y
    def draw(self, win):
        win.blit(self.hp[self.hits], (self.x, self.y))
    #The player hp actually goes down here
    #i wanted a visual representation of health
    #so no need for the player to have it's own hp variable

        
        

#These variables has to go up here. I don't know why but pygame likes it this way.
bgcount = 0
ship = player(500, 300, 32, 32)
bulletnum = 0




def redrawGameWindow():
    
    #All the things that run at the end

    
    win.blit(space, (0,0))
    win.blit(ui[bgcount],(0,0))

    ship.draw(win)
    enemy1.draw(win)
    enemy2.draw(win)
    hearts.draw(win)
    enemybig[0].draw(win) 
    enemybig[1].draw(win)
    enemybig[2].draw(win)
    drones[0].draw(win)
    drones[1].draw(win)
    drones[2].draw(win)
    drones[3].draw(win)
    enemyboss.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


    

# variables
hearts = healthui(800, 500)
time = 0
score = 0
clock = pygame.time.Clock()
run = True
enemyboss = boss(1100, 350, 92, 92, 50)
enemy1 = midEnemy(900, 100, 92, 92, 200, 100)
enemy2 = midEnemy(900, 300, 92, 92, 200, 300)
enemybig = [bigEnemy(1000, 350, 92, 92, 300), bigEnemy(800, 200, 92, 92, 300), bigEnemy(1000, 60, 92, 92, 300) ]
#I want a lot of these ones, so i made a list!
drones = [drone(950, 250, 32, 32, 200, ), drone(800, 390, 32, 32, 300, ), drone(800, 10, 32, 32, 300,) , drone(950, 150, 32, 32, 200, )]

bullets = []



shootloop = 0
# main loop:
while run:
    time += 1
    if shootloop > 0:
        shootloop += 1
    if shootloop > 15:
        shootloop = 0
    if ship.iframes > 0:
        ship.iframes -= 1

    for bullet in bullets:
        if bullet.x < 1200 and bullet.x > 0: # If bullet is on the screen
            # collision with enemies:
            for enemy in [enemy1, enemy2] + drones + enemybig + [enemyboss]:
                if enemy.visible:
                    #I had like 8 billion lines of code to do this
                    # I figured out i could just put everything in lists
                    # so i did the tried and true method of making variables and lists until it works
                    if (bullet.y < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y > enemy.hitbox[1] and bullet.x > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]):
                        # hits:
                        if enemy in [enemy1, enemy2, enemyboss]:
                            enemy.hit()
                            score += 100 if enemy in [enemy1, enemy2] else 500
                            bullets.pop(bullets.index(bullet))
                        else:
                            enemy.hit()
                            score += 50
                            bullets.pop(bullets.index(bullet))
                        
                        #I know you don't like breaks.
                        #oh well.
                        break
        #this deletes bullets that go off-screen           
        else:
            bullets.pop(bullets.index(bullet))



        # Handle collision with ship
    if ship.iframes == 0 and ship.visible:
        # had issues with the player dying too quickly.
        # so i added i-frames,
        for enemy in [enemy1, enemy2] + drones + enemybig + [enemyboss]:
            if (ship.y > enemy.hitbox[1] and ship.y < enemy.hitbox[1] + enemy.hitbox[3] and ship.x > enemy.hitbox[0] and ship.x < enemy.hitbox[0] + enemy.hitbox[2]):
                ship.hit()
                score -= 100
                break



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
        bulletnum += 1
        bullets.append(projectile(ship.x + ship.width//2, ship.y + ship.height//2))
        shootloop += 5




    # calls the code we wrote before that blits objects onto the window.
    redrawGameWindow()


pygame.quit
