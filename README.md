# Brädfodrings beräknare

Ett enkelt verktyg för att beräkna och optimera åtgång av brädor vid brädfodring.

## Kom igång

Installera beroenden via pip och kör skriptet med Python 3. Exempel:

```bash
pip install -r requirements.txt
python main.py
```

### Kodstandard och automatiska hooks

För utveckling rekommenderas att installera dev-beroenden och aktivera
`pre-commit` så att koden automatiskt lintas med **ruff** innan varje commit.

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Efter installationen körs lintern automatiskt. Du kan även starta den manuellt:

```bash
pre-commit run --all-files
./scripts/run_ruff.sh
```
