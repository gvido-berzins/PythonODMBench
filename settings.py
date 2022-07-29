import environs

env = environs.Env()
env.read_env()

DATABASE_URL: str = env.str("DATABASE_URL")
