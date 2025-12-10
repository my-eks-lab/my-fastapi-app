import os
import socket
from fastapi import FastAPI

app = FastAPI()

# 루트 경로 - 앱 정보 반환
@app.get("/")
def root():
    return {
        "message": "Hello from K8s",
        "version": "v1.0.0",
        "hostname": socket.gethostname()  # Pod 이름 확인용
    }

# 헬스 체크 - Kubernetes Probe용
@app.get("/health")
def health():
    return {"status": "ok"}

# 직접 실행 시 uvicorn 서버 구동
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)