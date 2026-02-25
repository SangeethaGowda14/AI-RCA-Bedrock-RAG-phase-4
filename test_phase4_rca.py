from rca.rca_engine import RCAEngine

engine = RCAEngine()

log_query = "Authentication failed repeatedly for multiple users"

result = engine.analyze(log_query)

print("\n--- AI RCA OUTPUT ---\n")
print(result)