echo "Введіть будь-яке число:"
read number

if [ "$number" -gt 100 ]; then
    echo "Число $number БІЛЬШЕ ніж 100."
elif [ "$number" -eq 100 ]; then
    echo "Число дорівнює рівно 100."
else
    echo "Число $number МЕНШЕ ніж 100."
fi