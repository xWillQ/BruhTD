def logicLoop(mobs, turns):
    for i in range(0, len(mobs)):
        turned = False
        for turn in turns:
            if (turn.isInside(mobs[i].x, mobs[i].y)):
                mobs[i].turn(turn)
                turned = True
        if (not turned):
            mobs[i].move()

        if ((i > 0) and (mobs[i - 1].distance > mobs[i].distance)):
            t = mobs[i - 1]
            mobs[i - 1] = mobs[i]
            mobs[i] = t
