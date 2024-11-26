from flask import Flask, Response, request
import time

app = Flask(__name__)

# Définition des codes de couleur ANSI
colors = {
    "red": "\033[31m",       # Rouge
    "green": "\033[32m",     # Vert
    "yellow": "\033[33m",    # Jaune
    "blue": "\033[34m",      # Bleu
    "magenta": "\033[35m",   # Magenta
    "cyan": "\033[36m",      # Cyan
    "reset": "\033[0m",      # Réinitialiser la couleur
}


# Frames de l'animation
frames = [
    """




    


         ,--._______,-. 
       ,','  ,    .  ,_`-. 
      / /  ,' , _` ``. |  )       `-.. 
     (,';'""`/ '"`-._ ` \/ ______    \\\\
       : ,o.-`- ,o.  )\` -'      `---.)) 
       : , d8b ^-.   '|   `.      `    `. 
       |/ __:_     `. |  ,  `       `    \ 
       | ( ,-.`-.    ;'  ;   `       :    ; 
       | |  ,   `.      /     ;      :    \ 
       ;-'`:::._,`.__),'             :     ; 
      / ,  `-   `--                  ;     | 
     /  \                   `       ,      | 
    (    `     :              :    ,\      | 
     \   `.    :     :        :  ,'  \    : 
      \    `|-- `     \ ,'    ,-'     :-.-'; 
      :     |`--.______;     |        :    : 
       :    /           |    |         |   \ 
       |    ;           ;    ;        /     ; 
     _/--' |   -grr-   :`-- /         \_:_:_| 
   ,',','  |           |___ \ 
   `^._,--'           / , , .) 
                      `-._,-' 
""","""







         ,--._______,-. 
       ,','  ,    .  ,_`-. 
      / /  ,' , _` ``. |  )             ..-'
     (,';'""`/ '"`-._ ` \/ ______     //
       : ,o.-`- ,o.  )\` -'      `---.)) 
       : , d8b ^-.   '|   `.      `    `. 
       |/ __:_     `. |  ,  `       `    \ 
       | ( ,-.`-.    ;'  ;   `       :    ; 
       | |  ,   `.      /     ;      :    \ 
       ;-'`:::._,`.__),'             :     ; 
      / ,  `-   `--                  ;     | 
     /  \                   `       ,      | 
    (    `     :              :    ,\      | 
     \   `.    :     :        :  ,'  \    : 
      \    `|-- `     \ ,'    ,-'     :-.-'; 
      :     |`--.______;     |        :    : 
       :    /           |    |         |   \ 
       |    ;           ;    ;        /     ; 
     _/--' |   -grr-   :`-- /         \_:_:_| 
   ,',','  |           |___ \ 
   `^._,--'           / , , .) 
                      `-._,-' 
"""
]

# Liste des couleurs dans l'ordre souhaité
color_sequence = ["cyan", "blue", "magenta", "red", "yellow", "green"]

# Fonction pour appliquer la couleur
def apply_color(frame, color):
    return colors.get(color, colors["reset"]) + frame + colors["reset"]

@app.route("/")
def animated_ascii():
    def generate():
        color_index = 0
        while True:
            for frame in frames:
                # Appliquer la couleur actuelle à la frame
                current_color = color_sequence[color_index]
                colored_frame = apply_color(frame, current_color)
                yield colored_frame + "\n"
                time.sleep(0.3)  # Pause entre les frames

                # Passer à la couleur suivante
                color_index = (color_index + 1) % len(color_sequence)
    

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)