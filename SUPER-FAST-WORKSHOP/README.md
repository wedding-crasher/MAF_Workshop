# 🚀 MAF Super Fast Workshop

Microsoft Agent Framework 핸즈온 워크샵 노트북입니다.

## 📚 워크샵 노트북

| 노트북 | 내용 |
|--------|------|
| `MAF-Travel-Planner-Workshop.ipynb` | Travel Planner Agent 구축 (Agent, Tools, Memory, Workflow) |
| `MAF-Orchestrations-Workshop.ipynb` | 멀티 에이전트 오케스트레이션 (Concurrent, Group Chat) |

---

## ⚡ 환경 설정 (3분)

### 사전 준비
- ✅ Python 3.12 설치 완료
- ✅ Azure OpenAI 리소스 준비 (Endpoint, Deployment Name)
- ✅ 인증 방법 택1:
  - **(권장)** Azure CLI 설치 후 `az login` 실행
  - 또는 Azure OpenAI API Key 준비

### 1️⃣ 가상환경 생성 & 활성화

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate
```

**Mac / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> ⚠️ **Python 명령어가 안 될 때?**
> 
> 환경에 따라 `python`, `python3`, `python3.12` 중 하나가 동작합니다.
> ```bash
> # 먼저 버전 확인 (3.12.x 인지 체크)
> python --version      # 또는
> python3 --version     # 또는  
> python3.12 --version
> ```
> 동작하는 명령어로 가상환경을 생성하세요.

### 2️⃣ JupyterLab 설치 & 실행

```bash
pip install jupyterlab
python -m jupyter lab
```

### 3️⃣ 노트북 열고 시작!

노트북 내 첫 번째 셀에서 `agent-framework` 패키지가 자동 설치됩니다.

---

## 🔗 참고 링크

- [Microsoft Agent Framework 문서](https://learn.microsoft.com/en-us/agent-framework/)
- [Azure OpenAI 설정 가이드](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
