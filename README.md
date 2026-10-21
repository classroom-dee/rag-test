### Yeeep
1. Activate your venv if you don't want messy python env
2. Start `./infra.sh`. Warning: the script is not idempotent.
3. `pip install -r requirements.txt --no-cache-dir`
4. `uvicorn main:app --reload`
5. Access the endpoint via `http://localhost:8000/api/chat`