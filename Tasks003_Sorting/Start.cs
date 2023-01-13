using static Infrastructure;
using static Sorting;


Console.WriteLine("Введите размер массива:");
int n = int.Parse(Console.ReadLine()!);
int[] array = CreateArray(n);
Console.WriteLine($"Исходный массив: [{String.Join(", ", array)}]");
Console.WriteLine();
Console.WriteLine("Выберите вид сортировки:");
Console.WriteLine("1. Сортировка выбором");
Console.WriteLine("2. Пузырьковая сортировка");
int sortNum = int.Parse(Console.ReadLine()!);

if (sortNum != 1 && sortNum != 2) Console.WriteLine("Такой сортировки не указано");
else
{
    if (sortNum == 1) ChooseSortArray(array);
    if (sortNum == 2) BubbleSortArray(array);
}
