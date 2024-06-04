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
    def __init__(self,x,y,width,height, end, ):
        self.x = x
        self.y = y 
        self.aniCount = -1
        self.end = end 
        self.path = [self.x, self.y, end]
        self.width = width
        self.height = height
        self.animation = [pygame.image.load("enemy_ship0.png")]

class projectile(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bullet_ani = [pygame.image.load("projectile_1.png"), pygame.image.load("projectile_0.png"), pygame.image.load("projectile_2.png"), pygame.image.load("projectile_3.png"), pygame.image.load("projectile_4.png"), pygame.image.load("projectile_5.png"), pygame.image.load("projectile_6.png")]
        self.bulletCount = 0
        self.vel = 8 

    def draw(self,):
        #sometimes i wish i didn't want to animate litterally everything
        if self.bulletCount >= 7:
            self.bulletCount = 0
        self.bulletCount += 1
        win.blit(self.bullet_ani[self.bulletCount], (self.x) (self.y))

bgcount = 0




def redrawGameWindow():
    
    #All the things that run at the end

    #I have had SO MANY ERRORS
    #this section is the BANE of my existance
    win.blit(space, (0,0))
    win.blit(ui[bgcount],(0,0))
    ship.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
    

# variables
clock = pygame.time.Clock()
run = True
ship = player(500, 300, 32, 32)
bullet = projectile(32, 32)
bullets = []
shootloop = 0
# main loop:
while run:
    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0: #if on the screen
            bullet.x += bullet.vel #move the bullet by its vel (negative or positive)
        else:
            bullets.pop(bullets.index(bullet)) #else delete from the list


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
  
            
        
        bullets.append(projectile(round(ship.x + ship.width //2), round(ship.y + ship.height//2),))

            


    # calls the code we wrote before that blits objects onto the window.
    redrawGameWindow()


pygame.quit
