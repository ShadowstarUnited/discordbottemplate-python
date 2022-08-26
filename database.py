import tokens
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import Collection
db = AsyncIOMotorClient(tokens.mongo)
BotDB = db["botdb"] # These can be named anything, but if you DO rename BotDB, make sure it's referenced everywhere the database is called.
BlacklistCol: Collection = BotDB["blacklist"]
PrefixCol: Collection = BotDB["prefixes"]
UserCol: Collection = DrunkDB["users"]
# This is your DataBase. Whenever you'd like to create a new type of collection, it goes in here. PrefixCol = prefix collection. This is where the database stores custom prefixes. BlacklistCol = blacklist collection, which is where the database stores blacklisted servers or users.
