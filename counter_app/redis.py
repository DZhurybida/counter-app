from typing import AsyncIterator

import aioredis


async def init_redis_pool(
    redis_dsn: str, max_connections: int
) -> AsyncIterator[aioredis.Redis]:
    pool = aioredis.ConnectionPool.from_url(redis_dsn, max_connections=max_connections)
    redis = aioredis.Redis(connection_pool=pool)
    yield redis
    await redis.close()
