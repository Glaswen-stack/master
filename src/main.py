


import uvicorn
import asyncio


async def main() -> None:
    uvicorn.run('application:get_app', host='localhost', port=8000, reload=True, factory=True)

if name == '__main__':
    asyncio.run(main())