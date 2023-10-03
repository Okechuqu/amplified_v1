from website.models import WebTemplate
from django.conf import settings
from contextlib import contextmanager


def contextManager():
    contextList = []
    app = WebTemplate.objects.all()
    if app:
    # There are records in the query result
        app = app[0].name
    else:
        # No records found, handle this case as needed
        app = "default"  # Replace with a default value or appropriate handling
    context = f"webapps.{app}.context_processor.frontendContextProcessor"
    contextList.append(context)
    return(contextList)

@contextmanager
def update_context_processors(context_processors):
  """Updates the context processors setting."""
  old_context_processors:list = settings.TEMPLATES[0]['OPTIONS']['context_processors']
  old_context_processors += context_processors
  # print(old_context_processors)
  settings.TEMPLATES[0]['OPTIONS']['context_processors'] = old_context_processors
  try:
    yield
  finally:
    settings.TEMPLATES[0]['OPTIONS']['context_processors'] = old_context_processors

def update_templates():
  with update_context_processors(contextManager()):
    pass


