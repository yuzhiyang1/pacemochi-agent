"""PaceMochi Agent 后端入口。

当前是一个空的 FastAPI 应用——没有任何路由，所有 API 从这里开始手写。

启动：
    uvicorn app.main:app --reload
"""
import uuid
from datetime import datetime
from typing import Dict, Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PaceMochi Agent API")



# =============================================================================
# 聊天会话管理器
# =============================================================================

class SessionConfig(BaseModel):
    """创建会话时传入的配置。"""

    provider: Literal["gemini", "openai", "anthropic"] = "gemini"
    baseline: Literal["pha", "parallel", "phia"] = "pha"
    persona_id: str = "sample"


class SessionResponse(BaseModel):
    """创建会话成功后的响应。"""

    session_id: str
    config: SessionConfig
    created_at: str
    status: str = "ready"


class ChatSession:
    """保存在服务端内存里的会话。"""

    def __init__(self, session_id: str, config: SessionConfig):
        self.session_id = session_id
        self.config = config
        self.created_at = datetime.now()
        # 每个会话有自己的消息列表。
        self.messages = []

@app.get("/")
async def root():
    """带有 API 信息的端点."""
    return {
        "name": "PaceMochi Agent API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running",
    }


sessions: Dict[str, "ChatSession"] = {}

# 健康检查
@app.get("/health")
async def health_check():
    """ 健康检测 """
    return {"status": "health", "timestamp": datetime.now().isoformat()}

# 列出所有活动的会话
@app.get("/sessions")
async def list_sessions():
    """List all active sessions."""
    return {
        "sessions": [
            {
                "session_id": sid,
                "baseline": s.config.baseline,
                "persona": s.config.persona_id,
                "message_count": len(s.messages),
                "created_at": s.created_at.isoformat(),
            }
            for sid, s in sessions.items()
        ],
        "count": len(sessions),
    }

# 创建会话
# 创建会话
@app.post("/sessions", response_model=SessionResponse)
async def create_session(config: SessionConfig):
    """创建一条空会话。"""
    session_id = str(uuid.uuid4())[:8]
    session = ChatSession(session_id, config)

    # 保存会话，供 GET /sessions 查询。
    sessions[session_id] = session

    return SessionResponse(
        session_id=session_id,
        config=config,
        created_at=session.created_at.isoformat(),
        status="ready",
    )

