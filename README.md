## CAH Telegram Bot

*En Desarrollo*

Bot de Telegram que permite jugar en grupos al juego de mesa [Cartas Contra la Humanidad](https://cardsagainsthumanity.com/).
Creado con [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)


#### Instalación

``` bash
# crear y activar entorno virtual
virtualenv CAHenv
source CAHenv/bin/activate

# instalar dependencias
pip install pytelegrambotapi

# establecer token
mv TOKEN_py TOKEN.py
vi TOKEN.py

# ejecutar bot
python polling.py

```

---

#### ToDo
- [X] Mostrar carta negra.
- [X] Mostrar cartas blancas a los jugadores.
- [X] Votación.
- [X] Almacenar puntos.
- [X] Comenzar nuevas rondas.
- [X] Finalizar partida.
- [ ] Temporizadores.
- [ ] Opción de barajar tus cartas.
- [ ] Soporte para cartas pick2.
- [ ] Configuración independiente por grupo.
- [ ] Ranking de grupo.
- [ ] Ranking global.