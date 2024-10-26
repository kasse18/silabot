from aiogram import Router


def setup_routers() -> Router:
    from . import user, common

    router = Router()
    router.include_router(user.router)
    router.include_router(common.router)

    return router
