from evennia.utils.evmenu import EvMenu
from evennia.contrib.dice import roll_dice
from evennia.utils.create import create_object
from evennia import create_script
from timeit import default_timer as timer

damage = 0
# Menu implementing the dialogue tree
def exit_combat(caller):
    caller.execute_cmd('Exit')

def attack_node(caller):
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: O O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: / O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: / / O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: / / / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: / / / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: / / / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: / / / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: / / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 11)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 12)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 13)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0
		

	if((caller.db.lethal == 0 ) and ( caller.db.bashing >= 14)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X / O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X / / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X / / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X / / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X / / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /  ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 11)):
		caller.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 12)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X / O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X / / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X / / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X / / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X / / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X X / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /   ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0
		
		

	if((caller.db.lethal == 2 ) and ( caller.db.bashing >= 11)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	
	
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0
		

	if((caller.db.lethal == 3 ) and ( caller.db.bashing >= 8)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0


	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X X X / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.conscious = 0

		

	if((caller.db.lethal == 4 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	

	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 5 ) and ( caller.db.bashing >= 4)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0		

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X O")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 6 ) and ( caller.db.bashing >= 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		

	if((caller.db.lethal >= 7 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: O O O O O O O")
		caller.db.target.db.conscious = 1
		

	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: / O O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: / / O O O O O")
		caller.db.target.db.conscious = 1
			
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 12)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 13)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing >= 14)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X O O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X / O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /  ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing >= 12)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /   ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing >= 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
	
	
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing >= 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0


	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
	

	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing >= 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0		

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing >= 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		

	if((caller.db.target.db.lethal >= 7 ) and ( caller.db.target.db.bashing >= 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0	


	caller.db.start_time = timer()

	attack_script = create_script("typeclasses.attackwait.AttackTime", obj=caller)
	attack_script.attacker(caller)
	attack_script.target(caller.db.target)

	text = ""

	options = ({"key": "|ypunch",
		"desc": "Punch %s" % caller.db.target,
		"goto": "wait",
		"exec": "punch"},
		{"key": "|ykick",
		"desc": "Kick %s" % caller.db.target,
		"goto": "wait",
		"exec": "kick"},
		{"key": "|ywield",
		"desc": "Wield a weapon",
		"goto": "wield",
		"exec": "wield"},
		{"key": "|yFlee",
		"desc": "Quit attacking",
		"goto": "wait",
		"exec": "flee_attack"},
		{"key": "|yskip",
		"desc": "Do nothing",
		"goto": "skip_attack"},)

	for each in caller.contents:
		if(each.key == caller.db.selected_weapon):
			if(each.db.weapon == 1):
				options += ({"key": "|y" + each.key,
					"desc": "An axe.",
					"goto": "wait",
					"exec": "axe"},)
			if(each.db.weapon == 2):
				options += ({"key": "|y" + each.key,
					"desc": "A knife.",
					"goto": "wait",
					"exec": "knife"},)
			if(each.db.weapon == 3):
				options += ({"key": "|y" + each.key,
					"desc": "A baseball bat.",
					"goto": "wait",
					"exec": "bat"},)
			if(each.db.weapon == 4):
				options += ({"key": "|y" + each.key,
					"desc": "A staff.",
					"goto": "wait",
					"exec": "staff"},)
			if(each.db.weapon == 5):
				options += ({"key": "|y" + each.key,
					"desc": "A sword.",
					"goto": "wait",
					"exec": "katana"},)


	if(caller.db.conscious == 0 and caller.db.alive == 1):
		options = ({"key": "_default",
			"goto": "skip_attack"})

        if(caller.db.move_speed == "freeze"  and caller.db.alive == 1):
                options = ({"key": "_default",
                        "goto": "skip_attack"})

	return text, options


def select_weapon(caller, input):
	caller.db.start_time = 99999999999999999999999
	caller.db.selected_weapon = input 
	caller.db.target.msg("|/|g%s wield his %s." % (caller.name, caller.db.selected_weapon))
	text = ("|/|gYou wield the %s" % input)
	EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)

	options = ({"key": "_default", 
		"goto": "skip_attack"})
	return text, options

def remove_weapon(caller, input):
        caller.db.start_time = 99999999999999999999999
        caller.db.target.msg("|/|g%s puts his %s away." % (caller.name, caller.db.selected_weapon))
        text = ("|/|gYou put your %s away" % caller.db.selected_weapon)
        caller.db.selected_weapon = "None"
        EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)

        options = ({"key": "_default", 
                "goto": "skip_attack"})
        return text, options

def wield(caller):
	caller.db.start_time = timer() - 7
	text = ""
	options = ()
	for each in caller.contents:
		options += ({"key": "|y" + each.name,
			"desc": "appearances",
			"goto": "select_weapon"},)
	options += ({"key": "|y remove",
                "desc": "remove weapons",
                "goto": "remove_weapon"},
                {"key": "_default",
		"goto": "skip_attack"},)

	return text, options

def punch(caller):
	caller.db.weapon = 0
	test = caller.db.dexterity + caller.db.brawl
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou punch %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to punch you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s punches, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	return text, options


def kick(caller):
	caller.db.weapon = 0
	test = caller.db.dexterity + caller.db.brawl
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 7):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength + 1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou kick %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to kick you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s kicks, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	return text, options

def axe(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 7):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+3
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def knife(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 4):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def bat(caller):
	caller.db.weapon = 0

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 5):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+2
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def staff(caller):
	caller.db.weapon = 0

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+1
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def katana(caller):
	caller.db.weapon = 1

	test = caller.db.dexterity + caller.db.melee
	counter = 0
	attackpoints = 0
	while(counter < test):
		counter = counter + 1
		roll = roll_dice(1,10)
		if(roll >= 6):
			attackpoints = attackpoints + 1

	global damage
	damage = attackpoints

	hit = caller.db.strength+3
	counter = 0
	attackpoints2 = 0
	while (counter < hit):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			attackpoints2 = attackpoints2 + 1

	global damage2
	damage2 = attackpoints2

	caller.db.start_time = 99999999999999999999999
	if (attackpoints > 0):
		caller.msg("|/|gYou strike %s with %i success rolls. " % (caller.db.target, attackpoints))
		caller.db.target.msg("|/|g%s attempts to strike you with %i succesful rolls." % (caller, attackpoints))
		EvMenu(caller.db.target, "typeclasses.menu", startnode="defend_node", auto_quit=False, cmd_on_exit=None)
	else:
		caller.msg("|/|gYou miss %s." % caller.db.target)
		caller.db.target.msg("|/|g%s strikes, but misses you." % caller)
		EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
				"goto": "skip_attack"})
	return text, options

def wait(caller):
    caller.db.start_time = 99999999999999999999999
    text = ""
    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def finish(caller):
	caller.db.start_time = 99999999999999999999
	EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = {"key": "_default",
		"goto": "wait"}
	return text, options

def skip_attack(caller):
    caller.db.start_time = 99999999999999999999999
    if(caller.db.move_speed == "freeze"):
        caller.msg("Time is moving too slow to react") 
    if(caller.db.conscious == 0 and caller.db.alive ==1):
        text = "|r You are unconscious!"
        caller.db.target.msg("|/|r %s is unconscious."% caller)
    if(caller.db.conscious == 1 or caller.db.alive == 0):
        text = "|r You have skipped your turn!"
    EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)

    if(caller.db.alive == 0):
        caller.db.conscious = 1
        caller.msg("|/|rYou are dead!")
        caller.db.target.msg("|/|r%s is dead!"% caller)
        caller.ndb._menutree.close_menu()
        caller.db.target.ndb._menutree.close_menu()
	corpse1 = create_object(key="Corpse", location = caller.location)
	print(caller.location)
        corpse1.attributes.add("target", caller.db.target)
        corpse1.attributes.add("lastname", caller)
	corpse1.db.description = "A bloody mess of flesh and broken bones."
        text = ""
        options = ()


    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def skip_defend(caller):
    caller.db.start_time = 99999999999999999999999
    caller.msg("|/|rYou have been hit by %s.|/" % caller.db.target)
    if(caller.db.conscious == 0):
        caller.db.target.msg("|/|r%s is unconscious.|/" % caller)
    if(caller.db.conscious == 1):
        caller.db.target.msg("|/|r%s has skipped his turn.|/" % caller)

    if(caller.db.conscious == 0 and caller.db.alive == 1):
        text = "|/|rYou are unconscious!"
    if(caller.db.conscious == 1 or caller.db.alive == 0):
        text = "|/|r You have skipped your turn!"
    EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)

    if(caller.db.alive == 0):
        caller.db.conscious = 1
        caller.msg("|rYou are dead!")
        caller.db.target.msg("|/|r%s is dead!"% caller)
        caller.ndb._menutree.close_menu()
        caller.db.target.ndb._menutree.close_menu()
	corpse2 = create_object(key="Corpse", location = caller.location)
        corpse2.attributes.add("target", caller.db.target)
        corpse2.attributes.add("lastname", caller)
	corpse2.db.description = "A bloody mess of flesh and broken bones."
       	print(caller.location)
	text = ""
        options = ()


    options = {"key": "_default",
               "goto": "wait"}
    return text, options

def defend_node(caller):
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: O O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: / O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: / / O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: / / / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: / / / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: / / / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: / / / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: / / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 11)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 12)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 0 ) and ( caller.db.bashing == 13)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 0 ) and ( caller.db.bashing >= 14)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X O O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X / O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X / / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X / / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X / / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X / / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X / / / / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 1 ) and ( caller.db.bashing == 11)):
		caller.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 1 ) and ( caller.db.bashing >= 12)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X O O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X / O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X / / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X / / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X / / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X / / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 8)):
		caller.msg(prompt="|X|[wHealth: X X X X X / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 9)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 2 ) and ( caller.db.bashing == 10)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
                caller.db.alive = 0

		

		

	if((caller.db.lethal == 2 ) and ( caller.db.bashing >= 11)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	
	

	
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X O O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X / O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X / / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X / / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 6)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 3 ) and ( caller.db.bashing == 7)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 3 ) and ( caller.db.bashing >= 8)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0


	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X O O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X / O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X / / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 4)):
		caller.msg(prompt="|X|[wHealth: X X X X X / / ")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 4 ) and ( caller.db.bashing == 5)):
		caller.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 4 ) and ( caller.db.bashing >= 6)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	

	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X O O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X / O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.conscious = 0
		
	if((caller.db.lethal == 5 ) and ( caller.db.bashing == 3)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 5 ) and ( caller.db.bashing >= 4)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0		

	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X O")
		caller.db.conscious = 1
		
	if((caller.db.lethal == 6 ) and ( caller.db.bashing == 1)):
		caller.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.conscious = 0

		

		

	if((caller.db.lethal == 6 ) and ( caller.db.bashing >= 2)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
		

	if((caller.db.lethal >= 7 ) and ( caller.db.bashing >= 0)):
		caller.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.conscious = 1
		caller.db.alive = 0
	
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: O O O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: / O O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: / / O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: / / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 12)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing == 13)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 0 ) and ( caller.db.target.db.bashing >= 14)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X O O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X / O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / /  ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 1 ) and ( caller.db.target.db.bashing == 12)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / O O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X / / / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /   ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 9)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing == 10)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		

	if((caller.db.target.db.lethal == 2 ) and ( caller.db.target.db.bashing >= 11)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
	
	
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X O O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing == 7)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		


	if((caller.db.target.db.lethal == 3 ) and ( caller.db.target.db.bashing >= 8)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0


	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X O O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / / ")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing == 5)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
		caller.db.target.db.conscious = 0

		

	if((caller.db.target.db.lethal == 4 ) and ( caller.db.target.db.bashing >= 6)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
	

	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X O O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
		caller.db.target.db.conscious = 0
		
	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing == 3)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		

	if((caller.db.target.db.lethal == 5 ) and ( caller.db.target.db.bashing >= 4)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0		

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X O")
		caller.db.target.db.conscious = 1
		
	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing == 1)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
		caller.db.target.db.conscious = 0

		

	if((caller.db.target.db.lethal == 6 ) and ( caller.db.target.db.bashing >= 2)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0
		

	if((caller.db.target.db.lethal >= 7 ) and ( caller.db.target.db.bashing >= 0)):
		caller.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
		caller.db.target.db.conscious = 1
		caller.db.target.db.alive = 0	


	caller.db.target.start_time = timer()

	defend_script = create_script("typeclasses.defendwait.DefendTime", obj=caller)
	defend_script.attacker(caller)
	defend_script.target(caller.db.target)

	text = ""
	options = ({"key": "|ydodge",
		"desc": "Avoid the attack.",
		"goto": "wait",
		"exec": "dodge"},
		{"key": "|yblock",
		"desc": "Block the attack.",
		"goto": "wait",
		"exec": "block"},
		{"key": "|yflee",
		"desc": "Run away.",
		"goto": "wait",
		"exec": "flee"},)


	if(caller.db.alive == 0):
                calle.ndb.end_combat = 0
                caller.db.target.ndb.end_combat = 0
		caller.db.conscious = 1
		caller.msg("|rYou are dead!")
		caller.db.target.msg("|/|r%s is dead!"% caller)
		caller.ndb._menutree.close_menu()
		caller.db.target.ndb._menutree.close_menu()
		corpse3 = create_object(key="Corpse", location = caller.location)
		corpse3.db.description = "A bloody mess of flesh and broken bones."
		corpse3.attributes.add("target", caller.db.target)
                corpse3.attributes.add("lastname", caller)
                print(caller.location)
		text = ""
		options = ()

	if(caller.db.conscious == 0 and caller.db.alive == 1):
		options = ({"key": "_default",
		"goto": "new_skip"})

        if(caller.db.move_speed == "freeze" and caller.db.alive == 1):
                options = ({"key": "_default",
                "goto": "new_skip"})

	return text, options

def dodge(caller):
	test = caller.db.dexterity + caller.db.athletics
	soak = caller.db.stamina
	counter = 0
	defendpoints = 0
	while (counter < test):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			defendpoints = defendpoints + 1

	counter = 0
	soakpoints = 0
	while (counter < soak):
		counter = counter + 1
		roll = roll_dice(1,10)
		if (roll >= 6):
			soakpoints = soakpoints + 1
	dmg = damage
	caller.db.start_time = 99999999999999999999999
	if (defendpoints > 0):
		tst = damage2
		dmg2 = damage
		cnt2 = 0
		while (cnt2 < tst):
			cnt2 = cnt2 + 1
			roll = roll_dice(1, 10)
			if (roll >= 6):
				dmg = dmg + 1

		reduced =  dmg - defendpoints
		if(reduced < 0):
			reduced = 0
		if(defendpoints >= dmg2):
			defendpoints = dmg2
			reduced = 0

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|gYou dodge %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, reduced))
			if (soakpoints > reduced):
				soakpoints = reduced
			if (soakpoints > 0):
				caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, reduced))
			if (reduced - soakpoints > 0):
				caller.msg("|/|gYou lose a total of %i health points." % (reduced - soakpoints))
				caller.db.bashing = caller.db.bashing + (reduced - soakpoints)
			caller.db.target.msg("|/|g%s dodges %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of damage with your punch." % (reduced))
	
			if(soakpoints>0):
				caller.db.target.msg("|/|g%s soaks %i points of damage from your punch." % (caller, soakpoints))
			if(reduced-soakpoints > 0):
				caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, reduced - soakpoints))

		if(caller.db.target.db.weapon == 1):
			caller.msg("|/|gYou dodge %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, reduced))
			caller.db.lethal = caller.db.lethal + reduced
			caller.db.target.msg("|/|g%s dodges %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of lethal damage." % (reduced))
			
	else:
		caller.msg("|/|rYou have been hit by %s." % caller.db.target)
		caller.db.target.msg("|/|r%s fails to dodge your attack." % caller)

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, dmg))
			caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, dmg))
			caller.msg("|/|gYou lose a total of %i health points." % (dmg - soakpoints))
			caller.db.bashing = caller.db.bashing + (dmg - soakpoints)
			caller.db.target.msg("|/|gYou deal %i points of damage with your punch." % (dmg))
			caller.db.target.msg("|/|g%s soaks %i points of damage from your punch." % (caller, soakpoints))
			caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, dmg - soakpoints))

                if(caller.db.target.db.weapon == 1):
                        caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, dmg))
                        caller.db.lethal = caller.db.lethal + dmg 
                        caller.db.target.msg("|/|gYou deal %i points of lethal damage to %s." % (dmg, caller))
                        caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, dmg))

	EvMenu(caller, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	
	if(caller.db.alive == 0 or caller.db.target.db.alive == 0):
                calle.ndb.end_combat = 0
                caller.db.target.ndb.end_combat = 0
		caller.db.conscious = 1
		caller.db.target.db.conscious = 1
		caller.msg("|rGAMEOVER")
		caller.db.target.msg("|rGAMEOVER")
		caller.db.target.ndb._menutree.close_menu()
		caller.ndb._menutree.close_menu()
		corpse5 = create_object(key="Corpse", location = caller.location)
                corpse5.attributes.add("target", caller.db.target)
                corpse5.attributes.add("lastname", caller)
		corpse5.db.description = "A bloody mess of flesh and broken bones."
		print(caller.location)
		text = ""
		options = ()

	return text, options


def block(caller):
	test = caller.db.dexterity + caller.db.brawl
	soak = caller.db.stamina
	counter = 0
	defendpoints = 0
	while (counter < test):
		counter = counter + 1
		roll = roll_dice(1, 10)
		if (roll >= 6):
			defendpoints = defendpoints + 1

	counter = 0
	soakpoints = 0
	while (counter < soak):
		counter = counter + 1
		roll = roll_dice(1,10)
		if (roll >= 6):
			soakpoints = soakpoints + 1
	dmg = damage
	caller.db.start_time = 99999999999999999999999
	if (defendpoints > 0):
		tst = damage2
		dmg2 = damage
		cnt2 = 0
		while (cnt2 < tst):
			cnt2 = cnt2 + 1
			roll = roll_dice(1, 10)
			if (roll >= 6):
				dmg = dmg + 1

		reduced =  dmg - defendpoints
		if(reduced < 0):
			reduced = 0
		if(defendpoints >= dmg2):
			defendpoints = dmg2
			reduced = 0

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|gYou block %i out of %i of %s's attack points." % (defendpoints, dmg2, caller.db.target))
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, reduced))
			if (soakpoints > reduced):
				soakpoints = reduced
			if (soakpoints > 0):
				caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, reduced))
			if (reduced - soakpoints > 0):
				caller.msg("|/|gYou lose a total of %i health points." % (reduced - soakpoints))
				caller.db.bashing = caller.db.bashing + (reduced - soakpoints)
			caller.db.target.msg("|/|g%s blocks %i points of your attack." % (caller, defendpoints))
			caller.db.target.msg("|/|gYou deal %i points of damage with your attack." % (reduced))
	
			if(soakpoints>0):
				caller.db.target.msg("|/|g%s soaks %i points of damage from your attack." % (caller, soakpoints))
			if(reduced-soakpoints > 0):
				caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, reduced - soakpoints))

		if(caller.db.target.db.weapon == 1):
			caller.msg("|/|gYou can't block %s's attack points." % (caller.db.target))
			caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, dmg))
			caller.db.lethal = caller.db.lethal + dmg
			caller.db.target.msg("|/|g%s fails to block your attack." % (caller))
			caller.db.target.msg("|/|gYou deal %i points of lethal damage." % (dmg))
			
	else:
		caller.msg("|/|rYou have been hit by %s." % caller.db.target)
		caller.db.target.msg("|/|r%s fails to dodge your attack." % caller)

		if(caller.db.target.db.weapon == 0):
			caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, dmg))
			caller.msg("|/|gYou soak %i out of %i points of bashing damage." % (soakpoints, dmg))
			caller.msg("|/|gYou lose a total of %i health points." % (dmg - soakpoints))
			caller.db.bashing = caller.db.bashing + (dmg - soakpoints)
			caller.db.target.msg("|/|gYou deal %i points of damage with your punch." % (dmg))
			caller.db.target.msg("|/|g%s soaks %i points of damage from your punch." % (caller, soakpoints))
			caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, dmg - soakpoints))

		if(caller.db.target.db.weapon == 1):
			caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, dmg))
			caller.msg("|/|gYou lose a total of %i health points." % (dmg))
			caller.db.lethal = caller.db.lethal + dmg
			caller.db.target.msg("|/|gYou deal %i points of lethal damage with your attack." % (dmg))
			caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, dmg))


	EvMenu(caller, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)
	text = ""
	options = ({"key": "skip",
		"goto": "skip_attack"})
	
	if(caller.db.alive == 0 or caller.db.target.db.alive == 0):
                calle.ndb.end_combat = 0
                caller.db.target.ndb.end_combat = 0
		caller.db.conscious = 1
		caller.db.target.db.conscious = 1
		caller.msg("|rGAMEOVER")
		caller.db.target.msg("|rGAMEOVER")
		caller.db.target.ndb._menutree.close_menu()
		caller.ndb._menutree.close_menu()
		text = ""
		options = ()

	return text, options

def flee_attack(caller):
    caller.db.start_time = 99999999999999999999999
    caller.msg("|/|rYou flee from combat!|/|/")
    caller.db.target.msg("|/|r%s flees from combat!|/|/" % caller)
    caller.ndb._menutree.close_menu()
    if(caller.db.target.ndb._menutree):
        caller.db.target.ndb._menutree.close_menu()
    calle.ndb.end_combat = 0
    caller.db.target.ndb.end_combat = 0
    caller.execute_cmd('look')
    caller.db.target.execute_cmd('look')
    text = ""
    options = ()
    return text, options

def flee(caller):
    caller.db.start_time = 99999999999999999999999

    init_a = caller.db.dexterity + caller.db.wits
    init_b = caller.db.target.db.dexterity + caller.db.target.db.wits
    init_a = init_a + roll_dice(1,10)
    init_b = init_b + roll_dice(1,10)
    if(init_a > init_b):
        caller.msg("|yYou flee from combat!")
        caller.db.target.msg("|y%s flees from combat" % caller)
        caller.db.target.ndb._menutree.close_menu()
        caller.ndb._menutree.close_menu()
        calle.ndb.end_combat = 0
        caller.db.target.ndb.end_combat = 0
    else:
        caller.msg("|yYou fail to flee from combat")
        caller.db.target.msg("|y%s fails to flee from combat" % caller)
        if(caller.db.target.db.weapon == 1):
            caller.msg("|/|g%s causes %i points of lethal damage to you." % (caller.db.target, damage))
            caller.msg("|/|gYou lose a total of %i health points." % (damage))
            caller.db.lethal = caller.db.lethal + damage
            caller.db.target.msg("|/|gYou deal %i points of lethal damage with your attack." % (damage))
            caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, damaga))
        if(caller.db.target.db.weapon == 0):
            caller.msg("|/|g%s causes %i points of bashing damage to you." % (caller.db.target, damage))
            caller.msg("|/|gYou lose a total of %i health points." % (damage))
            caller.db.bashing = caller.db.bashing + damage
            caller.db.target.msg("|/|gYou deal %i points of bashing damage with your attack." % (damage))
            caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, damage))
        EvMenu(caller, "typeclasses.menu", startnode="attack_node", auto_quit=False, cmd_on_exit=None)

    text = ""
    options = ()
    return text, options

def new_skip(caller):
        if(caller.db.move_speed == "freeze"): 
            caller.msg("Time is moving too slow to react") 
	caller.msg("|/|rYou have been hit by %s." % caller.db.target)
	caller.db.target.msg("|/|r%s fails to dodge your attack." % caller)

	if(caller.db.target.db.weapon == 0):
		caller.msg("|/|g%s causes %i points of damage to you." % (caller.db.target, damage))
		caller.msg("|/|gYou lose a total of %i health points." % damage)
		caller.db.bashing = caller.db.bashing + damage
		caller.db.target.msg("|/|gYou deal %i points of damage with your punch." % damage)
		caller.db.target.msg("|/|g%s loses a total of %i hit points." % (caller, damage))

        if(caller.db.conscious == 0 and caller.db.alive == 1):
            text = "|r You are unconscious."
            caller.db.target.msg("|/|r%s is unconscious. "% caller)
        if(caller.db.conscious == 1 or caller.db.alive == 0):
	    text = "|r You have skipped your turn!"
	EvMenu(caller.db.target, "typeclasses.menu", startnode="attack_node",auto_quit=False, cmd_on_exit=None)

	if(caller.db.alive == 0):
		caller.db.conscious = 1
		caller.msg("|rYou are dead!")
		caller.db.target.msg("|/|r%s is dead!"% caller)
		caller.ndb._menutree.close_menu()
		caller.db.target.ndb._menutree.close_menu()
		corpse4 = create_object(key="Corpse", location = caller.location)
		corpse4.db.description = "A bloody mess of flesh and broken bones."
                corpse4.attributes.add("target", caller.db.target)
                corpse4.attributes.add("lastname", caller)
		print(caller.location)
		text = ""
		options = ()


	options = {"key": "_default",
		"goto": "wait"}
	return text, options


def END(caller):
    caller.msg("EXIT COMBAT")
    caller.db.target.msg("EXIT COMBAT")
    caller.ndb._menutree.close_menu()
    caller.db.target.ndb._menutree.close_menu()

    text = ""
    options = ()
    return text, options
