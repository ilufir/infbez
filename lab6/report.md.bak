---
# Front matter
title: "Лабораторная работа 4"
subtitle: "Дискреционное разграничение прав в Linux. Расширенные атрибуты"
author: "Илья Валерьевич Фирстов"

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
### Fonts
mainfont: comic.ttf
romanfont: comic.ttf
sansfont: comic.ttf
monofont: comic.ttf
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
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
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Получение практических навыков работы в консоли с расширенными атрибутами файлов

# Задание

Ознакомиться с расширенными атрибутами файлов в терминале системы Linux 

# Теоретическое введение

Изначально каждый файл имел три параметра доступа. Вот они:

    Чтение - разрешает получать содержимое файла, но на запись нет. Для каталога позволяет получить список файлов и каталогов, расположенных в нем;
    Запись - разрешает записывать новые данные в файл или изменять существующие, а также позволяет создавать и изменять файлы и каталоги;
    Выполнение - вы не можете выполнить программу, если у нее нет флага выполнения. Этот атрибут устанавливается для всех программ и скриптов, именно с помощью него система может понять, что этот файл нужно запускать как программу.

Но все эти права были бы бессмысленными, если бы применялись сразу для всех пользователей. Поэтому каждый файл имеет три категории пользователей, для которых можно устанавливать различные сочетания прав доступа:

    Владелец - набор прав для владельца файла, пользователя, который его создал или сейчас установлен его владельцем. Обычно владелец имеет все права, чтение, запись и выполнение.
    Группа - любая группа пользователей, существующая в системе и привязанная к файлу. Но это может быть только одна группа и обычно это группа владельца, хотя для файла можно назначить и другую группу.
    Остальные - все пользователи, кроме владельца и пользователей, входящих в группу файла.


# Выполнение лабораторной работы

Проверил атрибуты файла file1 и изменил права доступа (рис. [-@fig:001])

![Атрибуты файла file1](image/1.png){ #fig:001 width=70% }

Добавил файлу расширенный атрибут а (рис. [-@fig:002])

![Расширенный атрибут а](image/2.png){ #fig:002 width=70% }

Попытался после этого записать в файл данные. Произошла ошибка доступа(рис. [-@fig:003])

![Попытка записи в файл данных](image/3.png){ #fig:003 width=70% }

После добавления атрибута а недоступна даже смена владельца или прав доступа, до тех пор, пока не убран атрибут (рис. [-@fig:004])

![Проверка смены владельца и удаление атрибута а](image/4.png){ #fig:004 width=70% }

После этого все операции снова доступны. Установка прав 000 закономерно отбирает у пользователя права на запись и чтение.(рис. [-@fig:005])

![Проведение операций после снятия атрибута а](image/5.png){ #fig:005 width=70% }

# Выводы

Я ознакомился с ограничением прав в терминале системы Linux

# Список литературы{.unnumbered}

https://losst.ru/prava-dostupa-k-fajlam-v-linux
