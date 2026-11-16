"""PaceMochi Agent 后端入口。

当前是一个空的 FastAPI 应用——没有任何路由，所有 API 从这里开始手写。

启动：
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="PaceMochi Agent API")
