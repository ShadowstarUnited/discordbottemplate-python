import tokens
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection
db = AsyncIOMotorClient(tokens.mongo)
BotDB = db["botdb"] # These can be named anything, but if you DO rename BotDB, make sure it's referenced everywhere the database is called.
BlacklistCol: Collection = BotDB["blacklist"]
PrefixCol: Collection = BotDB["prefixes"]
