# PaceMochi-Agent

PaceMochi-Agent 的后端服务。一个从零开始手搓的 Python Web 项目——当前只有空的应用骨架，所有代码由你自己写。

## 环境

需要 Python 3.12+。

```bash
# 创建虚拟环境（任选其一）
python -m venv .venv                # 标准方式
uv venv -p 3.12 .venv               # 或用 uv

# 激活环境
source .venv/Scripts/activate       # Git Bash（Windows）
# .venv\Scripts\activate            # PowerShell / CMD

# 安装依赖
pip install -r requirements.txt     # 标准方式
uv pip install -r requirements.txt  # 或用 uv
```

## 启动

```bash
uvicorn app.main:app --reload
```

打开 <http://127.0.0.1:8000/docs> 可以看到自动生成的 API 文档页面（现在还没有任何接口）。

## 手搓路线建议

1. 在 `app/main.py` 里写下第一个路由（比如 `GET /` 返回一句 hello）
2. 用 pydantic 定义请求 / 响应模型
3. 把路由拆到 `app/routers/`，用 `APIRouter` 组织
4. 加配置管理（`pydantic-settings` 读环境变量）
5. 接数据库（SQLAlchemy / SQLModel）
6. 需要参考完整实现时，隔壁 `consumer-health-research-cn/personal_health_agent` 是一个 FastAPI + 多 Agent 的成熟范例
