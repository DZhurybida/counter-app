import logging
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)


from counter_app import health, counter, errors
from counter_app.containers import Container
from counter_app.logging import logging_setup


def get_app():
    app = FastAPI(title="Counter App")
    app.include_router(health.router)
    app.include_router(counter.router, prefix="/counter")
    app.include_router(errors.router, prefix="/errors")

    container = Container()
    container.config.redis_dsn.from_env(
        "REDIS_DNS", "redis://:password@localhost:6379/0"
    )
    container.config.redis_max_connections.from_env("REDIS_MAX_CONNECTIONS", 10)
    container.config.log_level.from_env("LOG_LEVEL", logging.INFO)
    container.config.log_json.from_env("LOG_JSON", False)
    container.wire(modules=[counter, health])

    @app.on_event("startup")
    async def startup_event():
        await container.init_resources()

    @app.on_event("shutdown")
    async def shutdown_event():
        await container.shutdown_resources()

    Instrumentator(should_respect_env_var=True).instrument(app).expose(app)


    provider = TracerProvider()
    # processor = BatchSpanProcessor(ConsoleSpanExporter())
    # provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    FastAPIInstrumentor().instrument_app(app)

    logging_setup(container.config)

    return app
