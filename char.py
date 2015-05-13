from combat import Combat
class Character(Combat):
    exp = 0
    hit_points = 10

    
    def getWeapon(self):
        wep = raw_input('Weapon ([S]word [A]ss [N]igger: ').lower()
        
        if wep == 's':
            return 'sword'
        elif wep == 'a':
            return 'ass'
        elif wep == 'n':
            return 'nigger'
        else:
            return self.getWeapon()

    def __init__(self, **kwargs):
        self.name = raw_input('Name: ')
        self.weapon = self.getWeapon()
        
        for key, value in kwargs.items():
            setattr(self, key, value)
