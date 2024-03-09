import asyncio , uvicorn
from server import app
from server.config import PORT
from server.tables import init_database

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def init_db():
    init_database()


async def main():
    uvicorn.run(
        "server.__main__:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )

loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(main())
