from fastapi import FastAPI
from server.routes import __all__ as allRoutes



app = FastAPI()

for router in allRoutes :
    app.include_router(router)


