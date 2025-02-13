// Définir les frames de l'animation du chien
const frames = [
            `
                     ,--._______,-. 
                   ,','  ,    .  ,_\`-. 
                  / /  ,' , _\` \`\`. |  )      \`-.. 
                 (,';'""\`/ '"\`-._ \` \\/ ______   \\\\ 
                   : ,o.-\`- ,o.  )\` -'      \`---.)) 
                   : , d8b ^-.   '|   \`.      \`    \`. 
                   |/ __:_     \`. |  ,  \`       \`    \\ 
                   | ( ,-.\`-.    ;'  ;   \`       :    ; 
                   | |  ,   \`.      /     ;      :    \\ 
                   ;-'\`:::._,\`.__),'             :     ; 
                  / ,  \`-   \`--                  ;     | 
                 /  \\                   \`       ,      | 
                (    \`     :              :    ,\\      | 
                 \\   \`.    :     :        :  ,'  \\    : 
                  \\    \`|-- \`     \\ ,'    ,-'     :-.-\'; 
                  :     |\`--.______;     |        :    : 
                   :    /           |    |         |   \\ 
                   |    ;           ;    ;        /     ; 
                 _/--' |   -grr-   :\`-- /         \\_:_:_| 
               ,',','  |           |___ \\ 
               \`^._,--'           / , , .) 
                                  \`-._,-'`,
            `
                     ,--._______,-. 
                   ,','  ,    .  ,_\`-. 
                  / /  ,' , _\` \`\`. |  )           ..-'
                 (,';'""\`/ '"\`-._ \` \\/ ______    //
                   : ,o.-\`- ,o.  )\` -'      \`---.)) 
                   : , d8b ^-.   '|   \`.      \`    \`. 
                   |/ __:_     \`. |  ,  \`       \`    \\ 
                   | ( ,-.\`-.    ;'  ;   \`       :    ; 
                   | |  ,   \`.      /     ;      :    \\ 
                   ;-'\`:::._,\`.__),'             :     ; 
                  / ,  \`-   \`--                  ;     | 
                 /  \\                   \`       ,      | 
                (    \`     :              :    ,\\      | 
                 \\   \`.    :     :        :  ,'  \\    : 
                  \\    \`|-- \`     \\ ,'    ,-'     :-.-\'; 
                  :     |\`--.______;     |        :    : 
                   :    /           |    |         |   \\ 
                   |    ;           ;    ;        /     ; 
                 _/--' |   -grr-   :\`-- /         \\_:_:_| 
               ,',','  |           |___ \\ 
               \`^._,--'           / , , .) 
                                  \`-._,-'`
];

// Sélectionner l'élément où afficher l'animation
const animationDiv = document.getElementById('ascii-animation');

let currentFrame = 0; // Indice de la frame actuelle

// Fonction pour afficher l'animation
function animate() {
    animationDiv.textContent = frames[currentFrame]; // Afficher la frame actuelle
    currentFrame = (currentFrame + 1) % frames.length; // Passer à la frame suivante
}

// Lancer l'animation toutes les 500ms
setInterval(animate, 500);