import os

path = os.path.realpath(os.path.dirname(__file__))[:-6] + 'terraform/schemas/'

print(path)