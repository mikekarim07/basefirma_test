from deta import Deta

DETA_KEY = "b0n5nt3hskp_dDCyndpUKxP7vn3e6vxuvnNB2LJkUsex"

deta = Deta(DETA_KEY)

db = deta.Base("kpis")
