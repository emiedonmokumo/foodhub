from django.apps import AppConfig
import os
import sys


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # Connect to MongoDB when the app is ready so MongoEngine has a default connection.
        mongo_uri = os.getenv('MONGO_URI')
        if not mongo_uri:
            # If the env var isn't set, raise early so deployments fail fast with a clear message.
            sys.stderr.write('ERROR: MONGO_URI is not set. Set the MongoDB connection string in the environment.\n')
            return
        try:
            from mongoengine import connect
            connect(host=mongo_uri)
        except Exception as e:
            # Write to stderr so Render logs show the problem and re-raise to stop startup.
            sys.stderr.write(f'ERROR connecting to MongoDB: {e}\n')
            raise
