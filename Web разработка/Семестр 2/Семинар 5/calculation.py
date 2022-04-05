from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/hello")
async def hello(req):
    return web.Response(text=f"Hello")

@routes.get('/python')
async def main(req):
    data = await req.json()
    print(data)
    return web.Response(text=f"Accepted!")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8181)
