from fastapi import APIRouter, Request, Response
import uuid
from pydantic import ValidationError


class CRUDRoutes:

    def __init__(self, database, ObjectSchema=None, ObjectUpdateSchema=None, route_code='CRUD'):
        self.router = APIRouter()
        self.database = database
        self.route_code = route_code
        self.ObjectSchema = ObjectSchema
        self.ObjectUpdateSchema = ObjectUpdateSchema

        self._create_routes()

    def _create_routes(self):
        # adding the read routes
        if 'R' in self.route_code:

            @self.router.get('/')
            async def read_all():
                return self.database.read_all()

            @self.router.get('/{id}')
            async def read_one(id: str, res: Response):
                item = None
                try:
                    item = self.database.read_one(id)
                except KeyError:
                    res.status_code = 404
                    return {'message': 'Item not found'}

                return item

        if 'C' in self.route_code:
            # create route
            @self.router.post('/', status_code=201)
            async def create(req: Request, res: Response):
                id = str(uuid.uuid4()).replace('-', '')
                item = await req.json()
                try:
                    self.ObjectSchema(**item)
                except ValidationError as e:
                    res.status_code = 400
                    return e.errors()

                self.database.create(id, item)
                return {'createdId': id}

        if 'U' in self.route_code:
            @self.router.put('/{id}')
            async def update(id: str, req: Request):
                delta = await req.json()
                try:
                    self.ObjectUpdateSchema(**delta)
                except ValidationError as e:
                    return e.errors()

                updated = self.database.update(id, delta)
                return updated

        if 'D' in self.route_code:
            @self.router.delete('/{id}')
            def delete(id: str, res: Response):
                if not self.database.exists(id):
                    res.status_code = 404
                    return {'message': 'Not Found!'}
                removed_id = self.database.delete(id)
                return removed_id

    def get_router(self):
        return self.router
