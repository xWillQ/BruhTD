def logicLoop(mobs, towers, turns):
    for i in range(0, len(mobs)):
        for turn in turns:
            if (turn.isInside(mobs[i].posX, mobs[i].posY)):
                mobs[i].turn(turn)
            else:
                mobs[i].move()

            if ((i > 0) and (mobs[i - 1].distance > mobs[i].distance)):
                t = mobs[i - 1]
                mobs[i - 1] = mobs[i]
                mobs[i] = t

        for tower in towers:
            if (tower.isInside(mobs[i].posX, mobs[i].posY) and tower.cooldown == 0):
                tower.attack(mobs[i])
                if (mobs[i].hp <= 0):
                    mobs.remove(mobs[i])
