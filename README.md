![Build Status](https://github.com/DevilishSasuke/testing_part2/actions/workflows/tests.yml/badge.svg)

# Проект

Проект для освоения автоматического тестирования ПО с использованием различных инструментов.

В проекте используются такие инструменты, как pytest, GitHub Actions, Coveralls, SonarCloud.

Комментарии в исходных файлах написаны в формате Google Style Docstring.

# Описание

Для приложения разработаны 2 класса. 
Они не имеют никакого практического применения и 
не гарантируют качество реализованных функций, 
а сделаны лишь для тестирования на них инструментов.

### Matrix

Класс, представляющий саму сущность матрицы и самые базовые операции с ней

#### Перменные класса:

##### public:
	Не содержит.

##### private:
	__rows: int - содержит в себе текущее количество строк матрицы
	имеет getter property - rows, не имеет setter'a
		
	__cols: int - содержит в себе текущее количество столбцов матрицы
	имеет getter property - cols, не имеет setter'a
		
	__matrix: list[list[float]]- содержит в себе текущие элементы матрицы
	имеет private setter для установки новой матрицы (используется при create())
	
##### protected:
	_defaultValue: int - представляет из себя переменную, 
	которая используется при заполнении матрицы новыми значениями
	
	
#### Методы класса:

	__init__ - стандартный инициализатор и конструктор класса
	create - запасной конструктор класса для создания сущности 
	на основе существующей матрицы(её элементов)
	set_default_value - устанавливает значение для инициализации матрицы
	reset_default_value - ставит значение для инициализации по умолчанию (=1)

#### Методы сущности:

fill_with_random - заполняет матрицу текущего размера случайными значениями <br>
resize - изменяет размер матрицы, заполняя её случайными значенями или _defaultValue <br>
transpose - свойство, транспонирует матрицу <br>
set_matrix - приватный метод для изменения текущих элементов матрицы на основе существующей <br>
get_matrix - свойство, получение элементов матрицы списком <br>
is_square - свойство, показывает, квадратная ли матрица <br>

	
Более подробно можно о всех методах прочитать в [тех. документации](DOCS.md)
		

### MatrixOperators

Представляет из себя более сложные операции с матрицами. Является статическим.

#### Перменные класса:

Не содержит.
	
	
#### Методы класса:

	diag - считает сумму элементов матрицы, лежащих на диагонали <br>
	determinant -  считает определитель для матриц размером 1х1, 2х2, 3х3 <br>
	power_elements - возводит все элементы матрицы в указанную степень <br>
	add_matrices - складывает две матрицы и возвращает их в 1 новом объекте <br>

#### Методы сущности:

Не содержит.
	
Более подробно можно о всех методах прочитать в тех. документации

# Установка и запуск

### Установка

1. Клонирование репозитория:
	```
	git clone https://github.com/DevilishSasuke/testing_part2
	cd testing_part2
	```

2. Создание виртуальной среды (на примере venv)
	```
	python -m venv .venv
	.venv\Scripts\activate
	
	```
	
3. Установка зависимостей
	```
	python -m pip install -r req.txt
	```
	
	
### Запуск тестов вручную

1. Из главной директории репозитория (testing_part2)
```
python -m pytest tests/

при желании можно добавить флаги для генерации отчётов xml или html:
--cov=mat --cov-report=xml --cov-report=html
```

### Запуск приложения

1. Из главной директории репозитория (testing_part2)
  ```
  python main.py
  ```

### Обновление документации

1. Чтобы обновить документацию в DOCS на основе документации из модуля mat (должна быть в формате Google Style Docstring)
  ```
  pydoc-markdown -p mat --render-toc >DOCS.md
  ```

# Описание тестов

## Блочные тесты | Unit tests

### Тесты для класса Matrix

#### Позитивные тесты

1. ```test_matrix_init()``` <br>
 Тест успешной инициализации при создании сущности класса
 
2. ```test_matrix_create()``` <br>
 Тест на успешное создание сущности класса при использовании готовых значений для матрицы
 
3. ```test_create_square_matrix()``` <br>
 Тест на корректность работы свойства is_square
 
4. ```test_fill_with_random()``` <br>
 Тест на успешное заполнение матрицы случайными значениями с разными типами
 
5. ```test_resize()``` <br>
 Тест на изменение размеров матрицы
 
6. ```test_resize_extend_matrix()``` <br>
 Тест на корректное расширение матрицы при изменениии размеров с случайными и дефолтными значениями

7. ```test_resize_dont_replace_content()``` <br>
 Тест на замещение данных матрицы при расширении и уменьшении размеров
 
8. ```test_transpose()``` <br>
 Тест на правильное транспонирование матрицы

#### Негативные тесты

9. ```test_wrong_matrix_shapes()``` <br>
 Тест исключения при неправильной форме матрицы при инициализации
 
10. ```test_wrong_range_on_fill()``` <br>
 Тест исключения при неправильно выбранном диапазоне для заполнения матрицы случайными числами
 
11. ```test_resize_validation()``` <br>
 Тест исключения при некорректной форме матрицы при изменении размера
 
12. ```test_empty_matrix_create()``` <br>
 Тест исключения при создании матрицы с переданной пустой матрицей или заполненной матрицей, но с пустыми рядами
 
13. ```test_dif_row_lens()``` <br>
 Тест исключения, если передать при создании существующую матрицу, у которой строки разной длины. 
 Пример: [[1, 2, 3], [4, 5]

#### Тесты на права доступа переменных и методов

14. ```test_private_variable()``` <br>
 Тест исключения при обращении к приватной переменной и корректная обработка её изменения

15. ```test_protected_and_private_methods()``` <br>
 Тест исключение при нарушении доступа к private и protected переменным и методам
 
### Тесты для класса MatrixOperators

#### Позитивные тесты

16. ```test_power_elements()``` <br>
 Тест корректности возведения в степень всех элементов матрицы
 
17. ```test_diag()``` <br>
 Тест вычисления суммы диагонали элементов матрицы
 
18. ```test_determinant()``` <br>
 Тест на расчёт определителя матрицы
 
19. ```test_add_matrices()``` <br>
 Тест на успешное сложение двух матриц

#### Негативные тесты

20. ```test_not_square_determ()``` <br>
 Тест исключения при неквадратной матрице в расчете определителя
 
21. ```test_wrong_shape_determ()``` <br>
 Тест исключения при выходе за диапазон размеров допустимых для расчета матриц
 
22. ```test_dif_shapes_on_add()``` <br>
 Тест исключения при разных размерах матриц для сложения

## Интеграционные тесты | Integration tests

23. ```test_create_after_add_power_and_resize()``` <br>
 Тест на корректное поведение взаимодействия классов при создании матрицы из существующей,
 возведении её элементов в степень и сложение с самой собой, а затем изменение формы
 
24. ```test_wave_numbers_in_matrix()``` <br>
 Тест на создание "волны" из чисел от 1 до 3 в матрице <br>
 Итоговый размер - 6х6, итоговый вид:
	```
	[1, 1, 2, 2, 3, 3]
	[1, 1, 2, 2, 3, 3]
	[2, 2, 2, 2, 3, 3]
	[2, 2, 2, 2, 3, 3]
	[3, 3, 3, 3, 3, 3]
	[3, 3, 3, 3, 3, 3] 
	```

## Аттестационные тесты | Acceptance tests

25. ```test_complex_task_in_row()``` <br>
 Тест на корректное поведение взаимодействия классов	
 при сложных последовательных задачах вычисления, создания и форматирования

# Полная документация

Изучите файл [DOCS.MD](DOCS.md)

# Лицензия и контакты

--