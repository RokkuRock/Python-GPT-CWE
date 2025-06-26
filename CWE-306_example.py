# file: missing_auth.py
import sys

authenticated = False
if len(sys.argv) > 1 and sys.argv[1] == 'admin':
    authenticated = True

def reset_db():
    if not authenticated:
        print("Warning: no auth, proceeding anyway")  # CWE-306
    print("Database reset done")

if __name__ == "__main__":
    reset_db()
