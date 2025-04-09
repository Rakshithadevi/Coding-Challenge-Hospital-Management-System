# util/DBPropertyUtil.py

def getPropertyString(file_name):
    props = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    props[key.strip()] = value.strip()
    except FileNotFoundError:
        print("Properties file not found.")
        return None

    conn_str = {
        "host": props.get("host"),
        "port": props.get("port"),
        "database": props.get("database"),
        "user": props.get("user"),
        "password": props.get("password")
    }

    return conn_str
