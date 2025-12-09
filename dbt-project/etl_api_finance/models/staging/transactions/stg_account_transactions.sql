{{ config(
    alias='transactions',
    schema='finance_prod_stg'  
) }}


with transactions as (
    select 
      * 
    from 
      {{ source('public', 'raw_account') }} 
)
select
    "ClientId"::int as id_cliente, 
    "Agencia"::int as agencia, 
    "Valor"::float as valor, 
    "TipoTransacao"::varchar as tipo_transacao, 
    "DescricaoTransacao"::varchar as descricao_transacao, 
    {{ current_timestamp() }} as data_carga
from transactions

        