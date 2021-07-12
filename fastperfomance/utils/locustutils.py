import os


class LocustFile(object):
    def __init__(self):
        self.name = 'locustfile'

    def prepare_locust_tests(self, qjson):
        self.url = qjson['url']
        self.headers = qjson['body']['request']['headers']
        self.body = qjson['body']['request']['data']
        self.method = qjson['method']
        self.users = qjson['users']
        self.rate = qjson['rate']
        self.missiontime = qjson['missiontime']
        self.assertstr = qjson['assertstr']
        return self


def makefile(datatext):
    filename = '/Users/chenxiaolong/Desktop/Project/Djangostudy/fastperfomance/templates/locustfile.py'
    locustfile1 = '/Users/chenxiaolong/Desktop/Project/Djangostudy/fastperfomance/templates/locustfile1.py'
    try:
        os.remove(locustfile1)
    except IOError:
        print('文件不存在')

    finally:
        fp = open(filename, 'r')
        content = fp.read()
        fp.close()
        print(type(content))
        print(content)
        c2 = content.replace('self.method', '"%s"' % datatext.method,1)
        c2 = c2.replace('self.url', '"%s"' % datatext.url,1)
        c2 = c2.replace('self.headers', '"%s"' % str(datatext.headers),1)
        c2 = c2.replace('self.data', '"%s"' % str(datatext.body),1)
        c2 = c2.replace('self.assertstr', '"%s"' % datatext.assertstr,1)
        print(datatext.method, datatext.url, '"%s"' % str(datatext.headers), str(datatext.body), datatext.assertstr)
        f = open(locustfile1, 'w+')
        f.write(c2)
        read = f.readline()
        print(read)
        f.close()
    return locustfile1


def run(path, parm):
    os.system('locust -f %s --headless -u %s -r %s --run-time %s ' % (path, parm.users, parm.rate, parm.missiontime))
