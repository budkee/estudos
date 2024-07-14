# data/router.py
class DataAppRouter:
    """
    A router to control database operations for data app.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read data from 'db_data'.
        """
        if model._meta.app_label == 'data':
            return 'db_data'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write data to 'db_data'.
        """
        if model._meta.app_label == 'data':
            return 'db_data'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        É implementada para permitir relacionamentos entre modelos de diferentes aplicativos se necessário.
        """
        if obj1._meta.app_label == 'data' or obj2._meta.app_label == 'data':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the data app only appears in the 'db_data' database.
        """
        if app_label == 'data':
            return db == 'db_data'
        return None
