from fastapi import FastAPI

from routes.upload_routes import router as upload_router
from routes.analysis_routes import router as analysis_router
from routes.chat_routes import router as chat_router
from routes.report_routes import router as report_router
from routes.document_routes import router as document_router

app = FastAPI(
title="AI Compliance & Risk Intelligence Platform",
description="AI-powered system to detect compliance risks in enterprise documents",
version="1.0.0"
)

app.include_router(upload_router)
app.include_router(analysis_router)
app.include_router(chat_router)
app.include_router(report_router)
app.include_router(document_router)


@app.get("/")
def root():
    return {"message": "AI Compliance Platform Running", "status": "OK"}