{% macro dynamic_pivot(table, index, column, value) %}

    {# 1. Buscar todos os valores distintos da coluna para pivotar #}
    {% set query %}
        select distinct {{ column }} from {{ table }}
    {% endset %}

    {% set results = run_query(query).columns[0].values() %}

    {# 2. Criar os CASE WHEN dinamicamente #}

    {% set pivot_cases = [] %}

    {% for c in results %}
        {% set case_sql %}
            sum(case when {{ column }} = '{{ c }}' then {{ value }} else 0 end) as {{ c|lower }}
        {% endset %}
        {% do pivot_cases.append(case_sql) %}
    {% endfor %}

    {# 3. Retorna o SQL final #}

    select 
        {{ index }},
        {{ pivot_cases | join(',\n        ') }}
    from {{ table }}
    group by {{ index }}

{% endmacro %}
