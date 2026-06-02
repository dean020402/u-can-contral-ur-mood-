from fastapi import FastAPI
from app.routers import routes

app = FastAPI(
    title="감정 상태에 따른 분석을 통한 활동코스 추천"
    description="어플 만드는거 연습할겸 1인 개발 프로젝트"
    version="0.1"  
)

app.include_router(routes.router)