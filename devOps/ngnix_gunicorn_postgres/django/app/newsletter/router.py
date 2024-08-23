class NewsletterAppRouter:
    """
    A router to control database operations for newsletter app.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read data from 'db_newsletter'.
        """
        if model._meta.app_label == 'newsletter':
            return 'db_newsletter'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write data to 'db_newsletter'.
        """
        if model._meta.app_label == 'newsletter':
            return 'db_newsletter'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        É implementada para permitir relacionamentos entre modelos de diferentes aplicativos se necessário.
        """
        if obj1._meta.app_label == 'newsletter' or obj2._meta.app_label == 'newsletter':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the newsletter app only appears in the 'db_newsletter' database.
        """
        if app_label == 'newsletter':
            return db == 'db_newsletter'
        return None
