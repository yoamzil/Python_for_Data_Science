import datetime as dt
import time as t

time = t.time()
date = dt.datetime.now(tz=dt.timezone.utc).strftime("%b %d %Y")

print (f"Seconds since January 1, 1970: {time:,.4f} or {time:.2e} in scientific notation")
print (date)