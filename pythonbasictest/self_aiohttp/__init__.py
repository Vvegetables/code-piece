'''
pip3 install aiohttp
pip3 install cchardet
pip3 install aiodns
'''
import asyncio

from aiohttp import web
import aiohttp


#客户端
class AioClientClass:
    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()
        
    async def main(self):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, 'http://python.org')
            print(html)
    def test(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        
#服务端
class AioServerClass:
    async def handle(self, request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        return web.Response(text=text)
    
    def start(self):
        app = web.Application()
        app.add_routes([web.get('/', self.handle),
                web.get('/{name}', self.handle)])
        web.run_app(app)
    
if __name__ == '__main__':
#     _obj = AioClientClass()
#     _obj.test()
    _obj = AioServerClass()
    _obj.start()
        
        
