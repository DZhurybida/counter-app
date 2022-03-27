from fastapi import FastAPI

from counter_app import health
from counter_app import counter
from counter_app.containers import Container


def get_app():
    app = FastAPI(title="Counter App")
    app.include_router(health.router)
    app.include_router(counter.router, prefix="/counter")

    container = Container()
    container.config.redis_dsn.from_env(
        "REDIS_DNS", "redis://:password@localhost:6379/0"
    )
    container.config.redis_max_connections.from_env("REDIS_MAX_CONNECTIONS", 10)
    container.wire(modules=[counter])

    @app.on_event("startup")
    async def startup_event():
        container.init_resources()

    @app.on_event("shutdown")
    def shutdown_event():
        container.shutdown_resources()

    return app
