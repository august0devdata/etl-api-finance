{{ config(
    alias='accounts',
    schema='finance_prod_stg' 
) }}

with accounts_raw as (
    select 
      * 
    from 
      {{ source('public', 'raw_account') }} 
), 
accounts as (
select
    "ClientId"::int as id_cliente, 
    "Agencia"::int as agencia,
    "NomeConta"::varchar as tipo_conta, 
    {{ current_timestamp() }} as data_carga
from accounts_raw 
), 
 distinct_accounts as (
  select 
    distinct *
   from accounts
 ) select * from distinct_accounts

        