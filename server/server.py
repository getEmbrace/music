
from socket import *
import threading
import datetime
import ssl

import myHttp
from resources import Resources
import db1 as DB
import root

useDb = DB.useDb

class Server:
    def __init__(self, IP, Port, routers):
        self.IP = IP
        self.Port = Port
        self.routers = routers
        self.context = None
        
    def HeaderLength(self, request):
        itemList = request.split('\r\n\r\n', 1)
        if(len(itemList) == 1):
            headers, bodys = itemList[0], ""
            return 0
        else:
            headers, bodys = itemList[0], itemList[1]
            return len(headers) + 4
    
    def getReouestInfo(self, conn):
        g_length = 0
        userHttp = myHttp.requestInfo
        userHttp_from = myHttp.request_form
        data_b = conn.recv(1024)
        requestInfo = userHttp(str(data_b.split(b'\r\n\r\n')[0], encoding='utf-8'))
        headerLength = self.HeaderLength(data_b.decode('utf-8', 'ignore'))
        c_length = requestInfo['field'].get('Content-Length')
        conent_type = requestInfo['field'].get('Content-Type')
        g_length = len(data_b)
        if(c_length):
            c_length = int(c_length) + headerLength
            while(True):
                if(g_length >= c_length):
                    break
                data_b = data_b + conn.recv(4096)
                g_length = len(data_b)
                if(g_length >= c_length): 
                    break
        if(conent_type and conent_type.split(';')[0] == "multipart/form-data"):
            requestInfo = userHttp_from(data_b)
        else:  
            requestInfo = userHttp(str(data_b, encoding='utf-8'))

        return requestInfo

    def Threadfun(self, conn, addr):
        requestInfo = self.getReouestInfo(conn)
        url = requestInfo['url']
        method = requestInfo['method']
        if(url == ''):
            conn.close()
            return

        print("\nTime: {}\n\t连接来自{},url:{}, method:{}".format(datetime.datetime.today(), addr, url, method))
        if(method == "OPTIONS"):
            response = myHttp.response({})
        else:
            response = self.routers.get(url, Resources)(requestInfo)
    
        conn.send(response)
        conn.close()

    def setSSL(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        self.context = context
        
    def run(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.IP, self.Port))
        sock.listen(100)
        print("开启服务: ",self.IP,':',self.Port)
        while True:
            conn, addr = sock.accept()
            if(self.context != None):
                connstream = self.context.wrap_socket(conn, server_side=True)
            else:
                connstream = conn
            t = threading.Thread(target = self.Threadfun, args = (connstream, addr, ))
            t.setDaemon(True)
            t.start()
            

if __name__ == "__main__":
    server = Server(root.IP,root.PORT, root.routers)
    server.run()
