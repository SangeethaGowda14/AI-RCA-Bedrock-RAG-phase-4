def chunk_logs(logs, chunk_size=3):
    chunks = []
    for i in range(0, len(logs), chunk_size):
        chunks.append(" ".join(logs[i:i + chunk_size]))
    return chunks