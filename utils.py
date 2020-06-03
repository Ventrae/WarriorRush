def CheckIfCollision(character, obstacle):
	hitbox1 = (
		(character.position[0], character.position[0]+character.size[0]), # x1, x2
		(character.position[1], character.position[1]+character.size[1]) # y1, y2
	)
	hitbox2 = (
		(obstacle.position[0], obstacle.position[0]+obstacle.size[0]), # x1, x2
		(obstacle.position[1], obstacle.position[1]+obstacle.size[1]) # y1, y2
	)
	if character.isInMidair == False:
		if hitbox1[0][1] < hitbox2[0][0]:
			print("No match")
			return False
		else:
			print("Horizontal match")
			return True # horizontal match
	else:
		print("In midair")
		return False