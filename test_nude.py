from nudenet import NudeDetector
import sys

detector = NudeDetector()
# Hum check karenge ki default detections mein model kya output deta hai
print("Detector Loaded!")
result = detector.detect(sys.argv[1])
print(f"RAW RESULT: {result}")
