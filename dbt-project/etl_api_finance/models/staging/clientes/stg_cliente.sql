{{ config(
    alias='clients',
    schema='finance_prod_stg'  
) }}

with clientes_raw as (
    select 
      * 
    from 
      {{ source('public', 'raw_cliente') }} 
)
select
    id::int as id_cliente, 
    "Name"::varchar as nome, 
    "Email"::varchar as email, 
    "DataNascimento"::date as data_nascimento, 
    "Cidade"::varchar as cidade, 
    "Estado"::varchar as estado, 
    {{ current_timestamp() }} as data_carga
from clientes_raw

        