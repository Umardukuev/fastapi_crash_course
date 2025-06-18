from database import new_session, TaskTable
from schemas import STaskAdd, STaskRead
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STaskRead]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskRead.model_validate(task_model) for task_model in task_models]
            return task_schemas