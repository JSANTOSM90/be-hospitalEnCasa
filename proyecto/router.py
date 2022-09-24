from aplicacion.viewsets import pacienteViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register('entidad',pacienteViewset)

