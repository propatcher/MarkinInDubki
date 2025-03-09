# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.


define k = Character('Куляс' , color="#34eb86")

define mc = Character('[povname]' , colo='#0000FF')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
default tgk = 0
default alco = 0
default nic = 0
default ruble = 0
default respect = 0
label start:
    "Добро пожаловать в игру!"
    $ povname = renpy.input("Как вас зовут?", length =32)
    mc "Так будет выглядить ваш диалог."
    "Вы очутились в Саранске, Республика Мордовия."

    scene bg idle
    with fade
    play music "bg1.mp3"

    "Вы не помните, как попали сюда и откуда у вас знания мордовского и русского языков."

    "Вы должны будете выжить в этом неизвестном и опасном мире Самарско-мордовоского быдла."

    show markidle at center
    with dissolve

    m "Здравствуй пацанчик, что ты тут забыл этот город только для крутых."
    play sound "mark1.mp3"
    with fade
    m "Шёл бы ты отсюда."

    play sound "hit1.mp3"

    "*Лещ*"

    stop music

    pause (1.0)
    scene bs
    with fade

    play music"bg2.mp3"

    scene bs

    "Вы были отпизжены главным быдлом Саранска :(."

    "Вы не помните сколько пролежали без сознания."

    "!!!!!"

    scene 2323
    with fade

    play music "kidle.mp3"
    show kidle at center

    k "Пацан валяйся где-то в другом месте."
    k "Давай пиздуй отсюда."
    play sound "hit1.mp3"
    stop music

    scene bs
    with fade
    play music "bg2.mp3"
    "Вы оказались на улице Саранска."
label call_mapUI:
    call screen MapUI
screen MapUI:
    add "map/mapmain.png"
    imagebutton:
        xpos 1000
        ypos 360
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action Jump("house1_pressed")
    imagebutton:
        xpos 1000
        ypos 260
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action Jump("house2_pressed")
    imagebutton:
        xpos 10
        ypos 10
        idle "menu/but.png"
        hover "menu/but1.png"
        action Jump("menu_pressed")

label house1_pressed:
    scene ma
    "Вы оказались у мордовия арены."
    with fade
    call screen MapUI
label house2_pressed:
    if respect == 0:
        "У вас недостаточно уважения (Ваше уважение [respect]) от быдла, вы не можете пройти."
        call screen MapUI
    elif respect > 0:
        k "О опять ты, извини за подъезд, не узнал в тебе ровного пацана"
label menu_pressed:
    call screen StatsUI
screen StatsUI:
    add "menubg"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40
            vbox:
                spacing 10
                text "Толер к ТГК" size 40
                text "Толер к Алкоголю" size 40
                text "Толер к никотину" size 40
                text "Рубли" size 40
                text "Уважение" size 40

            vbox:
                spacing 10
                text "[tgk]" size 40
                text "[alco]" size 40
                text "[nic]" size 40
                text "[ruble]" size 40
                text "[respect]" size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Jump("call_mapUI")

