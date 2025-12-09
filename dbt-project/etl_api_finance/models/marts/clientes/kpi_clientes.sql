{{ config(materialized="view") }}

with stg_clientes as (
    select 
        *
    from {{ ref('clients') }}
), agg_clientes as (
select 
   cli.nome::varchar as cliente, 
   trs.agencia::float as agencia_origem,
   
from 
  stg_clientes cli
  left join 
  (
    select 
      * 
    from 
      {{ref('transactions')}} 
  ) trs
  on cli.id_cliente = trs.id_cliente
)
