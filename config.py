import os


class Config:
    def __init__(self, db_user: str, db_password: str, db_server: str, db_port: str, db_name: str, server_address: str,
                 server_port: int):
        self.db_user = db_user
        self.db_password = db_password
        self.db_server = db_server
        self.db_port = db_port
        self.db_name = db_name
        self.server_address = server_address
        self.server_port = server_port


def load_config_from_environment() -> Config:
    db_user = os.getenv('DATABASE_USERNAME', 'blog_backend_user')
    db_password = os.getenv('DATABASE_PASSWORD', 'blog123')
    db_server = os.getenv('DATABASE_SERVER', 'localhost')
    db_port = os.getenv('DATABASE_PORT', '3306')
    db_name = os.getenv('DATABASE_NAME', 'blog_backend_python')
    server_address = os.getenv('SERVER_ADDRESS', 'localhost')
    server_port = int(os.getenv('SERVER_PORT', '8080'))

    return Config(db_user, db_password, db_server, db_port, db_name, server_address, server_port)
