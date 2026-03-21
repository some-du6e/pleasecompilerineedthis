# hi
chance=0.5
no = "components/topsecret/talking-ben-no.mp3"
yes = "components/topsecret/talking-benn-yes.mp3"
laugh = "components/topsecret/talking-benny-laugh.mp3"

import playsound
import random
import time
def sensitiveFunction(fast=False):
    if random.random() < chance:
        playsound.playsound(yes, block=not fast)
        if fast: time.sleep(1.15)
        return True
    else:
        playsound.playsound(no, block=not fast)
        if fast: time.sleep(1.15)
        return False