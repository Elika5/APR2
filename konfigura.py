import tomli

def nacti_konfiguraci():
    with open("konfigurace_ucitel.toml", mode="rb") as fp:
        config = tomli.load(fp)
    return config
