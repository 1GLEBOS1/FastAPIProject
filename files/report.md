---
## Front matter
title: "Лабораторная работа №13"
subtitle: "Администрирование локальных сетей"
author: "Скандарова Полина Юрьевна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Провести подготовительные мероприятия по организации взаимодействия через сеть провайдера посредством статической маршрутизации локальной сети с сетью основного здания, расположенного в 42-м квартале в Москве, и сетью филиала, расположенного в г. Сочи.

# Выполнение лабораторной работы

Вношу изменения в схемы L1, L2 и L3 сети. На схеме предыдущего моего проекта размещаю необходимое оборудование: 4 медиаконвертера (Repeater-PT), 2 маршрутизатора типа Cisco 2811, 1 маршрутизирующий коммутатор типа Cisco 3560-24PS, 2 коммутатора типа Cisco 2950-24, коммутатор Cisco 2950-24T, 3 оконечных устройства типа PC-PT (рис. [-@fig:001]).

![Схема сети с дополнительными площадками](image/1.png){#fig:001 width=70%}

Присваиваю названия размещённым объектам. На медиаконвертерах заменяю имеющиеся модули на PT-REPEATER-NM-1FFE и PT-REPEATER-NM-1CFE для подключения витой пары по технологии Fast Ethernet и оптоволокна соответственно (рис. [-@fig:002]).

![Медиаконвертер с модулями PT-REPEATER-NM-1FFE и PT-REPEATER-NM-1CFE](image/2.png){#fig:002 width=70%}

На маршрутизаторе msk-q42-gw-1 добавляю дополнительный интерфейс NM-2FE2W (рис. [-@fig:003]).

![Маршрутизатор с дополнительным интерфейсом NM-2FE2W](image/3.png){#fig:003 width=70%}

В физической рабочей области Packet Tracer добаляю в г. Москва здание 42-го квартала, присваиваю ему соответствующее название (рис. [-@fig:004]).

![Здание основной территории организации в Москве на физической схеме проекта](image/4.png){#fig:004 width=70%}

В физической рабочей области Packet Tracer добавляю город Сочи и в нём здание филиала, присваиваю ему соответствующее название (рис. [-@fig:005]).

![Москва и Сочи на физической схеме проекта](image/11.png){#fig:005 width=70%}

Переношу из сети «Донская» оборудование сети 42-го квартала и сети филиала в соответствующие здания. Провожу соединение объектов согласно скорректированной мной схеме L1.

(рис. [-@fig:006] рис. [-@fig:007] рис. [-@fig:008] рис. [-@fig:009] рис. [-@fig:010] рис. [-@fig:011])

![Первоначальная настройка маршрутизатора msk-q42-gw-1](image/5.png){#fig:006 width=70%}

![Первоначальная настройка коммутатора msk-q42-sw-1](image/6.png){#fig:007 width=70%}

![Первоначальная настройка маршрутизирующего коммутатора msk-hostel-gw-1](image/7.png){#fig:008 width=70%}

![Первоначальная настройка коммутатора msk-hostel-sw-1](image/8.png){#fig:009 width=70%}

![Первоначальная настройка коммутатора sch-sochi-sw-1](image/9.png){#fig:010 width=70%}

![Первоначальная настройка маршрутизатора sch-sochi-gw-1](image/10.png){#fig:011 width=70%}

# Выводы

Проведены подготовительные мероприятия по организации взаимодействия через сеть провайдера посредством статической маршрутизации локальной сети с сетью основного здания, расположенного в 42-м квартале в Москве, и сетью филиала, расположенного в г. Сочи.

