from fastapi import APIRouter
from aplicacao.routes.v1 import equipmento_route, departamento_route, insumo_route
router = APIRouter(prefix='/v1')

router.include_router(equipmento_route.route)
router.include_router(departamento_route.route)
router.include_router(insumo_route.route)
