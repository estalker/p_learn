#1. В проекте, где вы решаете домашние задания, создайте модуль 'homework5.py' и напишите весь код в нём.

#2. Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (True, "Месяц", 6, [1,31])
#  - Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)

#3. Изменение значений переменных:
#  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

try:
    immutable_var[2] = 5
except TypeError:
    print("Имплементация tuple на cpython выдает ошибку в методе set:" +
          """int
PyTuple_SetItem(PyObject *op, Py_ssize_t i, PyObject *newitem)
{
    PyObject **p;
    if (!PyTuple_Check(op) || Py_REFCNT(op) != 1) {
        Py_XDECREF(newitem);
        PyErr_BadInternalCall();
        return -1;
    }
    if (i < 0 || i >= Py_SIZE(op)) {
        Py_XDECREF(newitem);
        PyErr_SetString(PyExc_IndexError,
                        "tuple assignment index out of range");
        return -1;
    }
    p = ((PyTupleObject *)op) -> ob_item + i;
    Py_XSETREF(*p, newitem);
    return 0;
}
""")

immutable_var[3][1] = 5

#4. Создание изменяемых структур данных:
#  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1,'a','b']
#  - Измените элементы списка mutable_list.
mutable_list[1] = 5
#  - Выведите на экран измененный список mutable_list.
print(mutable_list)
