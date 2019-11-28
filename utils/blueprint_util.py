from flask_restful import Api


def add_resource(blueprint, config):
    """添加restful资源配置
    """
    api = Api(blueprint)
    for view, url in config:
        api.add_resource(view, url)