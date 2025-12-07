# index-search-python

간단한 인덱스 검색 PoC 프로젝트입니다.
목표: 임베딩(벡터) 기반 검색 + 4단계 계층(classification) 기반 색인 선택을 결합한 검색 파이프라인을 설계/테스트합니다.

프로젝트 구조 (루트 폴더 기준)
- .venv/                     # 가상환경 (uv sync로 생성)
- src/
  - __init__.py              # 패키지 초기화 (src.config.init_paths 호출)
  - config.py                # init_paths(), ProjectPaths 정의
  - main.py                  # 예제 진입점
  - embeddings/
    - __init__.py
    - embedder.py            # 임베딩 생성/캐시 로직
  - db/
    - __init__.py
    - sqlite_manager.py      # SQLiteManager 구현 (tests와 연동)
  - elastic/
    - __init__.py
    - elastic_client.py      # Elasticsearch 연동 및 벡터 검색
  - llm/
    - __init__.py
    - langchain_client.py    # LangChain OpenaiChat 래퍼
  - classifier/
    - __init__.py
    - classifier.py         # 4단계 계층 분류 로직 (LLM 연동)
  - models/
    - __init__.py
    - index_models.py       # Pydantic/dataclass 정의
  - utils/
    - helpers.py
- scripts/
  - uv.py                    # uv sync / clean 스크립트
- uv.cmd                     # Windows cmd 래퍼 (uv sync)
- uv.ps1                     # PowerShell 래퍼 (.\uv.ps1 sync)
- requirements.txt
- tests/
  - test_sqlite.py
  - test_index_selection_ko.py
- data/                      # 데이터/샘플 파일
- embeddings/                # 임베딩 캐시 디렉터리
- logs/                      # 로그 파일
- models/                    # 학습/저장 모델 파일
- .gitignore

핵심 파일 설명
- src/config.py
  - init_paths(root=None, create_dirs=True) 반환형: ProjectPaths
  - 프로젝트 루트/디렉터리 경로를 계산하고(필요시 생성) 환경변수에 등록
- src/__init__.py
  - import 시 init_paths 호출, src.paths 를 통해 경로에 접근 가능
- scripts/uv.py + uv.cmd / uv.ps1
  - "uv sync"로 .venv 생성 및 requirements 설치
  - "uv clean"으로 .venv 삭제

빠른 시작 (Windows)
1) 프로젝트 루트로 이동
   cd C:\Users\R14634\Desktop\code\index_poc\index-search-python

2) 가상환경 생성 및 의존성 설치
   PowerShell:
     .\uv sync
   cmd.exe:
     uv sync

3) 가상환경 활성화
   PowerShell:
     .\.venv\Scripts\Activate.ps1
   cmd.exe:
     .\.venv\Scripts\activate.bat

4) 테스트 실행
   pytest -q

5) 예제 실행
   python -m src.main

테스트 연동 안내
- tests/test_sqlite.py 에 맞춰 src/db/sqlite_manager.py의 API를 구현하세요:
  - create_schema(), insert_record(), get_record(), update_record(), delete_record(), get_tables()
- tests/test_index_selection_ko.py 는 한국어 질의 리스트를 포함합니다. 초기 상태는 문자열 유효성 검사이며, 향후 분류기/검색기와 연동해 기대 결과를 검증하도록 확장하세요.

환경변수 / 외부 서비스
- OpenAI: OPENAI_API_KEY 환경변수 설정 필요
- Elasticsearch: ELASTICSEARCH_URL 등 연결 정보 환경변수로 관리

참고
- 파일/폴더 이름에 절대 경로가 들어가거나 불필요한 주석이 섞여 있지 않도록 위 구조로 정리했습니다.
- 원하면 실제 파일 생성/수정(예: sqlite_manager 구현, embedder 스켈레톤 추가)을 바로 만들어 드리겠습니다.