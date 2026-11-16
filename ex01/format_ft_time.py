import time

timestamp = time.time()
print(
    f"Seconds since January 1, 1970: {timestamp:,.4f} "
    f"or {timestamp:.2e} in scientific notation"
)
print(time.strftime("%b %d %Y", time.localtime(timestamp)))
