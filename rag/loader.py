from src.log_parser import LogParser
def load_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()