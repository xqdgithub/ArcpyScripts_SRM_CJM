
import multiprocessing as mp
import datetime
import ProjectTifs
import ClipTifs

def Run(pool):
    # ProjectTifs.Run(pool)
    ClipTifs.Run(pool)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    cpu= mp.cpu_count()
    usecore=cpu
    pool=mp.Pool(1)
    Run(pool)
    end_time = datetime.datetime.now()
    use_time = (end_time - start_time).total_seconds()
    print("Finished: " + "{:.2f}".format(use_time) + " s")

