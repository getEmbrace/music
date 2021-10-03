import myHttp
import root

path = root.path


def Resources(requestInfo):
    url = requestInfo['url']
    content_type = 'text/html'
    filetype = url.split('.')[-1]
    filetypeList = ['jpg', 'png', 'ico', 'jpge', 'ttf', 'woff', 'gif']
    try:
        if(filetype in filetypeList):
            with open(r"{}".format(path+url), 'rb') as f:
                data = f.read()
            content_type = 'image/{}'.format(filetype)
        else:
            with open(r"{}".format(path+url), 'r', encoding='utf-8') as f:
                data = f.read()
            content_type = 'text/{}'.format(filetype)

        response = myHttp.response({
            'headers': {
                'Content-Type': content_type
            },
            'body': data
        })
        return response
    except:
        return myHttp.response({'status': 404})
