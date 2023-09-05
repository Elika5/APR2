import tomli

with open("konfigurace.toml", mode="rb") as fp:
    config = tomli.load(fp)

print(config["znamka1_min"])