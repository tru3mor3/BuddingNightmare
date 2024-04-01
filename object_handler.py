# object handler
from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # spawn npc
        self.enemies = 20 # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        # add more sprites here as written below, each chunk of code is a room on the map
        
        # back garage area
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can1.PNG', pos=(1.75, 1.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can1.PNG', pos=(2.5, 1.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can1.PNG', pos=(3.25, 1.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can2.PNG', pos=(2.5, 7.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can3.PNG', pos=(3.5, 7.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'ladvert.PNG', pos=(1.15, 6.5), scale=0.85, shift=0.17))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'can4.PNG', pos=(1.25, 6)))

        # back bathroom
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'loo.PNG', pos=(7, 3.5), scale=1))

        # mother room
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 1.5), scale=1.5, shift=-0.05))

        # clone room
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 1.5), scale=0.5, shift=0.5))

        # med veg
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19.5, 1.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19.5, 2)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19.5, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19.5, 3)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19.5, 3.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(19, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(18.5, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(18, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(17.5, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(17, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(16.5, 2.5)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(16, 2.5)))

        # med flower 1
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 12.25)))

        # med flower 2
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 12.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 10.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 10.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 11.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 11.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 12.25)))

        # med flower 3
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 16.75)))

        # rec veg
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 16.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 14.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 15.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 15.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 16.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 16.75)))

        # rec flower 1
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 21.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 19.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 19.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 20.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 20.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 21.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 21.75)))

        # rec flower 2
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(2.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(3.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(4.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(5.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(6.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(7.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(8.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(9.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(10.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(11.5, 25.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 23.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 23.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 24.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 24.75)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 25.25)))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'weed1.PNG', pos=(12.5, 25.75)))

        # trim/weigh room


        # dry room


        # janitor closet


        # front bathroom


        # break room


        # office


        # front storage


        # front garage

        # npc map
        add_npc(CacoDemonNPC(game))
        add_npc(CyberDemonNPC(game, pos=(11.5, 6.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
