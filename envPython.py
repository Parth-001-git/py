import os

os.environ["VarHello"] = "87654"

env = os.getenv("VarHello")
print("\n",env,type(env),"\n")
