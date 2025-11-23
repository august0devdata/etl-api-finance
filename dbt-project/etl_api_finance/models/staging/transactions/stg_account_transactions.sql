{{ config(alias='transactions') }}

with transactions as (
    select 
      * 
    from 
      {{ source('public', 'raw_account') }} 
), 
select
    "ClientInd"::int as id_cliente, 
    "Valor"::float as valor, 
    "TipoTransacao"::varchar as tipo_transacao, 
    "DescricaoTransacao"::varchar as descricao_transacao, 
    {{ current_timestamp() }} as data_carga
from transactions

        