class FlaskConfigTemplate(object):

    DEBUG = True
    TESTING = True


class DevelopmentConfig(FlaskConfigTemplate):

    DEBUG = True
    TESTING = True


class ProductionConfig(FlaskConfigTemplate):
    pass
