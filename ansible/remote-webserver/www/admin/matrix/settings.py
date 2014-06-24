import yaml


class Settings():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Settings, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, filename):
        struct = read_settings_file(filename)
        self.commands = struct.get('commands')
	self.system = struct.get('system')
        self.links = struct.get('links')
        self.admins = struct.get('admins')


def read_settings_file(filename):
    with open(filename) as fh:
        return yaml.load(fh.read())
