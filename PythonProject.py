import requests
r = requests.get('https://www.google.com/')

if 'server' in r.headers:
    print(r.headers['server'])
else:
    print('Information not available')

if 'date' in r.headers:
    print(r.headers['date'])
else:
    print('Information not available')

if 'x-country-code' in r.headers:
    print(r.headers['x-country-code'])
else:
    print('Information not available')

if 'connection' in r.headers:
    print(r.headers['connection'])
else:
    print('Information not available')

if 'content-length' in r.headers:
    print(r.headers['content-length'])
else:
    print('Information not available')

# print(r.text)
# with open('test.html','wb') as f:
#     f.write(r.content)
#     f.close()
# print(r.content)
# print(type(r.headers))


# server = open('ServerList.txt','r')
#
# for line in server.readlines():
#     line = line.strip('\n')
#     req = requests.get(line)
#     print(line, 'results:')
#
#     try:
#         content_security = req.headers['Content-Security-Policy']
#         print('Content-Security-Policy is set')
#     except KeyError:
#         print('Content-Security-Policy not available')
#
#     try:
#         x_content_type = req.headers['X-Content-Type-Options']
#         print('X-Content-Type result:', x_content_type)
#     except KeyError:
#         print('X-Content-Type not available')
#
#     try:
#         x_frame_options = req.headers['X-Frame-Options']
#         print('X-Frame-Options result:', x_frame_options)
#     except KeyError:
#         print('X-Frame-Options not available')



