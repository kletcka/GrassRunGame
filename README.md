# GrassRunGame  
Игра про несчастную траву 
  
  
## main.py
  
**Переменные** 
WIDTH - int; Ширина экрана  
HEIGHT - int; Высота экрана  
screen - ?; экран  
clock - ?; таймер  
done - boolean; для цикла  
mode - boolean; режим меню/игра  
max_x = int; счет  
cur_x = int; тек. позиция  
hero  - object; трава  
g_o - object; надпись Game Over
spacen - object; изображение пробела
fields - list; поля
cars - list; машины

**Функции**
up_list() - пересоздание fields и cars

## objects.py  
### Классы:  
#### Hero()  
**Атрибуты:**   
image_adress - str?; путь  
my_image - ?; изображение  
x - int; положение по Х  
y - int; положение по Y   
rect - Rect;  для травы  
**Методы:**  
draw(screen)  
*screen* - ?; экран, где рисовать изображение  
  
#### Over()  
**Атрибуты:**    
image_adress - str?; путь  
my_image - ?; изображение  
x - int; положение по Х  
y - int; положение по Y  
**Методы:**   
draw(screen)  
*screen* - ?; экран, где рисовать изображение  
   
#### Space()      
**Атрибуты:**    
image_adress - str?; путь  
my_image - ?; изображение  
x - int; положение по Х  
y - int; положение по Y   
rect - Rect;  для пробела    
**Методы:**   
draw(screen)   
*screen* - ?; экран, где рисовать изображение   
   
#### Field()    
**Атрибуты:**   
image_adress - str?; путь  
my_image - ?; изображение  
x - int; положение по Х  
y - int; положение по Y   
**Методы:**   
draw(screen)   
*screen* - ?; экран, где рисовать изображение      
move(vector, step)  
*vector* -  str ('X'/'Y'); направление движения   
*step* - int; на сколько двигается   
 
#### Car()     
**Атрибуты:**   
image_adress - str?; путь  
my_image - ?; изображение  
x - int; положение по Х  
y - int; положение по Y 
rect - Rect;  для машины  
v - int; направление движения   
color - int; цвет   
way - str; название файла  
**Методы:**    
draw(screen)    
*screen* - ?; экран, где рисовать изображение    
move(step)  
*step* - int; на сколько двигается  
g_move(step, ystep)  
*step* - int; на сколько двигается по X   
*ystep* - int; на сколько двигается по Y  
