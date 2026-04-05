# Анализ датасета резюме

В репозитории собраны материалы по очистке, разведывательному анализу и проверке гипотез для датасета резюме с портала «Работа России».

## Данные

- Исходный датасет: [dataset.xlsx](/Users/max/shit/dano_spring/dataset.xlsx)
- Очищенный датасет: [dataset_cleaned.csv](/Users/max/shit/dano_spring/dataset_cleaned.csv)
- Описание задания: [Задание.pdf](/Users/max/shit/dano_spring/Задание.pdf)
- Справочник регионов: [regions.csv](/Users/max/shit/dano_spring/regions.csv)
- Расширенный справочник регионов: [regions_extended.csv](/Users/max/shit/dano_spring/regions_extended.csv)

## Ноутбуки

- [data_cleaning.ipynb](/Users/max/shit/dano_spring/data_cleaning.ipynb)  
  Ноутбук очистки данных. В нём загружается исходный датасет, формируются служебные признаки, применяется фильтрация по дубликатам, зарплате, опыту и водительским резюме, после чего сохраняется `dataset_cleaned.csv`.

- [eda_dataset.ipynb](/Users/max/shit/dano_spring/eda_dataset.ipynb)  
  Разведывательный анализ исходного датасета. Содержит анализ пропусков, описательные статистики, разрезы по полу, образованию, занятости, регионам, тегам регионов, федеральным округам, времени публикации, а также корреляционный анализ.

- [hypothesis_mobile_salary_welch_ttest.ipynb](/Users/max/shit/dano_spring/hypothesis_mobile_salary_welch_ttest.ipynb)  
  Проверка гипотезы о том, что мобильные соискатели в среднем имеют более высокие зарплатные ожидания, с помощью одностороннего двухвыборочного t-критерия Уэльча.

- [hypothesis_mobile_salary_levene.ipynb](/Users/max/shit/dano_spring/hypothesis_mobile_salary_levene.ipynb)  
  Проверка гипотезы о равенстве дисперсий зарплатных ожиданий у мобильных и немобильных соискателей с помощью теста Левене.

- [hypothesis_mobile_salary_skfo_robustness.ipynb](/Users/max/shit/dano_spring/hypothesis_mobile_salary_skfo_robustness.ipynb)  
  Проверка устойчивости гипотезы по регионам Северо-Кавказского федерального округа. В ноутбуке считаются тест Левене и Welch t-test по каждому региону округа, строятся сравнительные таблицы и графики.

## Логика признака мобильности

В гипотезах мобильными считаются соискатели, которые удовлетворяют хотя бы одному условию:

- готовы к командировкам;
- готовы к переезду;
- готовы работать вахтовым методом.

## Результат очистки

Основной рабочий файл для дальнейшего анализа и проверки гипотез: [dataset_cleaned.csv](/Users/max/shit/dano_spring/dataset_cleaned.csv).
