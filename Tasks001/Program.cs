// // Дано трехзначное число. Найти:
// а) число единиц в нем;
// б) число десятков в нем;
// в) сумму его цифр;
// г) произведение его цифр.

Console.Write("Введите трёхзначное число: ");
int Number = int.Parse(Console.ReadLine()!);

PrintNumberInfo(Number);

//===============================Методы===============================

int MultOfNumbers(int num)
{
    int sum = 1;
    for (int i = 0; i < 3; i++)
    {
        sum = sum * (num % 10);
        num = num / 10;
    }
    return sum;
}

int SumOfNumbers(int num)
{
    int sum = 0;
    for (int i = 0; i < 3; i++)
    {
        sum = sum + num % 10;
        num = num / 10;
    }
    return sum;
}

void PrintNumberInfo(int num)
{
    if (NumberCheck(num)) Console.WriteLine("Введено неверное число!");
    else
    {
        Console.WriteLine($"Число единиц в числе {num} равно {num}");
        Console.WriteLine($"Число десятков в числе {num} равно {num / 10}");
        Console.WriteLine($"Сумма цифр числа {num} равна {SumOfNumbers(num)}");
        Console.WriteLine($"Произведение цифр числа {num} равно {MultOfNumbers(num)}");
    }
}

bool NumberCheck (int num)
{
    if (num / 100 >= 10 || num / 100 < 1) return true;
    return false;
}
