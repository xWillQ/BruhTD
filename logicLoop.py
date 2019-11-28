def logicLoop(mobs, towers, turns):
    for mob in mobs:
        for turn in turns:
            if (turn.isInside(mob.posX, mob.posY)):
                mob.turn(turn)
            else:
                mob.move()
        for tower in towers:
            if (tower.isInside(mob.posX, mob.posY) and tower.cooldown == 0):
                tower.attack(mob)
                if (mob.hp <= 0):
                    mobs.remove(mob)
