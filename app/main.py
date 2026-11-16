"""PaceMochi Agent 后端入口。

当前是一个空的 FastAPI 应用——没有任何路由，所有 API 从这里开始手写。

启动：
    uvicorn app.main:app --reload
"""
from datetime import datetime
from fastapi import FastAPI, HTTPException, BackgroundTasks

app = FastAPI(title="PaceMochi Agent API")

@app.get("/")
async def root():
    """带有 API 信息的端点."""
    return {
        "name": "PaceMochi Agent API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running",
    }

# 健康检查
@app.get("/health")
async def health_check():
    """ 健康检测 """
    return {"status": "health", "timestamp": datetime.now().isoformat()}
