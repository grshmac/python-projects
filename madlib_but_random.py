from collect_madlibs import main, killin_it, brahh, zoo
import random

if __name__ == '__main__' :
    # m = (main,killin_it,brahh,zoo)
    # print(m)

    run = random.choice([killin_it,main,zoo,brahh])  #chooses random madlib code files from above import
    run.madlib()
