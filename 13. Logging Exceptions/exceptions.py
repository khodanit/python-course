import logging as log
import traceback as tb

FORMAT = "%(asctime)s:%(levelname)10s:%(message)s"
log.basicConfig(format=FORMAT, filename="logger.log", level=log.DEBUG)
log.debug("debug message")
log.warning("warning message")

try:
    1 / 0
except ZeroDivisionError:
    print("can't divide by zero", end="\n\n")

try:
    l = []
    l[0]
except IndexError:
    print("index not defined", end="\n\n")

try:
    print(a)

except NameError:
    print("name not defined", end="\n\n")

try:
    my_error = [fvewfsr]
except Exception as e:
    print("an error happened")
    print("err: ", e, end="\n\n")
else:
    print("no exception occurred")
finally:
    print("we do this no matter what")

print("here the program continues")
