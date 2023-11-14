
#!/usr/bin/env python3

import subprocess
import guesslang

def detect_language(code):
    classifier = guesslang.Classifier()
    result = classifier.predict_one(code)
    return result.language, result.confidence

def run_analysis(language):
    if language == 'Java':
        command = 'sl analyze --app guessjava --java'
    elif language == 'JavaScript':
        command = 'sl analyze --app guessjs --js'
    elif language == 'Python':
        command = 'sl analyze --app guesspy --pythonsrc'
    elif language == 'TypeScript':
        command = 'sl analyze --app guessts --js'
    elif language == 'PHP':
        command = 'sl analyze --app guessphp --php'
    elif language == 'C#':
        command = 'sl analyze --app guessc# --C#'
    elif language in ('C', 'C++'):
        command = 'sl analyze --app guessc --c'
    elif language == 'Kotlin':
        command = 'sl analyze --app guesskot --kotlin'
    elif language == 'Scala':
        command = 'sl analyze --app guesssca --scala'
    else:
        print(f"Unsupported language: {language}")
        return

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def analyze_code(code):
    language, confidence = detect_language(code)
    if confidence > 0.25:
        print(f"Detected language: {language} with confidence: {confidence}")
        run_analysis(language)
    else:
        print("Unable to confidently detect the language.")
# Example usage:
repository_path = """."""
analyze_code(repository_path)
