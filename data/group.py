import random
import string
import re
from model.group import Group


def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + re.sub("'", " ", string.punctuation) + " "*10
     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])