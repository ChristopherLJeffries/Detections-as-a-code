import yaml
import sys
import glob

errors = 0

for file in glob.glob("detections/**/*.yaml", recursive=True):
    try:
        yaml.safe_load(open(file))
    except Exception as e:
        print(f"❌ Error in {file}: {e}")
        errors += 1

if errors:
    sys.exit(1)

print("✅ All detections valid!")
