from flask import Flask, Response
import time

app = Flask(__name__)

# Frames de l'animation
frames = [
    r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
""",
    r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
"""
]

@app.route("/")
def animated_ascii():
    def generate():
        while True:
            for frame in frames:
                yield frame + "\n"
                time.sleep(0.3)  # Pause entre les frames
    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)