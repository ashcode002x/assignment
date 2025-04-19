import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from .import logReader as lr


class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # await self.send("good")
        self.task_list=asyncio.current_task(await self.sendLog())
    
    async def disconnect(self, code):
        self.task_list.cancel()
        # self.first.cancel()
        return super().disconnect(code)


    async def sendLog(self):
        # print(lr.sendLog)
        async for log in lr.sendLog():
            # print(log)
            await self.send(text_data=json.dumps({"log":log}))