import os


def templateManager(modelname=None, template='templates', app_directory='frontend'):
    '''
    modelname: this is represents a model instance with data.
    templates: this is the frontend template directory.
    app_directory: this defines the root or app where templates serves the html.
    '''
    try:
        DEFAULT_TEMPLATE = 'test'
        web = modelname if modelname != None else exit(
            'Web manager does not exist.')
        if web.exists():
            web = web[0]

            TEMPLATE = str(web.template)
            PATH = os.path.abspath(f"{app_directory}/{template}/{TEMPLATE}")
            # check if path does exist
            if os.path.exists(PATH):
                return TEMPLATE, str(web.page_title), str(web.seo_description), f"{web.favicon.url}"
            else:
                # else if it fails, fallback to default
                return DEFAULT_TEMPLATE
        else:
            # else if it fails, fallback to default
            return DEFAULT_TEMPLATE

    except Exception as e:
        print(e)
        return DEFAULT_TEMPLATE
