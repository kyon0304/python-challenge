# it's in the zip
#! /usr/bin/env python

from http.client import HTTPConnection
import base64

if __name__ == '__main__':
    url = 'www.pythonchallenge.com'
    suffix = '/pc/hex/unreal.jpg'
    method = 'GET'
    unpw = base64.b64encode(b'butter:fly').decode('utf-8')
    headers = {'Authorization': 'Basic %s' % unpw}
    conn = HTTPConnection(url)
    # rg = (30203, 30236)
    # rg = (30237, 30294)
    # rg = (30295, 30312)
    # rg = (30313, 30346)
#=================get user name is invader======================================
    # for n in range(30203, 30314):
    #     rg = (n, n + 40)
    #     headers['Range'] = 'bytes=%d-%d' % rg
    #     conn.request(method, suffix, headers=headers)
    #     resp = conn.getresponse()
    #     # print(resp.status)
    #     if resp.status == 206:
    #         print(resp.getheader('content-range'))
    #         content = resp.read().decode('utf-8')
    #         print(content)

#========================find pw================================================
    # for n in range(2123456743, 2123456745):
    #     headers['Range'] = 'bytes=%d-%d' % (n, n + 1)
    #     conn.request(method, suffix, headers=headers)
    #     resp = conn.getresponse()
    #     if resp.status == 206:
    #         # print(resp.getheader('content-range'))
    #         print(resp.getheaders())
    #         content = resp.read().decode('utf-8')
    #         print(content)
    #         print(content[::-1])

#=================the password is your new nickname in reverse==================
    for n in range(1152983631, 1152983632):
    # for n in range(2123456744, 2123456745):
        # print(n)
        headers['Range'] = 'bytes=%d-%d' % (n, n + 1)
        conn.request(method, suffix, headers=headers)
        resp = conn.getresponse()
        # print(resp.status)
        if resp.status == 206:
            print(resp.getheader('content-range'))
            content = resp.read()
            with open('unreal.zip', 'wb') as f:
                f.write(content)
        else:
            resp.read()
