{{ config (materialized='table')}}


select
  REGEXP_REPLACE(text, '<[^>]+>', ' ') as cleaned_text,
  TRY_TO_DATE(date,'yyyy-MM-dd') as article_date,
  LOWER(TRIM(label)) as label,
  CURRENT_TIMESTAMP() as cleaned_at
from {{ source('raw','RAW_NEWS_DATA')}}
  