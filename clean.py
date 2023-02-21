import json
import glob
import shutil

from datetime import datetime, timedelta

dirs = glob.glob('./fof/*/')

dirs = [x[2:-1] for x in dirs]
dirs = sorted(list(map(lambda x : int(x.split('/')[1]), dirs)), reverse=True)

start = 1676974832
end = 1676974145

for ts in dirs:
    if ts > start:
        continue

    if ts < end:
        continue

    dt = datetime.utcfromtimestamp(ts)

    base_dir = f'/Users/mkgk/Workspace/td/fof/{ts}'

    print(f'remove {base_dir}({dt})')
    shutil.rmtree(base_dir)
