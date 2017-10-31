from configparser import ConfigParser
config = ConfigParser()

config.read("config.cnf")
print(config.get("Section1","first_variable"))
print(config.get("Section2","second_variable"))